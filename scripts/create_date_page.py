#!/usr/bin/env python
import argparse
from datetime import datetime
from pathlib import Path


def parse_args():
    parser = argparse.ArgumentParser(
        description="Create a Hugo date archive page under content/date/"
    )
    parser.add_argument("date", help="Date in YYYY-MM-DD format")
    parser.add_argument(
        "--title",
        default=None,
        help="Optional page title (default: Posts on YYYY-MM-DD)",
    )
    parser.add_argument(
        "--content-root",
        default="content",
        help="Content root directory (default: content)",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite the date page if it already exists",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    try:
        dt = datetime.strptime(args.date, "%Y-%m-%d")
    except ValueError:
        raise SystemExit("Date must be in YYYY-MM-DD format.")

    content_root = Path(args.content_root)
    target_dir = content_root / "date"
    target_dir.mkdir(parents=True, exist_ok=True)
    target_file = target_dir / f"{args.date}.md"

    if target_file.exists() and not args.overwrite:
        raise SystemExit(
            f"{target_file} already exists. Use --overwrite to replace it."
        )

    title = args.title or f"Posts on {args.date}"
    front_matter = "\n".join(
        [
            "+++",
            f'title = "{title}"',
            f'date = "{dt.date().isoformat()}"',
            f'filterDate = "{dt.date().isoformat()}"',
            f'url = "/{dt.date().isoformat()}/"',
            "+++",
            "",
            f"This page lists posts published on {dt.date().isoformat()}.",
            "",
        ]
    )

    target_file.write_text(front_matter, encoding="utf-8")
    print(f"Created {target_file}")


if __name__ == "__main__":
    main()
