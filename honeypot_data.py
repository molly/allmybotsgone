WORDS = {
    "PLATFORM": [
        "Binance",
        "Coinbase",
        "MetaMask",
        "Trust Wallet",
        "Yoroi",
        "OpenSea",
        "PancakeSwap",
        "Safemoon",
    ],
    "STOLEN_NOUN": [
        "bitcoin",
        "BTC",
        "ETH",
        "ethereum",
        "NFTs",
        "doge",
        "SHIB",
        "BNB",
    ],
    "VERB": ["hacked", "stole", "took"],
    "CREDS": [
        "password",
        "seed phrase",
    ],
}

PREFIX = [
    "help me,",
    "i don't know what to do,",
    "help,",
    "can anybody help me?",
    "what do i do?",
    "help!",
]
SUFFIX = [
    "can anybody help me?",
    "help",
    "i don't know what to do",
    "does anyone know what to do?",
    "please help",
    "i'm going to be bankrupt",
    "this was all my money",
    "help",
]
TEMPLATES = [
    "my {PLATFORM} was hacked",
    "someone {VERB} all my {STOLEN_NOUN}",
    "i lost my {CREDS} to my {PLATFORM} account",
    "i'm locked out of my {PLATFORM} account",
]
