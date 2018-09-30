template = '''#!/bin/bash -l
#SBATCH -N {nnodes}
#SBATCH -A {account}
#SBATCH -t {runtime}
#SBATCH -J {jobname}_{nnodes}
#SBATCH -o {jobname}_{nnodes}.o%j
#SBATCH -p regular
#SBATCH -C haswell
'''

launcher = 'srun -N {nnodes} -n $(({npernode}*{nnodes})) {command}'
