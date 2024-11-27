import hou
import os
from lgmfxShotApi import lsa
import glob



def load_usd_files_from_departments(shotname,show,pub_directory="usd"):
    '''
    Scans the specified base directory for department subfolders, checks for 
    the presence of "geometry.usd" files in each department folder, and loads
    them into the LOP stage in Houdini. If any USD file is missing, a message
    is displayed for the user.The root directory where department folders (fx,
    animation, crowd, layout, etc.) are stored. Each department folder should
    contain a "geometry.usd" file.

    Args: 
        shotname (str): folder name of the shot
        show (str path): path of the show
    Returns:
        None

    TO-DO:
    Need to divide this function into two one to make a list of depts 
    and one to load a single stage from the dept and append to the current stage
    '''
    
    ###NEED TO FIX THIS ONE NOW to use LSA properly and test in houdini LSA first and this script later
    #departments_v2 = lsa.list_depts_from_shot
    #print(departments_v2)
    directory = pub_directory
    base_directory = os.path.normpath( os.path.join(show,shotname,directory))
    usd_files_to_load = glob.glob(base_directory+'\*\*geometry_v001.usd')
    usd_files_to_load = [x.replace('\\\\','/') for x in usd_files_to_load]
    #to avoid all this above scripts repetitively we need a shotApi which
    #will resolve the paths to the format we want
    
    stage = hou.pwd().editableStage()
    for usd_file in usd_files_to_load:
        if os.path.exists(usd_file):
            root = stage.GetEditTarget().GetLayer()
            layer = root.subLayerPaths.append(usd_file)
            print(f"USD file appended: {usd_file} \n in layer: {layer}")

        else:
            print(f"USD file not found: {usd_file}")

"""
if __name__ == "__main__":
    # Testing the function by fetching shot and show from Houdini's environment variables
    shot = hou.getenv("SHOT")
    show = hou.getenv("SHOW")

    if shot and show:
        load_usd_files_from_departments(shot, show)
    else:
        hou.ui.displayMessage("SHOT or SHOW environment variables are not set.")
        """
        