# Introduction

This is a programming language repository that contains various questions and solutions. The solutions can be different programming languages. Each solution is stored in its respective folder named after the programming language. The repository is organized to facilitate easy navigation and understanding of different programming concepts through practical examples.


# Repository Structure
```
{question-name}/
  ├── python/
  │   └── solution1.py
  │   └── solution2.py
  ├── javascript/
  │   └── solution.js
  ├── java/
  │   └── Solution.java
  └── README.md
```

# Branch Structure

This repository uses a two-branch strategy to separate questions from solutions:

## Main Branch
The `main` branch contains the complete content including:
- Question descriptions (README.md files in each question folder)
- Solution code in multiple programming languages (python/, javascript/, java/, etc.)
- Full implementation details and examples

This branch is intended for:
- Contributors who want to add or review solutions
- Learners who want to study existing solutions
- Anyone who needs the complete codebase

## Questions Branch
The `questions` branch contains only:
- Question descriptions (README.md files)
- No solution code

This branch is intended for:
- Students who want to practice solving problems without seeing solutions
- Anyone who wants to attempt the challenges independently

The questions branch is automatically synchronized from the main branch via GitHub Actions. When new questions or solutions are added to main, only the question descriptions are copied to the questions branch.