import os 
import hou
import platform
def setShowHou(studioProdDir = 'D:/prod/'):
    """
    This will let the user set the show. If it doesnt exist it will ask
    you if you want to create a folder.

    Args:

        studioProdDir:the Production folder under which one would expect
        shows/jobs/assets.

    Please customise D:/prod/ to your convineance. Please note some HDA's 
    use a string.split() or concatenations. If you run into issues please 
    feel free to contact me at manx151089@gmail.com
    """
    projname = hou.ui.readInput('enter show code')[1]
    #path=(studioProdDir+projname+'/')
    path=(studioProdDir+projname)
    if os.path.exists(path):
        os.environ['JOB'] = path
        os.environ['SHOW'] = path
    else:
        print('Proj:',path,'\ndoes not exist')
        if hou.ui.displayConfirmation("Create folder?", suppress=hou.confirmType.OverwriteFile):
            os.makedirs(path,exist_ok=True)
            if os.path.exists(path):
                os.environ['JOB'] = path
                os.environ['SHOW'] = path
                hou.hscript("set -g SHOW = {}".format(path))
                hou.hscript("set -g JOB = {}".format(path))
            else:
                print('permissionDenied: Could not create Job')
        
    print (os.environ['JOB'],hou.getenv('SHOW'))

def setSeqHou():
    """
    This would let the user set the sequence in the environment.
    Also it would let the user create the sequence folder if it
    does not exist. Feel free to add user permission validations.
    """
    job = hou.getenv('JOB')
    seqsDir = os.path.join(job,'shots')
    print('...',seqsDir,'exists:',os.path.exists(seqsDir))
    if os.path.exists(seqsDir) and len(os.listdir(seqsDir))!=0:
        seqs = os.listdir(seqsDir)
        seqSel=hou.ui.selectFromList(seqs,title='setSequence')
        project = os.path.join(seqsDir,seqs[seqSel[0]])
        if(platform.system()=="Windows"):
            project = project.replace("\\","/")
            
        print('setting SEQ env to',project)
        hou.hscript("set -g SEQ = {}".format(project))
        hou.hscript("set -g SEQNAME = {}".format(seqs[seqSel[0]]))
        

    else:
        print('Seq:',seqsDir,'\ndoes not exist')
        if hou.ui.displayConfirmation("Create folder?", suppress=hou.confirmType.OverwriteFile):
            input_seqname = hou.ui.readInput('input sequence name')
            dir_path = os.path.join(seqsDir,input_seqname[1])
            print(dir_path)
            os.makedirs(dir_path,exist_ok=True)

def setShotHou():
    """
    This would let the user create or set the shot.
    """
    seq = hou.getenv('SEQ')
    shotsDir = seq
    if os.path.exists(shotsDir):
        shots = os.listdir(shotsDir)
        if len(shots)!=0:
            shotSel=hou.ui.selectFromList(shots,title='setShot')
            shot = os.path.join(shotsDir,shots[shotSel[0]])
            if(platform.system()=="Windows"):
                shot = shot.replace("\\","/")
            print(shot)
            hou.hscript("set -g SHOT = {}".format(shot))
            print('set seq to:',hou.getenv('SHOTS'))
            scene = os.path.join(shotsDir,shots[shotSel[0]],'fx','houdini')
            if(platform.system()=="Windows"):
                scene = scene.replace("\\","/")
                print('setting scene to :',scene)
            hou.hscript("set -g SCENE = {}".format(scene))
            hou.hscript("set -g SHOTNAME = {}".format(shots[shotSel[0]]))
        else:
            print('No shots found:',shots)
            if hou.ui.displayConfirmation("Create folder?", suppress=hou.confirmType.OverwriteFile):
                input_shotname = hou.ui.readInput('input shot name')
                dir_path = os.path.join(shotsDir,input_shotname[1])
                print(dir_path)
                os.makedirs(dir_path,exist_ok=True)
    else:
        print('create seq folder please')