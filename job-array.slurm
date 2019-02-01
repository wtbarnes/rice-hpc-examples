#!/usr/bin/bash

#SBATCH --partition=commons
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --job-name=job-array-example
#SBATCH --time=00:00:30

array = (1 2 3 4 5)

echo "This is job number "$SLURM_ARRAY_TASK_ID
echo "The value of the array is "array[$SLURM_ARRAY_TASK_ID]
