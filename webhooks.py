import base64
import hashlib
import hmac
import os
from flask import Flask, request, json


app = Flask(__name__)


def is_valid(signature, request_body):
    # Check the signature to ensure this request came from Twitter
    sha256_hash_digest = hmac.new(
        bytes(os.environ.get("API_KEY"), "utf-8"),
        msg=bytes(request_body, "utf-8"),
        digestmod=hashlib.sha256,
    ).digest()
    hash_val = "sha256=" + base64.b64encode(sha256_hash_digest).decode("utf-8")
    return hmac.compare_digest(signature, hash_val)


@app.route("/", methods=["GET"])
def webhook_challenge():
    if request.args and request.args.get("crc_token"):
        sha256_hash_digest = hmac.new(
            bytes(os.environ.get("API_KEY_SECRET"), "utf-8"),
            msg=bytes(request.args.get("crc_token"), "utf-8"),
            digestmod=hashlib.sha256,
        ).digest()
        response = {
            "response_token": "sha256="
            + base64.b64encode(sha256_hash_digest).decode("utf-8")
        }
        return response
    else:
        return "Nothing to see here but us webhook handlers"


@app.route("/", methods=["POST"])
def handle_webook():
    print("hi")
