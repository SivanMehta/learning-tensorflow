from __future__ import absolute_import, print_function
import twitter
import json

credentials = {}
with open('secrets.json') as json_data:
  credentials = json.load(json_data)

print(credentials)