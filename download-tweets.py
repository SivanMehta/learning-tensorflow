from __future__ import absolute_import, print_function
import twitter
import json

# get the credentials
credentials = {}
with open('secrets.json') as json_data:
  credentials = json.load(json_data)

api = twitter.Api(consumer_key=credentials['CONSUMER_KEY'],
                  consumer_secret=credentials['CONSUMER_SECRET'],
                  access_token_key=credentials['ACCESS_TOKEN'],
                  access_token_secret=credentials['ACCESS_TOKEN_SECRET'])

# get the top 10 trends
trends = api.GetTrendsWoeid(woeid=23424977, exclude=None)[:10]
