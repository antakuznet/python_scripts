#!/bin/bash
> oldfiles.txt
files=$(grep " name_to_change " list.txt | cut -d ' ' -f 3)
for file in $files; do
  if test -e $file; then
    echo $file >> oldfiles.txt
  fi
done
