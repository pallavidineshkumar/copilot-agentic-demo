"""A small, beginner-friendly repository health checker."""

from pathlib import Path
import argparse
import sys


def check_repository(repository: Path) -> list[tuple[str, bool, str]]:
    """Return the health checks for a repository directory."""
    checks = []

    checks.append(("Git repository", (repository / ".git").exists(), "A .git directory was found"))
    checks.append(("README file", (repository / "README.md").exists(), "README.md was found"))

    python_files = list(repository.rglob("*.py"))
    checks.append(("Python files", bool(python_files), f"Found {len(python_files)} Python file(s)"))

    test_files = [
        path
        for path in repository.rglob("*")
        if path.is_file() and (path.name.startswith("test_") or path.name.endswith("_test.py"))
    ]
    checks.append(("Tests", bool(test_files), f"Found {len(test_files)} test file(s)"))

    return checks


def print_report(repository: Path, checks: list[tuple[str, bool, str]]) -> None:
    """Print a readable report and a final summary."""
    print(f"Repository health: {repository.resolve()}")
    print("-" * 50)

    for name, passed, details in checks:
        status = "PASS" if passed else "WARN"
        print(f"[{status}] {name}: {details}")

    passed_count = sum(passed for _, passed, _ in checks)
    print("-" * 50)
    print(f"{passed_count}/{len(checks)} checks passed")


def main() -> int:
    parser = argparse.ArgumentParser(description="Check the basic health of a Python repository.")
    parser.add_argument(
        "repository",
        nargs="?",
        default=".",
        help="repository directory to check (default: current directory)",
    )
    args = parser.parse_args()

    repository = Path(args.repository)
    if not repository.is_dir():
        print(f"Error: directory not found: {repository}", file=sys.stderr)
        return 1

    checks = check_repository(repository)
    print_report(repository, checks)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())