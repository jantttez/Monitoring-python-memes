#!/bin/bash

DATE="$(date -d "5 hour ago")"
FILE_PATH="./status.txt"

cat /dev/null > status.txt
git status -s > status.txt


LINE_COUNT=$(wc -l < "$FILE_PATH")

LINE=$(git status -s | awk '{print $1}')

if [ ! -n $LINE ]; then
  echo "нету изменений ( no changes found)"
else 
  echo "Pushing new localization changes"
  git add .
  git commit -m "commit at date: $DATE"
  git push origin main
  echo "Pushing completed"
fi

#в дальнейшем можно разтурбировать чтоб в новую бранчу комитить


#if [ $LINE_COUNT -eq 1 ]; then