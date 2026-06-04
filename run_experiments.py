import subprocess
import sys

NUM_RUNS = 100

# gunakan python dari venv yang sedang aktif
PYTHON_EXE = sys.executable

print("Using python:", PYTHON_EXE)

print("Running Baseline experiments...")
for i in range(NUM_RUNS):
    subprocess.run([PYTHON_EXE, "main.py", "--mode", "baseline"])

print("Running Adaptive experiments...")
for i in range(NUM_RUNS):
    subprocess.run([PYTHON_EXE, "main.py", "--mode", "adaptive"])

print("All experiments completed!")