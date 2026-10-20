from app.agent import run_agent
from evaluation.evaluator import evaluate_tool


def test_balance_tool():

    result = run_agent(
        "What is my account balance?"
    )

    assert result["intent"] == "get_balance"

    assert result["tool_call"] is not None

    evaluation = evaluate_tool(
        actual_tool=result["tool_call"]["name"],
        expected_tool="get_balance",
    )

    assert evaluation.passed


def test_balance_arguments():

    result = run_agent(
        "What is my account balance?"
    )

    assert (
        result["tool_call"]
        ["arguments"]
        ["account_id"]
        == "ACC001"
    )


def test_balance_grounding():

    result = run_agent(
        "What is my account balance?"
    )

    backend_balance = result[
        "tool_result"
    ]["balance"]

    expected_text = (
        f"{backend_balance:,}"
    )

    assert (
        expected_text
        in result["answer"]
    )


def test_block_card_tool():

    result = run_agent(
        "I lost my card. "
        "Please block my card."
    )

    assert result["intent"] == "block_card"

    assert (
        result["tool_call"]["name"]
        == "block_card"
    )

    assert (
        result["tool_result"]["status"]
        == "pending_verification"
    )


def test_agent_does_not_claim_false_success():

    result = run_agent(
        "I lost my card. "
        "Please block my card."
    )

    assert (
        "successfully blocked"
        not in result["answer"].lower()
    )