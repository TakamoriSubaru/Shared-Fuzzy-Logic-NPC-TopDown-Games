# Shared Fuzzy Logic for Emotional NPC Behavior in Top-Down Games

## Description

This project implements a Shared Fuzzy Logic architecture for emotional NPC behavior in a top-down game environment. The system centralizes fuzzy inference processing across multiple NPC agents to reduce duplicated decision-making structures while maintaining adaptive behavior.

## Authors

* Darryl Arief Tananjaya
* Adriel Kevin Jonathan
* Jocelyn Tania Harjanto

## Requirements

* Python 3.10 or newer
* Pygame
* NumPy
* Pandas
* Matplotlib

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Simulation

Run the main game:

```bash
python main.py
```

Run benchmark experiments:

```bash
python run_experiments.py
```

Generate benchmark graphs:

```bash
python plot_results.py
```

## Project Structure

```text
main.py                  Main game loop
npc.py                   NPC implementation
player.py                Player implementation
world.py                 World management
fuzzy_adaptation.py      Shared fuzzy logic system
performance.py           Performance measurement
run_experiments.py       Automated benchmark testing
plot_results.py          Result visualization
results/                 Experimental datasets
```

## Experimental Data

The experimental results used in the paper are stored in the `results` folder.

Files:

* baseline_results.csv
* adaptive_results.csv

## Research Paper

Paper Title:

Shared Fuzzy Logic for Emotional NPC Behavior in Top-Down Games

The project was developed as part of a game AI research study evaluating centralized fuzzy inference systems for multi-agent NPC environments.
