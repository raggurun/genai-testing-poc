import json
from pathlib import Path

import pytest  # pyright: ignore[reportMissingImports]


@pytest.fixture(scope="session")
def benchmark_cases():

    path = (
        Path(__file__).parent.parent
        / "data"
        / "benchmark.json"
    )

    with open(
        path,
        encoding="utf-8",
    ) as file:

        return json.load(file)