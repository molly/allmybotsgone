import random
import re

from auth import authenticate
from data import *

api = authenticate()


def hydrate_template(template):
    words_needed = re.findall("{(.*?)}", template)
    chosen_words = {}
    for word in words_needed:
        chosen_words[word] = random.choice(WORDS[word])
    return template.format(**chosen_words)


def random_punct():
    return random.choice([".", "!", "!!", "!!!", "..."])


def write_tweet():
    tweet_template = ""
    if random.random() < 0.8:
        tweet_template += random.choice(PREFIX) + " "
    tweet_template += random.choice(TEMPLATES) + random_punct()
    if random.random() < 0.8:
        tweet_template += " " + random.choice(SUFFIX)
        if not tweet_template.endswith("?"):
            tweet_template += random_punct()
    return hydrate_template(tweet_template)


def send_tweet(tweet_to_send):
    api.update_status(tweet_to_send)


if __name__ == "__main__":
    tweet = write_tweet()
    send_tweet(tweet)
