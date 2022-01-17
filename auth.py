import os
import tweepy


def authenticate(key=None, key_secret=None, at=None, at_secret=None):
    api_key = key or os.environ.get("API_KEY")
    api_key_secret = key_secret or os.environ.get("API_KEY_SECRET")
    access_token = at or os.environ.get("ACCESS_TOKEN")
    access_token_secret = at_secret or os.environ.get("ACCESS_TOKEN_SECRET")

    auth = tweepy.OAuthHandler(api_key, api_key_secret)
    auth.set_access_token(access_token, access_token_secret)
    return tweepy.API(auth)
