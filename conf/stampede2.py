template = '''#!/bin/bash
#SBATCH -N {nnodes}
#SBATCH --ntasks-per-node={npernode}
#SBATCH -A {account}
#SBATCH -t {runtime}
#SBATCH -J {jobname}_{nnodes}
#SBATCH -o {jobname}_{nnodes}.o%j
#SBATCH -p skx-normal
'''

launcher = 'mpirun -n $(({nnodes}*{npernode})) --npernode {npernode} {command}'
