import random
import requests

EMOJIS = "πππππβΊοΈππππππ₯΄π€ πππ€ππ¦Έππβπ»β­οΈβ¨ππ₯π₯πβοΈπ€Έππ£π§Ήππβ€οΈππποΈ"


def pick_emojis():
    """Return a random selection of 1β3 emojis"""
    selection = random.sample(EMOJIS, random.randint(1, 3))
    return " ".join(selection)


def write_stats_tweet():
    resp = requests.get("https://allmybotsgone.herokuapp.com/stats")
    resp_json = resp.json()
    count = int(resp_json["reported"])
    return "So far I've reported {} spambots!\n{}".format(count, pick_emojis())
