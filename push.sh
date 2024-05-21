#!/bin/bash

DATE="$(date -d "5 hour ago")"
FILE_PATH="./status.txt"


if [ ! -e "status.txt" ]; then
  touch status.txt
else 
 echo "status.txt was have"
fi


cat /dev/null > status.txt
git status -s > status.txt


LINE_COUNT=$(wc -l < "$FILE_PATH")


if [ $LINE_COUNT -eq 1 ]; then
  echo "нету изменений ( no changes found)"
else 
  echo "Pushing new localization changes"
  git add .
  git commit -m "commit at date: $DATE"
  git push origin main
  echo "Pushing completed"
fi

#в дальнейшем можно разбубенить чтоб в новую бранчу комитить

