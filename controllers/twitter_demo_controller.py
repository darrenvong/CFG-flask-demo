"""
This controller module consists of functions responsible for
orchestrating the functionalities for the 'File Upload' page on the server-side.

@author: Darren
"""
import os

import tweepy

# Again, these should be in a config file or env vars...
consumer_key = os.environ['twitter_consumer_key']
consumer_secret = os.environ['twitter_consumer_secret']

def request_access_token(session):
    """Requests access token from user."""
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth_url = auth.get_authorization_url()
    session["request_token"] = auth.request_token
    return auth_url

def get_access_token(verifier, session):
    """Retrieves the access token for using the Twitter API under the user's
    account, now that they have given permission for us to make requests
    on their behalf."""
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    try:
        request_token = session["request_token"]
        auth.request_token = request_token

        auth.get_access_token(verifier)
        session["access_token"] = auth.access_token
        session["access_token_secret"] = auth.access_token_secret
    except (tweepy.TweepError, KeyError) as e:
        print(e)
        return "Error :("
    else:
        return "Success!"
