#!/bin/bash

#SBATCH --job-name=sklearn-example
#SBATCH --partition=commons
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --time=00:01:00

# Load Anaconda Python
module load Anaconda3
# Run script
srun python sklearn-example.py
# Teardown environment
module unload Anaconda3
