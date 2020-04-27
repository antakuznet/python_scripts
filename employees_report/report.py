#!/usr/bin/env python3
import csv
import datetime
import requests

FILE_URL="http://marga.com.ar/employees-with-date.csv"

def get_start_date():
    """Interactively get the start date to query for."""

    print()
    print('Getting the first start date to query for.')
    print()
    print('The date must be greater than Jan 1st, 2018')
    year = int(input('Enter a value for the year: '))
    month = int(input('Enter a value for the month: '))
    day = int(input('Enter a value for the day: '))
    print()

    return datetime.datetime(year, month, day)

def get_file_lines(url):
    """Returns the lines contained in the file at the given URL"""

    # Download the file over the internet
    response = requests.get(url, stream=True)

    # Decode all lines into strings
    lines = []
    for line in response.iter_lines():
        lines.append(line.decode("UTF-8"))
    return lines


def get_same_or_newer(start_date):

    """Returns the employees that started on the given date, or the closest one."""
    data = get_file_lines(FILE_URL)
    reader = csv.reader(data[1:])

    employees_list = list(reader)
    employees_list.sort(key=lambda x: x[3])

    # We want all employees that started at the same date or the closest newer
    # date. To calculate that, we go through all the data and find the
    # employees that started on the smallest date that's equal or bigger than
    # the given start date.
    min_date = datetime.datetime.today()
    employees_by_date = []

    for row in employees_list:
        date = datetime.datetime.strptime(row[3], '%Y-%m-%d')
        if date >= start_date and date <= min_date:
            employees_by_date.append("{}: {} {}".format(date, row[0], row[1]))

    return employees_by_date


def list_newer(start_date):

    employees = get_same_or_newer(start_date)

    for employee in employees:

        print("Started on " + employee)

def main():
    list_newer(get_start_date())

if __name__ == "__main__":
    main()
