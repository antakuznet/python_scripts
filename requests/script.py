#!/usr/bin/env python3

import os
import requests
import json
import csv

path = os.path.expanduser('~') + ''
url = 'https://'

for file in os.listdir(path):
    if '.csv' in file and '.' not in file[0]:
        print(file)
        user_dict = {}
        users = csv.DictReader(open(path + file))
        for user in map(dict, users):
            user_dict = {}
            user_dict['unit'] = int(user['unit'])
            user_dict['name'] = user['name']
            user_dict['nameFull'] = user['nameFull']
            user_dict['address'] = user['address']
            user_dict['phone'] = user['phone']
            if user['email'] == '':
                user_dict['email'] = None
            else:
                user_dict['email'] = user['email']

            response = requests.post(url, json = user_dict)
            print(response)
