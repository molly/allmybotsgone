import os


__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
REPORTED_FILE_PATH = os.path.join(__location__, "reported.json")

BOT_ID = 1482758757247553540
ALLOWLISTED_USER_IDS = {BOT_ID, 545445165, 1477342011875381251}
