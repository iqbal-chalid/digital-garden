from datetime import date
from pathlib import Path
import re

DATE_PREFIX_RE = re.compile(r"^\d{6}_")


def stamp_paths(
    targets: list[Path],
    update: bool = False,
    dry_run: bool = False,
) -> None:
    prefix = date.today().strftime("%y%m%d")

    for target in targets:
        if not target.exists():
            print(f"Not found: {target}")
            continue

        if target.is_dir():
            candidates = [item for item in target.iterdir() if item.is_file()]
        elif target.is_file():
            candidates = [target]
        else:
            continue

        for source in candidates:
            name = source.name
            has_prefix = DATE_PREFIX_RE.match(name) is not None

            if has_prefix and not update:
                print(f"Skipped: {name}")
                continue

            new_name = DATE_PREFIX_RE.sub("", name, count=1) if has_prefix else name
            destination = source.with_name(f"{prefix}_{new_name}")

            if destination == source:
                continue

            if destination.exists():
                print(f"Conflict: {destination.name}")
                continue

            if dry_run:
                print(f"Would rename: {name} -> {destination.name}")
                continue

            try:
                source.rename(destination)
                print(f"Renamed: {name} -> {destination.name}")
            except OSError as exc:
                print(f"Error: {name}: {exc}")
