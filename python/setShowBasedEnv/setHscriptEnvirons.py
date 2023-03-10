import os 
import hou
def setShowHou():
    projname = hou.ui.readInput('enter show code')[1]
    
    path=('/media/vis/sg/prod/'+projname+'/')
    if os.path.exists(path):
        os.environ['JOB'] = path
        
    print (os.environ['JOB'])

def setSeqHou():
    job = hou.getenv('JOB')
    seqsDir = os.path.join(job,'shots')
    if os.path.exists(seqsDir):
        seqs = os.listdir(seqsDir)
        seqSel=hou.ui.selectFromList(seqs,title='setSequence')
        project = os.path.join(seqsDir,seqs[seqSel[0]])
        hou.hscript("set -g SEQ = {}".format(project))
        print('set seq to:',hou.getenv('SEQ'))

def setShotHou():
    import hou
    import os
    seq = hou.getenv('SEQ')
    shotsDir = seq
    if os.path.exists(shotsDir):
        shots = os.listdir(shotsDir)
        shotSel=hou.ui.selectFromList(shots,title='setShot')
        project = os.path.join(shotsDir,shots[shotSel[0]])
        print(project)
        hou.hscript("set -g SHOT = {}".format(project))
        print('set seq to:',hou.getenv('SHOTS'))
        scene = os.path.join(shotsDir,shots[shotSel[0]],'fx','houdini')
        hou.hscript("set -g SCENE = {}".format(scene))