import os
import re

def prepareName(text):
    name = re.sub('^OUT_','',text)
    name = "IN-{}-01".format(name)
    
    return name

mpos = hou.selectedNodes()[0].position()
for n in hou.selectedNodes():
    nodeName = n.name()
    
    pos = n.position()
    
    new_name = prepareName(nodeName)
    #print(new_name)
    
    objMerge = hou.node(os.path.dirname(n.path())).createNode("object_merge", new_name)
    
    #objMerge.setName("IN-" + nodeName + "-01", True)
    objMerge.move(hou.Vector2(mpos[0],mpos[1]-1))
    #objMerge.moveToGoodPosition()
    objMerge.setParms({"objpath1":"`opfullpath(\"..\")+\"/\"+split(opname(\".\"),\"-\",1)`"})
    objMerge.setCurrent(True, clear_all_selected=True)
    