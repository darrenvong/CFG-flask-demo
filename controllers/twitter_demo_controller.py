# -*- coding: utf-8 -*-

import sys
import codecs
import os

import tweepy
# "Hacky" workaround replacing the standard output with a UTF-8 encoding writer
# due to console's inability to print emojis...
sys.stdout = codecs.getwriter('utf-8')(sys.stdout)

# Again, these should be in a config file or env vars...
consumer_key = os.environ['twitter_consumer_key']
consumer_secret = os.environ['twitter_consumer_secret']
access_token = os.environ['twitter_access_token']
access_token_secret = os.environ['twitter_access_token_secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

cfg_tweets = api.search(q="CodeFirstGirls")

for tweet in cfg_tweets:
    print tweet.user.name + ": " + tweet.text

raw_input("Type anything to exit...")
