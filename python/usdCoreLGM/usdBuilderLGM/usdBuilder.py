import hou
import os


def load_usd_files_from_departments(shot,show,directory="usd"):
    '''
    Scans the specified base directory for department subfolders, checks for the presence of "geometry.usd"
    files in each department folder, and loads them into the LOP stage in Houdini. If any USD file is missing,
    a message is displayed for the user.

    Args:
        base_directory (str): The root directory where department folders (fx, animation, crowd, layout, etc.) are stored.
                             Each department folder should contain a "geometry.usd" file.
    
    Returns:
        None
    '''
    base_directory = os.path.join(show,shot,directory)
    departments = [
        d for d in os.listdir(base_directory) 
        if os.path.isdir(os.path.join(base_directory, d))
    ]

    usd_files_to_load = []
    stage = hou.pwd().editableStage()

    for dept in departments:
        usd_file_path = os.path.join(base_directory, dept, "geometry.usd")

        if os.path.exists(usd_file_path):
            usd_files_to_load.append(usd_file_path)
        else:
            hou.ui.displayMessage(f"USD file not found in department '{dept}': {usd_file_path}")

    for usd_file in usd_files_to_load:
        stage.GetRootLayer().SubLayerStack.append(usd_file)

    hou.ui.displayMessage(f"USD files loaded from departments: {', '.join(departments)}")


if __name__ == "__main__":
    # Testing the function by fetching shot and show from Houdini's environment variables
    shot = hou.getenv("SHOT")
    show = hou.getenv("SHOW")

    if shot and show:
        load_usd_files_from_departments(shot, show)
    else:
        hou.ui.displayMessage("SHOT or SHOW environment variables are not set.")