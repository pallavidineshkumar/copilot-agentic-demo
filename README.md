# Repository Health Checker

This beginner-friendly Python application checks whether a repository contains
three useful project files and folders:

- `README.md`
- a `tests` folder
- `requirements.txt`

The report prints `PASS` when an item exists and `MISSING` when it does not.

## Setup

You need Python 3.8 or newer. The application uses only Python's standard
library, so there are no external packages to install.

Clone or download this repository, then open a terminal in its folder.

## Usage

Run the health checker with:

```bash
python app.py
```

Run the tests with:

```bash
python -m unittest discover
```

The older `health_checker.py` script is also included as an expanded example
that checks additional repository details.