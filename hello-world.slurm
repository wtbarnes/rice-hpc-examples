#!/usr/bin/bash

#SBATCH --job-name=hello-world
#SBATCH --partition=commons
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --time=00:01:00

srun echo "Hello World!"
