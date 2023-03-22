import copy
import json


def applyParm(node, name, value):
    parm = node.parm(name)
    parm.set(value)
    parm.pressButton()
    
    
def getStringParm(node, name):
    return node.parm(name).eval().strip()
    
    
def buildMenuItems(items):
    """
    Utility method to return a sequence of items in the format expected by menus (value, label). 
    """
    menuItems = []
    for item in items:
        item = str(item) if item else ' '
        menuItems.extend((item, item))
    return menuItems
    

def refreshParmMenu(node, parmName, default = None):
    """
    Utility method to trigger the menu creation script on a menu parm.
    """
    
    # Get the parm.
    parm = node.parm(parmName)
    
    # Get the current value so we can check if we need to reset it.
    # This will also trigger the menu script.
    value = parm.eval().strip()
    
    # Reset current value to the first in the list.
    if default is not None:
        parm.set(default)
    else:
        menuItems = parm.menuItems()
        if menuItems and value not in menuItems:
            parm.set(menuItems[0])
        
    parm.pressButton()


def mergeDicts(d, *other_dicts):
    result = copy.deepcopy(d)
    for other_dict in other_dicts:
        for key, value in other_dict.iteritems():
            if key in result and isinstance(result[key], dict) and isinstance(value, dict):
                value = mergeDicts(result[key], value)
            else:
                value = copy.deepcopy(value)
            result[key] = value
    return result


def formatDictToStr(dataDict):
    dataStr = ''
    for keyL1, valuesL1 in sorted(dataDict.iteritems()):
        dataStr += '{}\n'.format(keyL1)
        for keyL2, valuesL2 in sorted(valuesL1.iteritems()):
            dataStr += '\t{}\n\t\t'.format(keyL2)
            count = 0
            for keyL3 in sorted(valuesL2.keys()):
                if count == 4:
                    dataStr += '\n\t\t'
                    count = 0
                dataStr += '{}, '.format(keyL3)
                count += 1
            dataStr = dataStr[:-2] # remove last ', '
            dataStr += '\n'
    return dataStr