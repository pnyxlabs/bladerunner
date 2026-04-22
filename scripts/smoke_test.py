#!/usr/bin/env python3
"""Import-only smoke test for bladerunner_runner/.

Walks every .py file under bladerunner_runner/ and imports it. Files inside
proper packages (dir contains __init__.py) are imported by dotted name so
relative imports resolve; loose scripts (e.g. analysis/, Initiators/) are
loaded via importlib.util.spec_from_file_location.

No network, no database — purely a "does the code parse and import" check.

Exits 0 if every module imports cleanly, 1 otherwise with a per-failure
traceback.
"""
from __future__ import annotations

import importlib
import importlib.util
import sys
import traceback
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PACKAGE_ROOT = REPO_ROOT / "bladerunner_runner"

def iter_python_files(root: Path):
    for p in sorted(root.rglob("*.py")):
        if "__pycache__" in p.parts:
            continue
        yield p


def dotted_module_name(path: Path) -> str | None:
    """Return the dotted module name if every intermediate dir is a package."""
    rel = path.relative_to(REPO_ROOT)
    parts = list(rel.with_suffix("").parts)
    current = REPO_ROOT
    for part in parts[:-1]:
        current = current / part
        if not (current / "__init__.py").exists():
            return None
    if parts[-1] == "__init__":
        parts = parts[:-1]
    return ".".join(parts)


def import_by_path(path: Path) -> None:
    synthetic = "smoke__" + "_".join(path.relative_to(REPO_ROOT).with_suffix("").parts)
    spec = importlib.util.spec_from_file_location(synthetic, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"could not build import spec for {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[synthetic] = module
    spec.loader.exec_module(module)


def main() -> int:
    if str(REPO_ROOT) not in sys.path:
        sys.path.insert(0, str(REPO_ROOT))

    if not PACKAGE_ROOT.is_dir():
        print(f"smoke_test: package root not found at {PACKAGE_ROOT}", file=sys.stderr)
        return 2

    attempted = 0
    failures: list[tuple[Path, str]] = []

    for path in iter_python_files(PACKAGE_ROOT):
        attempted += 1
        dotted = dotted_module_name(path)
        label = dotted if dotted is not None else str(path.relative_to(REPO_ROOT))
        try:
            if dotted is not None:
                importlib.import_module(dotted)
            else:
                import_by_path(path)
        except BaseException:
            failures.append((path, traceback.format_exc()))
            print(f"FAIL {label}")
            continue
        print(f"ok   {label}")

    print()
    if failures:
        print(f"{len(failures)} of {attempted} modules failed to import:")
        for path, tb in failures:
            print("-" * 72)
            print(path.relative_to(REPO_ROOT))
            print(tb.rstrip())
        return 1

    print(f"all {attempted} modules imported cleanly")
    return 0


if __name__ == "__main__":
    sys.exit(main())
