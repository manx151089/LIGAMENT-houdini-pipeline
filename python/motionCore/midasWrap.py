import os
import subprocess
import MiDaS as midas
verbose = 0
mBase = midas.__path__._path[0]
mBase = '/'.join(mBase.split('\\'))
modelType = 'dpt_beit_base_384'
run = 'python {0}/run.py --model_weights {0}\weights\{1}.pt --model_type {1}'.format(mBase,modelType)
log = subprocess.check_output(run)
if verbose is 1:
    print(log)