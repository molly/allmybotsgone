from auth import authenticate
from constants import REPORTED_FILE_PATH
from datetime import datetime
from honeypot import write_honeypot_tweet
from stats import write_stats_tweet
from secrets import *

api = authenticate(API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)


def get_latest_tweet_time():
    latest = api.home_timeline(count=1)
    return latest[0].created_at


def should_send_daily_stats_tweet():
    current_time = datetime.utcnow()
    latest_tweet_time = get_latest_tweet_time()
    return latest_tweet_time.day != current_time.day or (
        latest_tweet_time.hour < 17 <= current_time.hour
    )


def send_tweet(tweet_to_send):
    api.update_status(tweet_to_send)


if __name__ == "__main__":
    should_send_stats = should_send_daily_stats_tweet()

    # This only runs as frequently as it should tweet,
    # so no need to check anything before tweeting
    honeypot_tweet = write_honeypot_tweet()
    send_tweet(honeypot_tweet)

    # Send stats tweet if it's time
    if should_send_stats:
        stats_tweet = write_stats_tweet()
        send_tweet(stats_tweet)
