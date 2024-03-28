import glob
import os
import datetime
from pathlib import Path

def getProjectEntity():
    import lgmHoudiniCore.solarisUtils as solarisUtils
    return solarisUtils.getProject()
    
def timeFromPath(path):
    time = datetime.datetime.fromtimestamp(os.path.getmtime(path)).strftime('%Y-%m-%d %H:%M:%S')
    return time

class animationBrowser:
    def getAnimFromLGMReference(node):
        """
        This creates sublayers when you have a LGM reference when you give it a node
        node : an instance of hou.Node which is a LGMReference in the type().name()
        """
        parent = node.parent()
        if 'lgmReference' in node.type().name():    
            shotName = node.parm('shotList').eval()
            seqName = node.parm('sequenceList').eval()
            project = getProjectEntity()
            shot = project.getAsset(shotName)
            tasks = shot.getTasks()
            task = [ x.getName() for x in tasks if 'anim' in x.getName().lower() ]
            #animOutputs = shot.getTask('Anim').getLatestOutputs(includeOmit=False,refresh=True)
            print('taskName:',task)
            animOutputs = shot.getTask(task[0]).getLatestOutputs(includeOmit=False,refresh=True)
            paths = [ x.filePath for x in animOutputs if 'USD' in x.getName() ]
            #pathsDate = [ timeFromPath(x) for x in paths ]
            anims = [ str(x.getName()) for x in animOutputs if 'USD' in x.getName() ]
            animTree = [ str(x.getName())+'\t'+str(timeFromPath(str(x.filePath)))+'    ' for x in animOutputs if 'USD' in x.getName() ]
            print(anims)
            aT = hou.ui.selectFromTree(animTree)
            if len(aT) is not 0:
                for animSel in aT:
                    idx = animTree.index(animSel)
                    anim = anims[idx]
                    path = paths[idx]
                    print(anim,path)
                    slAnim = parent.createNode('sublayer','sublayerAnim_'+anim+'01')
                    parms = {
                                'filepath1' : path,
                                'setstagemetadata' : 'yes'
                            }
                    slAnim.setParms(parms)
                    slAnim.setInput(0,node)
                    slAnim.moveToGoodPosition()
                    

            
    def getClipsFromLopnet(node,clipNode):
        """
        This fills in clips from the source node lopnet and target clipNode
        node: A lopnet with anim clips
        clipNode: An agent clip node
        """
        if 'lopnet' in node.type().name():
            children = node.children()
            #clipNode = hou.selectedNodes()[1]
            
            animsSL = [ x for x in children if 'sublayerAnim' in x.name() ] 
            anims = [x.name() for x in animsSL]
            aT = hou.ui.selectFromTree(anims)
            for anim in aT:
                idx = anims.index(anim)
                lopnode = animsSL[idx]
                parent = node.parent()
                if 'agentclip' in clipNode.type().name():
                    
                    noOfClips = clipNode.parm('clips')
                    noOfClips.insertMultiParmInstance(noOfClips.eval())
                    cId = str(noOfClips.eval())
                    aName = anim.split('_')[-1].split('AnimUSD')[0]
                    #charName = '/'+'charAnansiBird'
                    lsr_SkelRoots = lopnode.selectionRule(pattern = '{ usd_istype(0,@primpath,"SkelRoot") }')
                    eps = lsr_SkelRoots.expandedPaths() 
                    skelRoots = [ x.pathString for x in eps if '/assets/' not in x.pathString ] 
                    if(len(skelRoots) == 0):
                        hou.ui.displayMessage('no skelroot found on clip:',clip)
                    skelRoot = skelRoots[0]
                    print(aName,'added to:',clipNode, ' with skelroot:',clipNode.name())
                    parms = { 
                                'name'+cId:aName,
                                'source'+cId:4,
                                'loppath'+cId:clipNode.relativePathTo(lopnode),
                                'primpattern'+cId:skelRoot,
                                'converttoinplace'+cId:1 
                            }
                    clipNode.setParms(parms)
                    
sel = hou.selectedNodes()
node = sel[0]
if 'lgmReference' in node.type().name():
    animationBrowser.getAnimFromlgmReference(node)
    
if 'lopnet' in node.type().name():
    animationBrowser.getClipsFromLopnet(node,sel[1])