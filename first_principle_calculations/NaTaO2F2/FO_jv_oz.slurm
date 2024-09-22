#!/bin/bash -l

################### VASP Job Batch Script (O. Zakary, 2022) ###################
# Section for defining queue-system variables:
#-------------------------------------
# This script asks for a given set of nodes and cores. IMMM cluster has got
# 6 nodes (4 with GPU and 2 without GPU), this script use the machine GTO (GPU node with 2 CPU).
# Runtime for this job is 14 days (can be modified); syntax is jj-hh:mm:ss.
# Memory is set to the half maximum amound adviced when asking for a full node, it
# adds up to 192 000MB, leaving a small part for the system to use. Memory
# can be specified per core, virtual or total pr job (be carefull!!!).
# Remark!!! : This script need to be modified and adapted to each calculation
#-------------------------------------
# SLURM-section
#SBATCH --job-name=FO
#SBATCH --nodes=1
#SBATCH --ntasks=8
#SBATCH --time=00-00:00:00
##SBATCH --mem-per-cpu=1500MB
#SBATCH --constraint="cascadelake"
#SBATCH --output=FO_vasp_run.log
#SBATCH --mail-type=FAIL 
#SBATCH --mail-type=END
#SBATCH --mail-user=zakary_o
#SBATCH --distribution=cyclic
#SBATCH --export=ALL
#SBATCH --exclude=voyager
#SBATCH --partition=cluster

######################################
# Section for defining job variables and settings:

# When you use this test script, make sure, your folder structure is as follows:
# ./FO_jv_oz.slurm
# ./FO/INPUT_files/INCAR
# ./FO/INPUT_files/KPOINTS
# ./FO/INPUT_files/POTCAR
# ./FO/INPUT_files/POSCAR

proj=FO # Name of job folder (!!to be changed when running calculation on another folder!!)
input=$(ls ${proj}/INPUT_files/{INCAR,KPOINTS,POTCAR,POSCAR}) # Input files from job folder

# We load all the default program system settings with module load:

module purge
module load vasp/6.2.1-gcc-10.2 # vasp support GCC
# You may check other available versions with "module avail vasp"

# Now we create working directory and temporary scratch for the job(s):
# Necessary variables are defined in the notur and the software modules.

export VASP_WORKDIR=/data/$USER/$SLURM_JOB_ID.OUT

mkdir -p $VASP_WORKDIR

# Preparing and moving inputfiles to tmp:

submitdir=$SLURM_SUBMIT_DIR

cp $input $VASP_WORKDIR
cd $VASP_WORKDIR

######################################
# Section for running the program and cleaning up:

# Running the program:
time mpirun vasp_std 
# multiple k-points, other options can be used by replacing 'vasp_std' with
# 'vasp_gam' (gamma-point only), 'vasp_ncl' (noncollinear spins) etc.

# Cleaning up and moving files back to /export/home/immm/ozakary/Jobs/NbOF3:
# Make sure to move all essential files specific for the given job/software.
mv $VASP_WORKDIR $submitdir/$proj/OUTPUT_files

# To copy other output files : cp CHGCAR $submitdir/${proj}.CHGCAR
# To zip some of the output might be a good idea!
#gzip results.gz OUTCAR
#mv $results.gz $submitdir/

# Investigate potentially other files to keep:
echo $(pwd)
echo $(ls -ltr)

# ALWAYS clean up after yourself. Please do uncomment the following line
# If we have to, we get really grumpy!
cd $submitdir
rm -r $VASP_WORKDIR/*

echo "Job finished at"
date
################### Job VASP ended ###################
exit 0
