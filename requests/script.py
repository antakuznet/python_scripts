#!/usr/bin/env python3

import os
import requests
import json

path = '/'
url = 'http://'

files = os.listdir(path)

for file in files:
    if file.endswith('.txt'):
        print(file)
        review_dict = {}
        with open(file, 'r') as review:
            review_dict["title"] = review.readline().strip()
            review_dict["name"] = review.readline().strip()
            review_dict["date"] = review.readline().strip()
            review_dict["feedback"] = review.readline().strip()
        json_app = json.dumps(review_dict)
        response = requests.post(url, data = json_app)
        print(response)
