#!/usr/bin/env python3
"""Search bundled design rules and return image paths without loading the images."""

import argparse
import hashlib
import json
import math
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "references" / "examples.json"
STOP = set("a an and are as at be been but by can do does for from has have how i if in into is it its me my of on or our should so than that the their them then there these they this to too use using want we what when which with would you your feels feel looks look make more less very really please help improve screen interface design".split())
ALIASES = {
    "nav": "navigation", "navbar": "navigation", "grey": "gray",
    "greys": "gray", "grays": "gray", "colour": "color", "colours": "color",
    "whitespace": "space", "photos": "photo", "images": "image",
    "cramped": "cramp", "cramping": "cramp", "crowded": "crowd",
    "crowding": "crowd", "competes": "compete", "competing": "compete",
    "confusing": "confuse", "confused": "confuse", "cluttered": "clutter",
    "sizing": "size", "sizes": "size", "spacing": "space", "gaps": "gap",
    "squeezed": "squeeze", "squeezing": "squeeze", "squished": "squeeze",
    "wrapping": "wrap", "wrapped": "wrap", "wraps": "wrap",
    "colliding": "collide", "collides": "collide", "overlapping": "overlap",
    "overflowing": "overflow", "overflows": "overflow", "tabs": "tab",
}


def tokens(text):
    words = re.findall(r"[\w]+", unicodedata.normalize("NFKC", text).casefold())
    result = set()
    for word in words:
        if word in STOP:
            continue
        word = ALIASES.get(word, word)
        if len(word) > 4 and word.endswith("s") and not word.endswith(("ss", "us")):
            word = word[:-1]
        result.add(word)
    return result


def fields(rule):
    # Exclude cautions: warning against removing form labels must not make the
    # data-label rule a strong match for a form-label problem.
    return [
        (tokens(rule["title"]), 5),
        (tokens(" ".join(rule["tags"])), 6),
        (tokens(rule["when"]), 4),
        (tokens(rule["summary"]), 2),
        (tokens(" ".join(f["caption"] for f in rule["figures"])), 1),
    ]


def search(rules, query, limit=3):
    wanted = tokens(query)
    if not wanted:
        return []
    prepared = [(rule, fields(rule)) for rule in rules]
    frequency = Counter(t for _, fs in prepared for t in set().union(*(ts for ts, _ in fs)))
    weights = {t: math.log(1 + len(rules) / (1 + frequency[t])) for t in wanted}
    ranked = []
    for rule, fs in prepared:
        hits = wanted & set().union(*(ts for ts, _ in fs))
        if not hits:
            continue
        score = sum(weight * sum(weights[t] for t in wanted & ts) for ts, weight in fs)
        score *= len(hits) / len(wanted)
        ranked.append((score, rule))
    ranked.sort(key=lambda item: (-item[0], item[1]["page"]))
    return [rule for _, rule in ranked[:limit]]


def select_figures(rule, query="", groups=1, all_figures=False):
    if all_figures:
        return rule["figures"]
    featured = set(rule["featured_figures"])
    wanted = tokens(query)
    if not wanted:
        return [f for f in rule["figures"] if f["id"] in featured]
    grouped = defaultdict(list)
    for figure in rule["figures"]:
        grouped[figure["group"]].append(figure)
    ordered = list(grouped.values())

    def score(group):
        # Average and strongest-caption relevance avoid rewarding large groups
        # just for having more images. Return the whole group to retain pairs.
        matches = [len(wanted & tokens(f["caption"] + " " + f["group"])) for f in group]
        return (max(matches) + sum(matches) / len(matches), any(f["id"] in featured for f in group))

    ordered.sort(key=score, reverse=True)
    return [f for group in ordered[:groups] for f in group]


def result(rule, query="", groups=1, all_figures=False):
    ref, anchor = rule["reference"].split("#", 1)
    return {
        "id": rule["id"], "title": rule["title"], "topic": rule["topic"],
        "page": rule["page"], "when": rule["when"], "recommendation": rule["summary"],
        "caution": rule["caution"], "reference": str(ROOT / ref) + "#" + anchor,
        "figures": [
            {k: (str(ROOT / v) if k == "path" else v) for k, v in f.items() if k != "sha256"}
            for f in select_figures(rule, query, groups, all_figures)
        ],
    }


def checked_path(relative):
    path = ROOT / relative
    if Path(relative).is_absolute() or not path.resolve().is_relative_to(ROOT):
        raise ValueError("Path escapes the skill: " + relative)
    if not path.is_file():
        raise ValueError("Missing file: " + relative)
    return path


def validate(data):
    if data["schema_version"] != 1:
        raise ValueError("Unsupported index schema")
    rules = data["rules"]
    if len(rules) != data["source"]["section_count"]:
        raise ValueError("Section count differs from source manifest")
    rule_ids, figure_ids, paths = set(), set(), set()
    for rule in rules:
        rid = rule["id"]
        if rid in rule_ids:
            raise ValueError("Duplicate rule: " + rid)
        rule_ids.add(rid)
        for field in ("title", "topic", "when", "summary", "caution", "tags", "figures", "featured_figures"):
            if not rule[field]:
                raise ValueError("Empty " + field + " in " + rid)
        ref, anchor = rule["reference"].split("#", 1)
        if anchor != rid or f'<a id="{anchor}"></a>' not in checked_path(ref).read_text(encoding="utf-8"):
            raise ValueError("Missing reference anchor: " + rule["reference"])
        groups = defaultdict(set)
        local_ids = set()
        for figure in rule["figures"]:
            fid = figure["id"]
            path = checked_path(figure["path"])
            if fid in figure_ids or figure["path"] in paths:
                raise ValueError("Duplicate figure: " + fid)
            figure_ids.add(fid)
            local_ids.add(fid)
            paths.add(figure["path"])
            if fid != path.stem or not re.fullmatch(r"fig-\d{3}-\d{3}", fid):
                raise ValueError("Invalid figure ID: " + fid)
            if figure["page"] != int(fid.split("-")[1]) or not rule["page"] <= figure["page"] <= data["source"]["pages"]:
                raise ValueError("Invalid page: " + fid)
            if min(figure["width"], figure["height"]) <= 0:
                raise ValueError("Invalid dimensions: " + fid)
            if figure["role"] not in {"before", "after", "comparison", "example", "problem", "diagram"}:
                raise ValueError("Invalid role: " + fid)
            if not figure["caption"].strip() or not figure["group"].strip():
                raise ValueError("Missing annotation: " + fid)
            if hashlib.sha256(path.read_bytes()).hexdigest() != figure["sha256"]:
                raise ValueError("Figure differs from source: " + fid)
            groups[figure["group"]].add(figure["role"])
        if not set(rule["featured_figures"]) <= local_ids:
            raise ValueError("Unknown featured figure: " + rid)
        featured_groups = defaultdict(set)
        for figure in rule["figures"]:
            if figure["id"] in rule["featured_figures"]:
                featured_groups[figure["group"]].add(figure["role"])
        for group, roles in featured_groups.items():
            if ("before" in roles) != ("after" in roles):
                raise ValueError("Incomplete featured pair: " + rid + "/" + group)
        for group, roles in groups.items():
            if ("before" in roles) != ("after" in roles):
                raise ValueError("Incomplete before/after group: " + rid + "/" + group)
    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    unlisted = sorted(rid for rid in rule_ids if "`" + rid + "`" not in skill)
    if unlisted:
        raise ValueError("Rules missing from SKILL.md: " + ", ".join(unlisted))
    if len(figure_ids) != data["source"]["figure_count"]:
        raise ValueError("Figure count differs from source manifest")
    actual = {str(p.relative_to(ROOT)) for p in (ROOT / "references/figures").glob("*.webp")}
    if paths != actual:
        raise ValueError("Unindexed or missing figures: " + ", ".join(sorted(paths ^ actual)))
    return {"rules": len(rules), "figures": len(figure_ids), "topics": len({r["topic"] for r in rules})}


def bounded_int(value):
    number = int(value)
    if not 1 <= number <= 10:
        raise argparse.ArgumentTypeError("use a number from 1 to 10")
    return number


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", nargs="?", help="quoted problem or search terms")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--rule", help="exact rule ID")
    mode.add_argument("--list-topics", action="store_true")
    mode.add_argument("--check", action="store_true", help="check corpus integrity and paired views")
    parser.add_argument("--topic", help="restrict to an exact topic ID")
    parser.add_argument("--limit", type=bounded_int, default=3, help="maximum rules (default: 3)")
    parser.add_argument("--groups", type=bounded_int, default=1, help="figure groups per search result (default: 1)")
    parser.add_argument("--all-figures", action="store_true", help="include every figure in matching rules")
    parser.add_argument("--json", action="store_true", help="emit structured output")
    args = parser.parse_args()
    if args.query is not None and (args.rule or args.list_topics or args.check):
        parser.error("query cannot be combined with --rule, --list-topics or --check")
    if args.query is None and not (args.rule or args.list_topics or args.check):
        parser.error("provide search terms, --rule, --list-topics or --check")
    try:
        data = json.loads(INDEX.read_text(encoding="utf-8"))
        if args.check:
            counts = validate(data)
            print(json.dumps(counts) if args.json else "OK: {rules} rules, {figures} figures, {topics} topics; references, hashes and paired views verified.".format(**counts))
            return 0
        rules = data["rules"]
        topics = list(dict.fromkeys(r["topic"] for r in rules))
        if args.list_topics:
            print(json.dumps(topics) if args.json else "\n".join(topics))
            return 0
        if args.topic:
            if args.topic not in topics:
                parser.error("unknown topic; use --list-topics")
            rules = [r for r in rules if r["topic"] == args.topic]
        if args.rule:
            matches = [r for r in rules if r["id"] == args.rule]
            if not matches:
                parser.error("unknown rule ID or rule excluded by --topic: " + args.rule)
        else:
            matches = search(rules, args.query, args.limit)
        output = [result(r, args.query or "", args.groups, args.all_figures) for r in matches]
        if args.json:
            print(json.dumps({"results": output}, ensure_ascii=False, indent=2))
        elif not output:
            print("No matching examples. Try concrete terms such as 'navigation', 'form spacing' or 'empty state', or use --list-topics.")
        else:
            for item in output:
                print(f"\n{item['id']} | {item['title']}")
                print("When: " + item["when"])
                print("Change: " + item["recommendation"])
                print("Caution: " + item["caution"])
                print("Read: " + item["reference"])
                for f in item["figures"]:
                    print(f"  {f['role']} | {f['group']}: {f['caption']}")
                    print("  Open image: " + f["path"])
        return 0
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print("Example index error: " + str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
