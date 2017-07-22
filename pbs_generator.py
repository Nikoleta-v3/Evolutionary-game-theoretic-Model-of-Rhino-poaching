submit_script = ""
for number_steps, tol, epsilon, step in [(3, 0.0001, 0.001, 0.0001),
                                         (4, 0.0001, 0.001, 0.0001),
                                         (5, 0.0001, 0.001, 0.0001),
                                         (6, 0.0001, 0.001, 0.0001),
                                         (7, 0.0001, 0.001, 0.0001),
                                         (8, 0.0001, 0.001, 0.0001),
                                         (9, 0.0001, 0.001, 0.0001),
                                         (10, 0.0001, 0.001, 0.0001)]:

    pbs_file = """#!/bin/bash
#PBS -q workq
#PBS -N step{}
#PBS -P PR350
#PBS -o rhino{}out.txt
#PBS -e rhino{}err.txt
#PBS -l select=1:ncpus=16:mpiprocs=16
#PBS -l place=scatter:excl
#PBS -l walltime=70:00:00
export MPLBACKEND="agg"
# Run std
cd /scratch/$USER/Evolutionary-game-theoretic-Model-of-Rhino-poaching/
/home/$USER/anaconda3/envs/rhino/bin/python parameter_sweep.py {} {} {} {}
""".format(number_steps, number_steps, number_steps, number_steps, tol, epsilon, step)

    with open("pbs/{}.pbs".format(number_steps), 'w') as f:
        f.write(pbs_file)

    submit_script += "qsub pbs/{}.pbs \n".format(number_steps)

with open("submit_meta_workers.sh", 'w') as f:
    f.write(submit_script)
