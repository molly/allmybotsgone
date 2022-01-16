import os
import tweepy


def authenticate():
    auth = tweepy.OAuthHandler(
        os.environ.get("API_KEY"), os.environ.get("API_KEY_SECRET")
    )
    auth.set_access_token(
        os.environ.get("ACCESS_TOKEN"), os.environ.get("ACCESS_TOKEN_SECRET")
    )
    return tweepy.API(auth)
