import json
import random
from time import time
from auth import authenticate
from constants import REPORTED_FILE_PATH

api = authenticate()

EMOJIS = "😀😃😄😁😅☺️😊🙂😉😌😏🥴🤠😈👋🤙🖕🦸💃💅‍🌻⭐️✨🌟💥🔥🌈☀️🤸🚀💣🧹🎉🎊❤️💕💞💖️"


def pick_emojis():
    """Return a random selection of 1–3 emojis"""
    selection = random.sample(EMOJIS, random.randint(1, 3))
    return " ".join(selection)


def write_and_send_stats_tweet():
    reported = None
    with open(REPORTED_FILE_PATH, "r") as reported_file:
        reported = json.load(reported_file)

    if reported:
        current_time = time()
        count = reported["count"]
        if (
            "last_tweeted_stats" not in reported
            or current_time - reported["last_tweeted_stats"] > 86400
        ) and count > 0:
            tweet = "So far I've reported {} spambots!\n{}".format(count, pick_emojis())
            api.update_status(tweet)
            reported["last_tweeted_stats"] = current_time

            with open(REPORTED_FILE_PATH, "w") as reported_file:
                json.dump(reported, reported_file)
