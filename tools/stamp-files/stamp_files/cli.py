import argparse
from pathlib import Path

from .renamer import stamp_paths


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="stamp-files",
        description="Add today's YYMMDD_ prefix to files.",
    )

    parser.add_argument(
        "targets",
        nargs="+",
        type=Path,
        metavar="PATH",
        help="File or folder to process. Multiple paths are supported.",
    )

    parser.add_argument(
        "--update",
        action="store_true",
        help="Replace existing YYMMDD_ prefixes with today's date.",
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without renaming files.",
    )

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    stamp_paths(
        targets=args.targets,
        update=args.update,
        dry_run=args.dry_run,
    )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
