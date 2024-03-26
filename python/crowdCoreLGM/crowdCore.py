#crowd dopnet
import hou
def makeDopnet():
    nodes = hou.selectedNodes()
    for node in nodes:
        dopnet = node.parent().createNode('dopnet')
        output = dopnet.children()[0]
        crowdsolver = dopnet.createNode('crowdsolver')
        crowdobject = dopnet.createNode('crowdobject')
        crowdsource = dopnet.createNode('popsource')
        merge = dopnet.createNode('merge')
        crowdsolver.setNextInput(crowdobject)
        crowdsolver.setNextInput(crowdsource)
        crowdsolver.setNextInput(merge)
        cs_parms = {
                    'usecontextgeo':2,
                    'emittype':1,
                    'jitterbirthtime':0
                    }
        cs_expr = {
                    'impulseactiveate':'$SF == 1'
                    }
        crowdsource.setParms(cs_parms)
        crowdsource.setParmExpressions(cs_expr)
        dopnet.setInput(0,node)
        output.setInput(0,crowdsolver)
        mynodes = [dopnet,crowdobject,crowdsolver,crowdsource,merge,output]
        for each in mynodes:
            each.moveToGoodPosition()

#createState
def createStateFromFirstPrim():
    sel = hou.selectedNodes()
    for node in sel:
       
        children = [x.name() for x in node.children()]
        childrenTypes = [x.type().name() for x in node.children()]
        
        input = node.input(0)
        clips = input.geometry().prim(0).clipCatalog()
        for clip in clips:
            clipname = clip.name()
            
            
            if clipname not in children:
                sNode = node.createNode('crowdstate::3.0',clipname)
                sParms = {  'statename':clipname, 
                            'clipname':clipname,
                            'cliptype':1
                            }
                sNode.setParms(sParms)
                print(childrenTypes,'crowdsolver::3.0' in childrenTypes)
                if 'crowdsolver::3.0' in childrenTypes:
                    print('crowdsolver found')
                    crowdSolver = [x for x in node.children() if 'crowdsolver' in x.type().name() ][0] 
                    solverInput = crowdSolver.input(2)
                    if 'merge' in solverInput.type().name():
                        print('merge found')
                        merge = solverInput
                        merge.setNextInput(sNode)
                sNode.moveToGoodPosition()


def createStateFromPrimGroups():
    sel = hou.selectedNodes()
    for node in sel:
       
        children = [x.name() for x in node.children()]
        childrenTypes = [x.type().name() for x in node.children()]
        
        input = node.input(0)
        for igroup in input.geometry().primGroups():
            prim = igroup.prims()[0]
            clips = prim.clipCatalog()
            for clip in clips:
                clipname = clip.name()
                if clipname not in children:
                    sNode = node.createNode('crowdstate::3.0',clipname)
                    sParms = {  'statename':clipname, 
                                'clipname':clipname,
                                'cliptype':1
                                }
                    sNode.setParms(sParms)
                    print(childrenTypes,'crowdsolver::3.0' in childrenTypes)
                    if 'crowdsolver::3.0' in childrenTypes:
                        print('crowdsolver found')
                        crowdSolver = [x for x in node.children() if 'crowdsolver' in x.type().name() ][0] 
                        solverInput = crowdSolver.input(2)
                        if 'merge' in solverInput.type().name():
                            print('merge found')
                            merge = solverInput
                            merge.setNextInput(sNode)
                    sNode.moveToGoodPosition()

