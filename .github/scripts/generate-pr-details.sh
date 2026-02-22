#!/bin/bash

# --- 1. Header & Metadata ---
echo "### 🕵️ Automated PR Inspection"
echo ""
echo "**Commit:** \`$(git rev-parse --short HEAD)\`"
echo "**Time:** $(date)"
echo ""

# --- 2. Check for TODOs in the code ---
# We search recursively (-r) but ignore the .git folder
TODO_COUNT=$(grep -r "TODO" . --exclude-dir=.git --exclude-dir=node_modules 2>/dev/null | wc -l)

if [ "$TODO_COUNT" -gt "0" ]; then
  echo "- ⚠️ **Action Item:** Found **$TODO_COUNT** \`TODO\` comments in this branch."
else
  echo "- ✅ **Clean:** No \`TODO\` comments found."
fi

# --- 3. Check for Large Files (Over 1MB) ---
# This helps prevent accidentally committing binary files
LARGE_FILES=$(find . -type f -size +1M -not -path '*/.*' | wc -l)

if [ "$LARGE_FILES" -gt "0" ]; then
  echo "- 🏋️ **Size Warning:** Found **$LARGE_FILES** file(s) larger than 1MB."
else
  echo "- 🍃 **Size Check:** No overly large files found."
fi

# --- 4. Documentation Check ---
if [ -f "README.md" ]; then
  echo "- 📘 **Docs:** \`README.md\` exists."
else
  echo "- 📕 **Missing:** No \`README.md\` found. Please add documentation."
fi

# --- 5. Footer ---
echo ""
echo "---"
echo "_Generated automatically by GitHub Actions_"