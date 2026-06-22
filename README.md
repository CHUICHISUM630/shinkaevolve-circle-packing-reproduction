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
