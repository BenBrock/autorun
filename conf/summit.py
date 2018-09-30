template = '''#!/bin/bash
# Begin LSF directives
#BSUB -P {account}
#BSUB -J {jobname}_{nnodes}
#BSUB -o {jobname}_{nnodes}.o%J
#BSUB -W {runtime}
#BSUB -nnodes {nnodes}
# End LSF directives and begin shell commands
cd $LS_SUBCWD

'''

launcher = 'jsrun -n {nnodes} -c ALL_CPUS -a {npernode} {command}'
