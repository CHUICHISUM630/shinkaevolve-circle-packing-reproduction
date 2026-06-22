from pathlib import Path
import yaml

p = Path("local_100.yaml")
cfg = yaml.safe_load(p.read_text(encoding="utf-8"))

cfg["evo_config"]["num_generations"] = 101
cfg["evo_config"]["results_dir"] = "results/results_circle_local_100"

p.write_text(yaml.safe_dump(cfg, sort_keys=False, allow_unicode=True), encoding="utf-8")

print("num_generations:", cfg["evo_config"]["num_generations"])
print("results_dir:", cfg["evo_config"]["results_dir"])
