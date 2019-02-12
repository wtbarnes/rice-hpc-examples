#!/bin/bash

#SBATCH --job-name=sunpy-example
#SBATCH --partition=commons
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --time=00:01:00

# Load Anaconda Python
module load Anaconda3
# Load the SunPy environment
source activate sunpy-env
# Run script
srun python sunpy-example.py
# Teardown environment
source deactivate
module unload Anaconda3
