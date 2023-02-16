class parmUtils():
    
    def setParms(node,initial_attributes={}):
        for parm,val in initial_attributes.items():
            node.parm(parm).deleteAllKeyframes()
            if ((type(val)==type(0)) or (type(val)==type(0.0))):
                node.parm(parm).set(val)
            if (type(val)==type("abcd")):
                if(val.find('`')!=-1):
                    node.parm(parm).set(val)
                if(val.find('`')==-1):
                    node.parm(parm).setExpression(val, language=hou.exprLanguage.Hscript)
            node.moveToGoodPosition()