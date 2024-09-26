import hou
import os

def agentDefinitionFromFbx(fbxpath):
    out = hou.node('/out')
    ag = out.createNode('agent')
    ag.parm('source').set(2)
    ag.parm('fbxfile').set(fbxpath)
    ag.parm('cachedir').set(os.path.dirname(fbxpath))
    ag.parm('execute').pressButton()
