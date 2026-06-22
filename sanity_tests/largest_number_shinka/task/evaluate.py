import os
import argparse
import math
from typing import Any, Dict, List

from shinka.core import run_shinka_eval

MAX_VALUE = 100.0


def validate_number(run_output: Any):
    try:
        value = float(run_output)
    except Exception:
        return False, f"Output is not numeric: {run_output!r}"

    if not math.isfinite(value):
        return False, f"Output is not finite: {value}"

    if value < 0 or value > MAX_VALUE:
        return False, f"Output must be between 0 and 100: {value}"

    return True, f"Valid numeric output: {value}"


def get_task_kwargs(run_index: int) -> Dict[str, Any]:
    return {}


def aggregate_number_metrics(results: List[Any], results_dir: str) -> Dict[str, Any]:
    if not results:
        value = 0.0
    else:
        try:
            value = float(results[0])
        except Exception:
            value = 0.0

    if (not math.isfinite(value)) or value < 0 or value > MAX_VALUE:
        value = 0.0

    return {
        "combined_score": value,
        "public": {
            "output_number": value,
            "max_allowed_value": MAX_VALUE,
        },
        "private": {
            "score_definition": "score equals the returned number if it is between 0 and 100; invalid outputs receive 0",
        },
    }


def main(program_path: str, results_dir: str):
    print(f"Evaluating program: {program_path}")
    print(f"Saving results to: {results_dir}")
    os.makedirs(results_dir, exist_ok=True)

    metrics, correct, error_msg = run_shinka_eval(
        program_path=program_path,
        results_dir=results_dir,
        experiment_fn_name="run_task",
        num_runs=1,
        get_experiment_kwargs=get_task_kwargs,
        validate_fn=validate_number,
        aggregate_metrics_fn=lambda r: aggregate_number_metrics(r, results_dir),
    )

    if correct:
        print("Evaluation completed successfully.")
    else:
        print(f"Evaluation failed: {error_msg}")

    print("Metrics:")
    for key, value in metrics.items():
        print(f"  {key}: {value}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--program_path", type=str, default="initial.py")
    parser.add_argument("--results_dir", type=str, default="results")
    args = parser.parse_args()
    main(args.program_path, args.results_dir)
