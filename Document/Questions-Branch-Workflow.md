# Questions Branch Sync Workflow

## Overview
This repository uses a two-branch strategy:
- **main**: Contains complete content (questions + solutions in all languages)
- **questions**: Contains only question descriptions (README.md files from each question folder)

## How It Works

### Automatic Sync
When you push commits to the `main` branch, a GitHub Actions workflow automatically:
1. Extracts all README.md files from question folders
2. Updates the `questions` branch with only these question files
3. Removes all solution code (python/, javascript/, java/, etc.)

### Workflow File
Location: `.github/workflows/sync-questions.yml`

The workflow triggers on every push to main and:
- Preserves the root LICENSE and readme.md
- Copies README.md from each question folder
- Removes all solution directories and files
- Commits and pushes to the questions branch

## Usage

### Adding a New Question
1. Create a folder structure on main branch:
   ```
   question-name/
     ├── README.md        (question description)
     ├── python/
     │   └── solution.py
     └── javascript/
         └── solution.js
   ```

2. Commit and push to main:
   ```powershell
   git add .
   git commit -m "Add new question: question-name"
   git push origin main
   ```

3. The GitHub Actions workflow will automatically:
   - Sync `question-name/README.md` to the questions branch
   - Remove all solution folders
   - Push the update to questions branch

### Manual Sync (if needed)
If you need to manually trigger the sync:
1. Go to GitHub Actions tab in your repository
2. Select "Sync Questions to Questions Branch" workflow
3. Click "Run workflow" and select the main branch

## Branch Structure

### Main Branch
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

### Questions Branch
```
{question-name}/
  └── README.md
```

## Benefits
- Students can clone the `questions` branch to practice without seeing solutions
- Contributors work on the `main` branch with full access to solutions
- Questions automatically stay in sync with main branch
- No manual maintenance of two separate repositories
