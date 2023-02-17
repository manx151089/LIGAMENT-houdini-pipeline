#set parms
def setParms(node,initial_attributes={}):
    for parm,val in initial_attributes.items():
        print parm,val
        node.parm(parm).deleteAllKeyframes()
        if ((type(val)==type(0)) or (type(val)==type(0.0))):
            node.parm(parm).set(val)
        if (type(val)==type("abcd")):
            if(val.find('`')!=-1):
                node.parm(parm).set(val)
            if(val.find('`')==-1):
                node.parm(parm).setExpression(val, language=hou.exprLanguage.Hscript)
        node.moveToGoodPosition()

import math
 
def euler_from_quaternion(x, y, z, w):
        """
        Convert a quaternion into euler angles (roll, pitch, yaw)
        roll is rotation around x in radians (counterclockwise)
        pitch is rotation around y in radians (counterclockwise)
        yaw is rotation around z in radians (counterclockwise)
        """
        t0 = +2.0 * (w * x + y * z)
        t1 = +1.0 - 2.0 * (x * x + y * y)
        roll_x = math.degrees(math.atan2(t0, t1))
     
        t2 = +2.0 * (w * y - z * x)
        t2 = +1.0 if t2 > +1.0 else t2
        t2 = -1.0 if t2 < -1.0 else t2
        pitch_y = math.degrees(math.asin(t2))
     
        t3 = +2.0 * (w * z + x * y)
        t4 = +1.0 - 2.0 * (y * y + z * z)
        yaw_z = math.degrees(math.atan2(t3, t4))
     
        return roll_x, pitch_y, yaw_z # in degrees

nodes=hou.selectedNodes()
placeNode=nodes[1]
crowdNode=nodes[0]
points=crowdNode.geometry().points()
#pos=points[0].position()
#print placeNode.children()
nodeType=hou.objNodeTypeCategory()
firstChild=placeNode.children()[0]
if(firstChild.type().name()=='objnet'):
    print 'placement_node : found'
    for pt in points:
        
        pos = pt.position()
        orient = pt.attribValue('orient')
        rot=euler_from_quaternion(orient[0],orient[1],orient[2],orient[3])
        attributesList={
        'agentname':pt.attribValue('agentname'),
        'clipname':pt.stringListAttribValue('clipnames')[0],
        'cliptime':pt.attribValue('clipoffset'),
        'actorid':pt.attribValue('actorId'),
        'costumename':pt.attribValue('costumename')
        }
        print rot,orient
        node=firstChild.createNode('dneg::agentPlacementObj')
        node.parmTuple('t').set(pos)
        node.parmTuple('r').set(rot)
        setParms(node,initial_attributes=attributesList)

        node.moveToGoodPosition()


