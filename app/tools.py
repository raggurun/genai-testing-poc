def get_balance(account_id: str):

    return {
        "status": "success",
        "account_id": account_id,
        "currency": "INR",
        "balance": 25000,
    }


def block_card(card_id: str):

    return {
        "status": "pending_verification",
        "card_id": card_id,
    }


def transfer_money(
    source_account: str,
    destination_account: str,
    amount: float,
):

    return {
        "status": "success",
        "source_account": source_account,
        "destination_account": destination_account,
        "amount": amount,
    }