#!/usr/bin/env python3

import csv
import re
import operator

errors = {}
users_list = {}

# Open log file to read all logs
with open("syslog.log", "r") as file:
  lines = file.readlines()
  # Check each log line for type and user
  for line in lines:
    result = re.search(r"ticky: ([A-Z]*) ([\w' #\[\]]*) \((\w*)\)", line)
    if result != None:
      if result[1] == "ERROR":
        if result[2] in errors:
          errors[result[2]] += 1
        else:
          errors[result[2]] = 1

        if result[3] in users_list:
          users_list[result[3]]["errors"] += 1
        else:
          users_list[result[3]] = {}
          users_list[result[3]]["info"] = 0
          users_list[result[3]]["errors"] = 1

      else:
        if result[3] in users_list:
          users_list[result[3]]["info"] += 1
        else:
          users_list[result[3]] = {}
          users_list[result[3]]["info"] = 1
          users_list[result[3]]["errors"] = 0
# Sort errors dictionary by value
sorted_errors = sorted(errors.items(), key = operator.itemgetter(1), reverse=True)

# Write errors into .csv file
with open("error_message.csv", "w") as file:
  file_writer = csv.writer(file)
  file_writer.writerow(["Error","Count"])
  for item in sorted_errors:
    file_writer.writerow(item)

# Sort user list dictionary by user's name
sorted_users = sorted(users_list.items(), key = operator.itemgetter(0))

# Write user's list into .csv file
with open("user_statistics.csv", "w") as file:
  file_writer = csv.writer(file)
  file_writer.writerow(["Username","INFO","ERROR"])
  for item in sorted_users:
    file_writer.writerow([item[0],item[1]["info"],item[1]["errors"]])
