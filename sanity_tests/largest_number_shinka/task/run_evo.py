#!/usr/bin/env python3
import argparse
import yaml

from shinka.core import ShinkaEvolveRunner, EvolutionConfig
from shinka.database import DatabaseConfig
from shinka.launch import LocalJobConfig


search_task_sys_msg = """
You are solving a very simple optimisation task.

The program must define a function called run_task().
The goal is to return the largest possible finite number.
The score is exactly the number returned by run_task().
The initial program returns 0.

Keep the program valid Python.
Do not change the required function name: run_task.
"""


def main(config_path: str):
    with open(config_path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    config["evo_config"]["task_sys_msg"] = search_task_sys_msg

    evo_config = EvolutionConfig(**config["evo_config"])
    job_config = LocalJobConfig(
        eval_program_path="evaluate.py",
        time="00:02:00",
    )
    db_config = DatabaseConfig(**config["db_config"])

    runner = ShinkaEvolveRunner(
        evo_config=evo_config,
        job_config=job_config,
        db_config=db_config,
        max_evaluation_jobs=config.get("max_evaluation_jobs"),
        max_proposal_jobs=config.get("max_proposal_jobs"),
        max_db_workers=config.get("max_db_workers"),
        debug=False,
        verbose=True,
    )
    runner.run()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config_path", type=str, default="local_number_100.yaml")
    args = parser.parse_args()
    main(args.config_path)
