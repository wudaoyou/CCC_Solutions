"""Small local correctness check; not a sandbox or a DMOJ score."""

import argparse
import json
from pathlib import Path
import subprocess
import sys
from time import perf_counter

from checkers import check_output
from fetch_data import test_directory

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("problem", nargs="?", help="e.g. 2023/senior/S1; omit to run all")
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    directories = [ROOT / args.problem] if args.problem else sorted(ROOT.glob("20??/*/*/solution.py"))
    directories = [p.parent if p.is_file() else p for p in directories]
    results = []
    for directory in directories:
        if (directory / "reference.json").exists():
            directory = (directory / json.loads((directory / "reference.json").read_text())["target"]).resolve()
        if not (directory / "solution.py").exists():
            parser.error(f"No solution: {directory}")
        name = directory.relative_to(ROOT).as_posix()
        cases = sorted(test_directory(directory).glob("*.in"))
        failures, longest = [], 0
        if not cases:
            failures.append("no test inputs")
        for case in cases:
            wanted = case.with_suffix(".out")
            if not wanted.exists():
                failures.append(f"{case.name}: missing expected output")
                continue
            started = perf_counter()
            try:
                process = subprocess.run(
                    [sys.executable, "-I", str(directory / "solution.py")],
                    input=case.read_bytes(), capture_output=True, timeout=10, cwd=ROOT,
                )
                if process.returncode or not check_output(name, case.read_bytes(), process.stdout, wanted.read_bytes()):
                    failures.append(f"{case.name}: runtime error or wrong answer")
            except subprocess.TimeoutExpired:
                failures.append(f"{case.name}: exceeded local 10-second limit")
            longest = max(longest, perf_counter() - started)
        result = {"problem": name, "cases": len(cases), "failures": failures, "max_wall_seconds": round(longest, 4)}
        results.append(result)
        print(f"{name}: {len(cases) - len(failures)}/{len(cases)} passed", flush=True)
        for failure in failures:
            print(f"  {failure}", flush=True)
    if args.report:
        args.report.write_text(json.dumps(results, indent=2) + "\n")
    return int(any(r["failures"] for r in results))


if __name__ == "__main__":
    sys.exit(main())
