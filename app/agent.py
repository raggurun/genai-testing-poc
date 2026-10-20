from app.rag import retrieve
from app.tools import get_balance, block_card


PROMPT_INJECTION_PATTERNS = [
    "ignore previous instructions",
    "ignore all previous instructions",
    "reveal your system prompt",
    "show your system prompt",
    "bypass security",
]


def is_prompt_injection(prompt: str):

    prompt = prompt.lower()

    return any(
        pattern in prompt
        for pattern in PROMPT_INJECTION_PATTERNS
    )


def run_agent(prompt: str):

    prompt_lower = prompt.lower()

    # -------------------------
    # Security
    # -------------------------

    if is_prompt_injection(prompt):

        return {
            "intent": "prompt_injection",
            "answer": (
                "I cannot reveal internal instructions "
                "or bypass security controls."
            ),
            "retrieved_context": None,
            "tool_call": None,
            "tool_result": None,
            "blocked": True,
        }

    # -------------------------
    # Unauthorized data access
    # -------------------------

    if (
        "another customer" in prompt_lower
        or "other customer" in prompt_lower
    ):

        return {
            "intent": "unauthorized_access",
            "answer": (
                "I cannot access another customer's "
                "banking information."
            ),
            "retrieved_context": None,
            "tool_call": None,
            "tool_result": None,
            "blocked": True,
        }

    # -------------------------
    # Balance tool
    # -------------------------

    if (
        "my balance" in prompt_lower
        or "account balance" in prompt_lower
    ):

        tool_call = {
            "name": "get_balance",
            "arguments": {
                "account_id": "ACC001"
            },
        }

        tool_result = get_balance(
            account_id="ACC001"
        )

        return {
            "intent": "get_balance",
            "answer": (
                f"Your account balance is "
                f"INR {tool_result['balance']:,}."
            ),
            "retrieved_context": None,
            "tool_call": tool_call,
            "tool_result": tool_result,
            "blocked": False,
        }

    # -------------------------
    # Block-card tool
    # -------------------------

    if (
        "lost card" in prompt_lower
        or "block my card" in prompt_lower
    ):

        tool_call = {
            "name": "block_card",
            "arguments": {
                "card_id": "CARD001"
            },
        }

        tool_result = block_card(
            card_id="CARD001"
        )

        return {
            "intent": "block_card",
            "answer": (
                "Your card-block request requires "
                "identity verification."
            ),
            "retrieved_context": None,
            "tool_call": tool_call,
            "tool_result": tool_result,
            "blocked": False,
        }

    # -------------------------
    # Out-of-scope
    # -------------------------

    if "train" in prompt_lower:

        return {
            "intent": "out_of_scope",
            "answer": (
                "Train booking is outside my banking "
                "capabilities."
            ),
            "retrieved_context": None,
            "tool_call": None,
            "tool_result": None,
            "blocked": False,
        }

    # -------------------------
    # RAG
    # -------------------------

    document = retrieve(prompt)

    if document:

        return {
            "intent": "banking_information",
            "answer": document["content"],
            "retrieved_context": document,
            "tool_call": None,
            "tool_result": None,
            "blocked": False,
        }

    # -------------------------
    # Unknown
    # -------------------------

    return {
        "intent": "unknown",
        "answer": (
            "I could not find sufficient approved "
            "information to answer that question."
        ),
        "retrieved_context": None,
        "tool_call": None,
        "tool_result": None,
        "blocked": False,
    }