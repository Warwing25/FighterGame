#!/bin/bash
# Quick push script for FighterGame
# Usage: ./push.sh "Your commit message here"

set -e

if [ -z "$1" ]; then
  echo "Usage: ./push.sh \"commit message\""
  exit 1
fi

git add -A
git commit -m "$1"
git push origin main

echo "Pushed to GitHub successfully."
