#!/bin/bash
# Launch this job by executing this command on a Stampede2 login node:
# sbatch serial_KNL_normal.slurm
# or Launch the following on idev
# mpirun -np 3 python3 file.py
#
# This script has been adapted from the Stampede2's webpage: https://portal.tacc.utexas.edu/user-guides/stampede2
#---------------------------------------------------------------------

#SBATCH -J frequency     # Job name
#SBATCH -o frequency.o%  # name of std output file
#SBATCH -e frequency.e%  # name of stderr error file
#SBATCH -p normal    # Queue name
#SBATCH -N 1         # Total # of nodes (must be 1 for serial)
#SBATCH -n 40         # Total # of mpi tasks (should be 1 for serial)
#SBATCH -t 00:05:00  # Run time (hh:mm:ss)
#SBATCH --mail-user=myname@myschool.edu
#SBATCH -A TG-DMS190011 # Allocation name (in case more than one)


# Laaunch serial code
ibrun -np 40 python3 get_frequency_mpi.py
#----------------------------------------------------------------------