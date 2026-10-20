class EvaluationResult:

    def __init__(
        self,
        passed: bool,
        score: float,
        reason: str,
    ):
        self.passed = passed
        self.score = score
        self.reason = reason

    def __repr__(self):

        return (
            f"EvaluationResult("
            f"passed={self.passed}, "
            f"score={self.score}, "
            f"reason='{self.reason}')"
        )


def evaluate_grounding(
    answer: str,
    context: str,
    expected_fact: str,
):

    if expected_fact not in context:

        return EvaluationResult(
            passed=False,
            score=0,
            reason=(
                "Retrieval failure: expected fact "
                "was not present in context"
            ),
        )

    if expected_fact not in answer:

        return EvaluationResult(
            passed=False,
            score=0,
            reason=(
                "Generation failure: correct context "
                "was retrieved but answer did not "
                "contain expected fact"
            ),
        )

    return EvaluationResult(
        passed=True,
        score=1.0,
        reason="Answer is grounded in retrieved context",
    )


def evaluate_tool(
    actual_tool: str,
    expected_tool: str,
):

    if actual_tool != expected_tool:

        return EvaluationResult(
            passed=False,
            score=0,
            reason=(
                f"Expected tool '{expected_tool}' "
                f"but received '{actual_tool}'"
            ),
        )

    return EvaluationResult(
        passed=True,
        score=1.0,
        reason="Correct tool selected",
    )