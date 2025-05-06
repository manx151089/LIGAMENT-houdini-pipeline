import hou
import os
from lgmfxShotApi import lsa
import glob

def __init__():
    pass

def load_usd_files_from_departments(shotname,show,pub_directory="usd"):
    '''
    Scans the specified base directory for department subfolders, checks for 
    the presence of "geometry.usd" files in each department folder, and loads
    them into the LOP stage in Houdini. If any USD file is missing, a message
    is displayed for the user.The root directory where department folders (fx,
    animation, crowd, layout, etc.) are stored. Each department folder should
    contain a "geometry.usd" file.

    Usage:
        
        load_usd_files_from_departments(shotname,show,pub_directory="usd")

    Args: 
        
        shotname (str): folder name of the shot
        
        show (str path): path of the show
    
    Returns:
        
        None

    TO-DO:
        
        Need to deprecate this an split the function into follows.
        
        update_multiparm_with_latest_versions()
        
        load_usd_files_from_multiparm()
    '''
    
    dept_paths,departments = lsa.lsa.list_depts_from_shot(shotname)    
    usd_files_to_load = [lsa.lsa.get_versions_from_dept(dept_path,list_all_versions=False) for dept_path in dept_paths]
    stage = hou.pwd().editableStage()
    
    for usd_file in usd_files_to_load:
        if os.path.exists(usd_file):
            root = stage.GetEditTarget().GetLayer()
            layer = root.subLayerPaths.append(usd_file)
        else:
            print(f"USD file not found: {usd_file}")
    
def get_dict_with_versions(shotname,get_latest_version=False):
    """
    Uses the lsa (LGMFX Shot Api) to concatenate all the versions and returns
    a list of departments and a dictionary of all versions.

    Usage:

        get_dict_with_versions(shotname,get_latest_version=False)

    Args:

        shotname (str. path) : the directory to the shot

        get_latest_version (bool.) : If set to True this will return a list of latest versions
        instead of a dictionary of all versions. Default is False.

    Returns: 

        [[departments] {int version_number:str version_path}] 
        
        or
        
        [[str departments] [str latest_versions]]]
    
    """
    dept_paths,departments = lsa.lsa.list_depts_from_shot(shotname)
    if get_latest_version:
        latest_versions = [lsa.lsa.get_versions_from_dept(dept_path,list_all_versions=False) 
                           for dept_path in dept_paths]
        return latest_versions
    else:
        all_versions = [lsa.lsa.get_versions_from_dept(dept_path) for dept_path in dept_paths]
        return [departments,all_versions]
        

def make_dept_menu(node):
    """
    Uses the function get_dict_with_versions to return the data needed to 
    create the menu.
    """
    shot = hou.getenv('SHOT')
    versions = get_dict_with_versions(shot)
    return versions
    

def buildb(node):
    """
    A callback script for the button 'build' which builds with
    the selected versions in the UI.
    """
    mp = node.parm('depts')
    mp_data = mp.multiParmInstancesAsData()
    build_data = []
    for mpi in mp_data:
        if mpi['live_dept_path#'] == '':
            mpi['live_dept_path#']=mpi['dept_path#']
        if mpi['live_dept_path#'] is not mpi['dept_path#']:
            mpi['live_dept_path#']=mpi['dept_path#']
        build_data.append(mpi)
    mp.setMultiParmInstancesFromData(build_data)
    
    
def load(node):
    """
    This is a callback script for the button 'load'
    It will let the user load new departments that do not exist in the 
    multiparm 'depts'.
    """
    mp = node.parm('depts')
    if mp.evalAsInt() == 0:
        mp.set(1)
        [x.set(x.menuItems()[0]) for x in mp.multiParmInstances() if 'dept_name' in x.name()]
        [x.set(x.menuItems()[-1]) for x in mp.multiParmInstances() if 'dept_path' in x.name() and 'live_' not in x.name()]
    mp = node.parm('depts')
    mp_data = mp.multiParmInstancesAsData()
    depts_loaded = [x['dept_name#'] for x in mp_data]
    departments,versions = make_dept_menu(node)
    [departments.remove(x) for x in depts_loaded]
    for dept in departments:
        dept_index= mp.evalAsInt()
        mp.insertMultiParmInstance(dept_index)
        dept_index = mp.evalAsInt()
        mp_data = mp.multiParmInstancesAsData()
        mp_data[-1]['dept_name#']=dept
        mp.setMultiParmInstancesFromData(mp_data)
        dept_path = hou.parm('dept_path'+str(dept_index))
        path = dept_path.menuItems()[-1]
        dept_path.set(path)
        

def update(node):
    """
    Callback script for the button Updates versions to Latest.
    It just make the currently selected versions in all the departments in the
    multi-parm to be latest.
    """
    mp = node.parm('depts')
    depts_paths = [x for x in mp.multiParmInstances() if 'dept_path' in 
                   x.name() and 'live_' not in x.name()]
    latest_versions = [x.set(x.menuItems()[-1]) for x in 
                       mp.multiParmInstances() if 'dept_path' in 
                       x.name() and 'live_' not in x.name()]
    
def append_stage_with_paths(path_list=[]):
    """
    Use in a python LOP to build the stage with a list of paths.
    
    Args:
        
        path_list (str. path list) : list of paths to `.usd` files.
    """
    if len(path_list) != 0:
        stage = hou.pwd().editableStage()
        usd_files_to_load = path_list
        for usd_file in usd_files_to_load:
            if os.path.exists(usd_file):
                root = stage.GetEditTarget().GetLayer()
                layer = root.subLayerPaths.append(usd_file)
            else:
                print(f"USD file not found: {usd_file}")

def get_usd_path_list(node):
    """
    This will return a list of values for multiParmInstances 
    of Current Dept Path.

        Args:
            
            node(hou.Node): Usually the multiparm would be on a parent hda. 
            Use `hou.pwd().parent()` to get to the node.
    """
    mp = node.parm('depts')
    path_list = [x.eval() for x in mp.multiParmInstances()
                  if 'live_dept_path' in x.name()]
    return path_list