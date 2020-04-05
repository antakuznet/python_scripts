#!/usr/bin/env python3

import sys
import subprocess

old_name = "Old_File_Name"
new_name = "New_File_Name"

try:
    with open(sys.argv[1], 'r') as file:
        string = file.readlines()
        for line in string:
            new_line = line.replace(old_name, new_name).strip()
            subprocess.run(["mv", line.strip(), new_line])
except IndexError:
    print("Usage: {Script} {File with old file's names}")
