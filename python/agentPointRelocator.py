
import hou
import crowdstoolutils
import fnmatch
def createVisualizer():
    node = hou.pwd()
    position = node.position()
    path = node.path()+'/OUT_guides'
    objName='Visualizer_'+node.name()
    visualizer = node.parent().createNode('object_merge',node_name=objName)
    visualizer.setPosition(position+hou.Vector2(2,0))
    visualizer.parm('objpath1').set(path)
    
def getGroup(node):
    geo = hou.node(node.path()+'/isolateKeeperGroup').geometry()
    
    return geo.prim(0)
def getJts():
    import crowdstoolutils
    return crowdstoolutils.selectJoint(kwargs['node'], kwargs['parmtuple'])
    
def checkTerrain():
    node = hou.pwd()
    if (node.parm('terrainProject').eval()==1):      
        if node.input(1) is None:
            return 1
        else:
            return 0
    else:
        return 0
        
def wildCardTransformNames(node):
    hda = node.parent()
    mystring = ""
    if hda.parm('method').eval() == 3:
        mystring = 'rootJNT'
    else:    
        for each in range(hda.parm('limbs').eval()):
            jtStr = hda.parm('joint_'+str(each+1))
            if "*" in jtStr.eval():
                jts = jtStr.eval().split(" ")
                for jt in jts:
                    if "*" in jt:
                        grp = hda.parm('group')
                        if grp.eval() is "":
                            ptnum = 0
                            #transformNames = node.input(0).geometry().prim(ptnum).rig().transformNames()
                            #transformNames only works in 19.0+
                            transformNames = list(dict.fromkeys(crowdstoolutils.buildTransformMenu(node)))#list dict from keys deletes the duplicates in array
                            for transformName in transformNames:
                                #patternMatch = hou.text.patternMatch(jt,transformName)
                                patternMatch = hou.patternMatch(jt,transformName)
                                if patternMatch:
                                    mystring += transformName+' '
                                #hou.text.patternMatch doesnt work in 18.0
                                if jt in transformName:
                                    mystring += transformName + ' '
                        else:
                            grpName = grp.eval()
                            ptnum = node.geometry().findPointGroup(grpName).points()[0].number()
                            #transformNames = node.input(0).geometry().prim(ptnum).rig().transformNames()
                            #transformNames only works in 19.0+
                            transformNames = list(dict.fromkeys(crowdstoolutils.buildTransformMenu(node)))#list dict from keys deletes the duplicates in array
                            for transformName in transformNames:
                                #patternMatch = hou.text.patternMatch(jt,transformName)
                                patternMatch = hou.patternMatch(jt,transformName)
                                if patternMatch:
                                    mystring += transformName + ' '
                    else:
                        mystring+=jt+" "
            else:        
                mystring+=jtStr.eval()+" "
    return mystring


    