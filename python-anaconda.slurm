#!/bin/bash

#SBATCH --job-name=sklearn-example
#SBATCH --partition=commons
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --time=00:01:00

module load Anaconda3  # Load Anaconda Python
srun python sklearn-example.py
module unload Anaconda3
