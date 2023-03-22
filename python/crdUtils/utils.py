import copy
import json


def applyParm(node, name, value):
    """
    This function takes in a node, a parameter name, and a value. It sets the value of the specified parameter 
    for the node and presses the button to apply the new value.
    """
    parm = node.parm(name) # get the specified parameter
    parm.set(value) # set the value of the parameter
    parm.pressButton() # press the button to apply the new value
    
def getStringParm(node, name):
    """
    This function takes in a node and a parameter name. It returns the value of the specified parameter as a string.
    """
    return node.parm(name).eval().strip() # get the parameter value and return it as a string
    
    
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
    """
    This will merge two dicts and even recursively merge the input children

    Arguments:
    - d: a dictionary
    - *other_dicts: any number of addition dictionaries to merge
    """
    result = copy.deepcopy(d)
    for other_dict in other_dicts:
        for key, value in other_dict.items():
            if key in result and isinstance(result[key], dict) and isinstance(value, dict):
                value = mergeDicts(result[key], value)
            else:
                value = copy.deepcopy(value)
            result[key] = value
    return result


def formatDictToStr(dataDict):
    """
    Converts a nested dictionary to a string with a specific format.

    Arguments:
    - dataDict: A nested dictionary to convert to a string.

    Returns:
    A string representation of the input dictionary, where each level of the nested dictionary is indented and
    each key-value pair is separated by a comma. The format of the string is tailored to a specific use case.
    """
    dataStr = ''
    for keyL1, valuesL1 in sorted(dataDict.items()):
        dataStr += '{}\n'.format(keyL1)
        for keyL2, valuesL2 in sorted(valuesL1.items()):
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