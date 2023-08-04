import os
import sys
import inspect
import hou

print('pythonrc.py is triggered')
tool_root = os.path.dirname(inspect.getfile(inspect.currentframe()).replace('\\','/').replace('python2.7libs/pythonrc.py',''))
python_root = '%s/python' % tool_root

if python_root not in sys.path:
    sys.path.append(python_root)
    sys.path.append('C:/python37/Lib/site-packages')

#print ('>>>',tool_root,'>>>>>',os.path.dirname(inspect.getfile(inspect.currentframe())))
#hou.putenv('RANDOM_VARIABLE_NAME','I Love houdini')
#os.environ['JOB'] = someJobPath
#hou.putenv("JOB",os.environ['JOB'])

