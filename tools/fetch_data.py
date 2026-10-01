"""Download and verify large official data packages; keep them out of Git."""

import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import urllib.request
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def test_directory(problem):
    source = json.loads((problem / "source.json").read_text())["test_data"]
    if source.get("storage") != "download":
        return problem / "tests"
    target = ROOT / ".data" / problem.relative_to(ROOT)
    count = len(list(target.glob("*.in")))
    if count != source["official_input_count"]:
        raise ValueError(f"Full data missing. Run: python3 tools/fetch_data.py {problem.relative_to(ROOT)}")
    return target


def fetch(problem):
    data = json.loads((problem / "source.json").read_text())["test_data"]
    if data.get("storage") != "download":
        print(f"{problem.relative_to(ROOT)}: full data is already bundled")
        return
    digest = data["archive_sha256"]
    archive = ROOT / ".data/_archives" / f"{digest}.zip"
    archive.parent.mkdir(parents=True, exist_ok=True)
    if not archive.exists():
        temporary = archive.with_suffix(".part")
        with urllib.request.urlopen(data["url"], timeout=60) as response, temporary.open("wb") as output:
            shutil.copyfileobj(response, output)
        with temporary.open("rb") as stream:
            valid = hashlib.file_digest(stream, "sha256").hexdigest() == digest
        if not valid:
            temporary.unlink()
            raise ValueError("Official archive hash mismatch")
        temporary.replace(archive)
    else:
        with archive.open("rb") as stream:
            if hashlib.file_digest(stream, "sha256").hexdigest() != digest:
                raise ValueError("Cached archive hash mismatch")
    target = ROOT / ".data" / problem.relative_to(ROOT)
    target.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(archive) as package:
        for member in data["members"]:
            name = Path(member).name
            if Path(name).suffix not in {".in", ".out"} or not re.fullmatch(r"[A-Za-z0-9_.-]+", name):
                raise ValueError(f"Unexpected data filename: {name}")
            with package.open(member) as stream, (target / name).open("wb") as output:
                shutil.copyfileobj(stream, output)
    result = test_directory(problem)
    print(f"{problem.relative_to(ROOT)}: {len(list(result.glob('*.in')))} full official cases ready")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("problem", help="e.g. 2025/senior/S4, or 2025 to fetch that year")
    args = parser.parse_args()
    selected = (ROOT / args.problem).resolve()
    if not selected.is_relative_to(ROOT):
        parser.error("Path must be inside this repository")
    sources = [selected / "source.json"] if (selected / "source.json").exists() else sorted(selected.glob("*/*/source.json"))
    if not sources:
        parser.error("No problems at that path")
    for source in sources:
        fetch(source.parent)


if __name__ == "__main__":
    main()
