from pathlib import Path

# This is a simple health checker for a Python repository.
def check_repository(repository):
    """Return whether the repository has each required item."""
    return {
        "README.md": (repository / "README.md").is_file(),
        "tests folder": (repository / "tests").is_dir(),
        "requirements.txt": (repository / "requirements.txt").is_file(),
    }


def main():
    repository = Path(".")
    checks = check_repository(repository)

    print("Repository health report")
    print("-----------------------")
    for name, present in checks.items():
        status = "PASS" if present else "MISSING"
        print(f"{name}: {status}")


if __name__ == "__main__":
    main()