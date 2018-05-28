from __future__ import absolute_import, print_function

import twitter
import json
import datetime
import urllib.parse
import re
import concurrent.futures
import time

# get the credentials
credentials = {}
with open('secrets.json') as json_data:
  credentials = json.load(json_data)

api = twitter.Api(
  consumer_key=credentials['CONSUMER_KEY'],
  consumer_secret=credentials['CONSUMER_SECRET'],
  access_token_key=credentials['ACCESS_TOKEN'],
  access_token_secret=credentials['ACCESS_TOKEN_SECRET']
)

# get the top 10 trends
trends = api.GetTrendsWoeid(woeid=23424977, exclude=None)[:10]

trend = trends[0]
now = datetime.date.today()
query = "q={}&result_type=recent&since={}-{}-{}&count=1000".format(
  urllib.parse.quote_plus(trend.name),
  now.year,
  now.month,
  now.day
)

def removeLinks(tweet):
  noLink = re.sub('https?://.*$', "", tweet.text)
  noLink = re.sub('\n', "", noLink)
  tweet.text = noLink
  return tweet

tweets = api.GetSearch(raw_query=query)
tweets = map(removeLinks, tweets)

def getMetaData(tweet):
  return (tweet.text, tweet.favorite_count)

with concurrent.futures.ThreadPoolExecutor(max_workers = 5) as executor:
  future_to_tweet = { executor.submit(getMetaData, t): t for t in tweets }
  enriched = []

  for future in concurrent.futures.as_completed(future_to_tweet):
    tweet = future_to_tweet[future]
    try:
        data = future.result()
    except Exception as exc:
        print('%r generated an exception: %s' % (tweet, exc))
    else:
        enriched.append(data)

  print("text,likes")
  for tweet in enriched:
    print("%s,%d" % (tweet[0], tweet[1]))