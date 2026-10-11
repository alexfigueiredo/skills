#!/usr/bin/env python3
"""Search bundled design rules and return image paths without loading the images."""

import argparse
import json
import math
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "references" / "examples.json"
MODES = ("convert", "operate", "browse", "read", "experience")
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
    "animation": "animate", "animated": "animate", "animating": "animate",
    "motion": "animate", "transitions": "transition", "darkmode": "dark",
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
    ranked.sort(key=lambda item: -item[0])
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


def result(rule, query="", groups=1, all_figures=False, mode=None):
    ref, anchor = rule["reference"].split("#", 1)
    return {
        "id": rule["id"], "title": rule["title"], "topic": rule["topic"],
        "when": rule["when"], "recommendation": rule["summary"],
        "caution": rule["caution"], "mode_note": rule.get("modes", {}).get(mode),
        "reference": str(ROOT / ref) + "#" + anchor,
        "figures": [
            {k: (str(ROOT / v) if k == "path" else v) for k, v in f.items()}
            for f in select_figures(rule, query, groups, all_figures)
        ],
    }


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
    parser.add_argument("--topic", help="restrict to an exact topic ID")
    parser.add_argument("--mode", choices=MODES, help="add the rule's note for this page mode")
    parser.add_argument("--limit", type=bounded_int, default=3, help="maximum rules (default: 3)")
    parser.add_argument("--groups", type=bounded_int, default=1, help="figure groups per search result (default: 1)")
    parser.add_argument("--all-figures", action="store_true", help="include every figure in matching rules")
    parser.add_argument("--json", action="store_true", help="emit structured output")
    args = parser.parse_args()
    if args.query is not None and (args.rule or args.list_topics):
        parser.error("query cannot be combined with --rule or --list-topics")
    if args.query is None and not (args.rule or args.list_topics):
        parser.error("provide search terms, --rule or --list-topics")
    try:
        data = json.loads(INDEX.read_text(encoding="utf-8"))
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
        output = [result(r, args.query or "", args.groups, args.all_figures, args.mode) for r in matches]
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
                if item["mode_note"]:
                    print(f"In {args.mode} pages: " + item["mode_note"])
                print("Read: " + item["reference"])
                if not item["figures"]:
                    print("  No figures for this rule.")
                for f in item["figures"]:
                    print(f"  {f['role']} | {f['group']}: {f['caption']}")
                    print("  Open image: " + f["path"])
        return 0
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print("Example index error: " + str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
