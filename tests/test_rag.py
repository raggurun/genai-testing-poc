import pytest # pyright: ignore[reportMissingImports]

from app.agent import run_agent
from evaluation.evaluator import evaluate_grounding


def get_rag_cases(cases):

    return [
        case
        for case in cases
        if case["category"] == "rag"
    ]


def test_rag_benchmark(
    benchmark_cases,
):

    cases = get_rag_cases(
        benchmark_cases
    )

    for case in cases:

        result = run_agent(
            case["prompt"]
        )

        context = result[
            "retrieved_context"
        ]

        assert context is not None

        # Retrieval validation
        assert (
            context["id"]
            == case["expected_document"]
        )

        # Grounding evaluation
        evaluation = evaluate_grounding(
            answer=result["answer"],
            context=context["content"],
            expected_fact=case[
                "expected_fact"
            ],
        )

        assert evaluation.passed, (
            f"{case['id']} failed: "
            f"{evaluation.reason}"
        )