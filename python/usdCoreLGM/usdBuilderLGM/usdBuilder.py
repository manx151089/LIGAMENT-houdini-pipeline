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

    #print('PRELOAD : usd files found:',usd_files_to_load)
    stage = hou.pwd().editableStage()
    for usd_file in usd_files_to_load:
        if os.path.exists(usd_file):
            root = stage.GetEditTarget().GetLayer()
            layer = root.subLayerPaths.append(usd_file)
            #print(f"USD file appended: {usd_file} \n in layer: {layer}")

        else:
            print(f"USD file not found: {usd_file}")
    
def get_dict_with_versions(shotname,get_latest_version=False):
    dept_paths,departments = lsa.lsa.list_depts_from_shot(shotname)
    if get_latest_version:
        latest_versions = [lsa.lsa.get_versions_from_dept(dept_path,list_all_versions=False) for dept_path in dept_paths]
        return latest_versions
    else:
        all_versions = [lsa.lsa.get_versions_from_dept(dept_path) for dept_path in dept_paths]
        #idx = 0
        #dept_dict = {}
        #for department in departments:
            #dept_versions = all_versions[idx]
            #print(department,dept_versions,'<<<<<<<<<<\n\n\n\n')
            #dept_dict['tst']= dept_versions[idx]
            #idx+=1
        return [departments,all_versions]
        
        
def set_multiparms_with_dict(node):
    depts = node.parm('depts')
    

def make_dept_menu(node):
    shot = hou.getenv('SHOT')
    versions = get_dict_with_versions(shot)
    return versions
    

def buildb(node):
    mp = node.parm('depts')
    mp_data = mp.multiParmInstancesAsData()
    build_data = []
    for mpi in mp_data:
        if mpi['live_dept_path#'] is '':
            mpi['live_dept_path#']=mpi['dept_path#']
        if mpi['live_dept_path#'] is not mpi['dept_path#']:
            mpi['live_dept_path#']=mpi['dept_path#']
        build_data.append(mpi)
    mp.setMultiParmInstancesFromData(build_data)
    
    
def load(node):
    mp = node.parm('depts')
    mp_data = mp.multiParmInstancesAsData()
    depts_loaded = [x['dept_name#'] for x in mp_data]
    departments,versions = make_dept_menu(node)
    #depts_loaded.remove(departments)
    [departments.remove(x) for x in depts_loaded]
    print(departments)#need to load these departments
    