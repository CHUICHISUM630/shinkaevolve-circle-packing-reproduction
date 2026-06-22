# ShinkaEvolve Circle Packing Local Reproduction

This repository contains my local ShinkaEvolve experiment for the 26-circle packing task.

## Experiment setup

- Method: ShinkaEvolve
- Task: 26-circle packing
- Model: qwen2.5-coder:7b via Ollama
- Endpoint: http://localhost:11434/v1
- Budget: 100 generated proposals
- Main config: configs/local_100.yaml

## Repository structure

- configs/: experiment configuration files
- task/: initial program, evaluator, and run script
- raw_results/: raw ShinkaEvolve output files
- logs/: terminal logs and PowerShell command history
- results/: processed CSV files and figures, if available

## How to run

From the original ShinkaEvolve circle_packing example folder, run:

python run_evo.py local_100.yaml

## Result summary

In this local run, ShinkaEvolve completed 100 generated proposals. The initial program remained the best program, with a score of 0.959764. All 100 generated candidate programs were evaluated as incorrect, so no generated candidate improved over the baseline.

This result is different from the original ShinkaEvolve paper, but it is meaningful as a constrained local reproduction using a single local 7B model and a simplified setup.

## Largest-number sanity test

I also added a simple sanity-check task requested after the circle-packing experiment.

Task: the initial program returns 0, and the objective is to return the largest number between 0 and 100. The score is exactly the returned number, as long as it is within this range.

Command lines used:

From examples/largest_number_shinka:

Smoke test:
python run_evo.py --config_path local_number_smoke.yaml

Formal 100-proposal run:
python run_evo.py --config_path local_number_100.yaml

The 100-proposal ShinkaEvolve run completed successfully:
- Target generations: 101
- Total proposals generated: 100
- Best score: 100.00
- Correct programs: 25 / 100
- Runtime: 613.34 seconds
- Average time per proposal: 6.13 seconds

The files for this sanity test are stored in:
sanity_tests/largest_number_shinka/

