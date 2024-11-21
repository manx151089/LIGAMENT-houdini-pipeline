import hou
import os
from lgmfxShotApi import lsa



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
    #departments = lsa.list_depts_from_shot
    directory = pub_directory
    base_directory = os.path.join(show,shotname,directory)
    departments = [
        d for d in os.listdir(base_directory) 
        if os.path.isdir(os.path.join(base_directory, d))
    ]

    usd_files_to_load = []
    stage = hou.pwd().editableStage()

    for dept in departments:
        usd_file_path = os.path.join(base_directory, dept, "geometry_v001.usd")
        usd_file_path = os.path.normpath(usd_file_path)
        if os.path.exists(usd_file_path):
            usd_files_to_load.append(usd_file_path)
        else:
            #hou.ui.displayMessage(f"USD file not found in department '{dept}': {usd_file_path}")
            print(f"USD file not found in department '{dept}': {usd_file_path}")

    print('usd_files_to_load:',usd_files_to_load)
    for usd_file in usd_files_to_load:
        stage.GetRootLayer().subLayerPaths.append(usd_file)

    hou.ui.displayMessage(f"USD files loaded from departments: {', '.join(departments)}")
    
    

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
        