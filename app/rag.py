KNOWLEDGE_BASE = [
    {
        "id": "DOC001",
        "topic": "gold_account",
        "content": (
            "Gold Account requires a minimum "
            "balance of INR 10,000."
        ),
    },
    {
        "id": "DOC002",
        "topic": "silver_account",
        "content": (
            "Silver Account requires a minimum "
            "balance of INR 5,000."
        ),
    },
    {
        "id": "DOC003",
        "topic": "atm",
        "content": (
            "The daily ATM withdrawal limit "
            "is INR 50,000."
        ),
    },
]


def retrieve(question: str):

    question = question.lower()

    if "gold" in question:
        return KNOWLEDGE_BASE[0]

    if "silver" in question:
        return KNOWLEDGE_BASE[1]

    if "atm" in question:
        return KNOWLEDGE_BASE[2]

    return None