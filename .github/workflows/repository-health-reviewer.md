---
name: Repository Health Reviewer
description: Reviews the repository and identifies simple quality improvements
on:
  schedule:
    - cron: "0 9 * * 1"
  workflow_dispatch:

permissions:
  contents: read
  issues: write
---

# Repository Health Reviewer

Review this repository for basic health and quality issues.

Check the repository for:

- Missing README documentation
- Missing tests
- TODO comments
- Missing requirements.txt
- Obvious documentation problems
- Simple code-quality problems

Do not make destructive changes.

If problems are found:

1. Summarize the problems.
2. Create a GitHub issue describing the problems.
3. Provide recommended improvements.

If the repository is healthy, create a short summary indicating that no significant issues were found......