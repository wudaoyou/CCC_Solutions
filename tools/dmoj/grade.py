"""Run inside the DMOJ Docker image; output goes to /results/dmoj.json."""

import json
from pathlib import Path
import re
import subprocess
import sys


def main():
    root = Path("/repo")
    sys.path.insert(0, str(root / "tools"))
    from fetch_data import test_directory
    workspace = Path("/tmp/ccc-dmoj")
    workspace.mkdir(exist_ok=True)
    (workspace / "judge.yml").write_text(json.dumps({
        "runtime": {"python3": "/usr/local/bin/python3"},
        "problem_storage_globs": [str(workspace / "problems/*")],
    }))
    results = []
    solutions = sorted(root.glob("20??/*/*/solution.py"))
    if len(sys.argv) > 1:
        selected = root / sys.argv[1]
        solutions = [selected / "solution.py"] if (selected / "solution.py").exists() else sorted(selected.glob("*/*/solution.py"))
    for solution in solutions:
        directory = solution.parent
        name = directory.relative_to(root).as_posix()
        year, level, number = name.split("/")
        problem_id = f"ccc{year}{number.lower()}"
        problem_dir = workspace / "problems" / problem_id
        problem_dir.mkdir(parents=True, exist_ok=True)
        cases = sorted(test_directory(directory).glob("*.in"))
        for case in cases:
            if not case.with_suffix(".out").exists():
                raise ValueError(f"Missing expected answer: {case}")
        checker = "standard"
        if name in {"2019/junior/J5", "2019/senior/S2"}:
            checker = "checker.py"
            (problem_dir / checker).write_text(
                'import sys\nsys.path.insert(0, "/repo/tools")\nfrom checkers import check_output\n'
                f'def check(process_output, judge_output, judge_input, **kwargs):\n'
                f'    return check_output({name!r}, judge_input, process_output, judge_output)\n'
            )
        elif name in {"2018/senior/S1", "2020/senior/S1", "2021/senior/S1"}:
            checker = {"name": "floats", "args": {"precision": 5}}
        (problem_dir / "init.yml").write_text(json.dumps({
            "checker": checker,
            "test_cases": [{"in": str(p), "out": str(p.with_suffix(".out")), "points": 1} for p in cases],
        }))
        command = ["dmoj-cli", "--no-ansi", "-c", str(workspace / "judge.yml"), "-e", "PY3",
                   "--", "submit", problem_id, "PY3", str(solution), "-tl", "3", "-ml", "262144"]
        process = subprocess.run(command, capture_output=True, text=True, timeout=600)
        log = process.stdout + process.stderr
        verdicts = re.findall(r"Test case\s+\d+\s+(\S+)", log)
        passed = bool(cases) and process.returncode == 0 and len(verdicts) == len(cases) and all(v == "AC" for v in verdicts)
        source = json.loads((directory / "source.json").read_text())
        results.append({
            "problem": name, "cases": len(cases), "passed": passed,
            "test_data_kind": source["test_data"]["kind"],
            "cpu_limit_seconds": 3, "memory_limit_kib": 262144,
            "verdicts": verdicts, "log": log,
        })
        print(f"{name}: {'PASS' if passed else 'FAIL'} ({verdicts.count('AC')}/{len(cases)})", flush=True)
        if not passed:
            print(log[-5000:], flush=True)
    report = {
        "judge": "DMOJ judge-server", "judge_commit": "5ef74c5d6cad9efb2e86a5bb8ff2c90aaa6e435c",
        "executor": "PY3", "results": results,
    }
    Path("/results/dmoj.json").write_text(json.dumps(report, indent=2) + "\n")
    return int(not results or any(not r["passed"] for r in results))


if __name__ == "__main__":
    sys.exit(main())
