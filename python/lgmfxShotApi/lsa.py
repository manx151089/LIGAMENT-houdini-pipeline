import os
import glob
class lsa:
    '''
    lsa is a shot api that can be used in various tools to resolve show,shot,sequence and various other metadata

    Functions:
        get_prod_folder_from_path()
        get_seq_from_shot()
        get_show_from_shot()
        list_depts_from_shot()
    '''
    def get_prod_folder_from_path(self,path):
        '''
        Returns:
            index (int): The index of the prod folder
        '''
        if os.path.exists(path):
            folder_list = os.path.split(path)
            index = folder_list.index('prod')
        return index


    def get_seq_from_shot(self,shot,path=False):
        '''
        This function returns the seq name or path
        Args:
            shot (directory): A directory of the shot
            path (boolean): To return the path instead of just the seq name
        Returns:
            seq (str):name or path
        '''
        folders = os.path.split(shot)
        offset = 3
        idx_seq = self.get_prod_folder_from_path(folders)+offset
        if path:
            list_of_folders = folders[:idx_seq]
            seq = os.path.join(list_of_folders)
        else:
            seq = folders[idx_seq]
        return seq
        

    def get_show_from_shot(self,shot,path=False):
        '''
        This function returns the seq name or path
        Args:
            path (boolean): To return the path instead of just the seq name
        Returns:
            show
        '''
        folders = os.path.split(shot)
        offset = 1
        idx_show = self.get_prod_folder_from_path(folders)+offset
        if path:
            list_of_folders = folders[:idx_show]
            show = os.path.join(list_of_folders)
        else:
            show = folders[idx_show]


    def list_depts_from_shot(shot):
        '''
        This will create a list of departments that have published usds for a shot

        Args:

            shot (str. path): String that is a path to shot. It needs to have 
            a parent folder called "shots" and in the same level of "shots" 
            there would be a sister folder with all the publishes called as 
            usd which should have the same folder structure.

        Returns -> [department_paths,departments]
            
            department_paths (list): List of the department paths that have 
            published a file in the usd folder,

            departments (list): List of the folder names of the department.

        To-do:
            Need to add a version resolver function
        '''
        dept_dirs = []
        pubs = shot.replace('shots','usd')
        if os.path.exists(pubs):
            dept_dirs = os.listdir(pubs)
        else:
            print("no usd shot folder found!")
        if len(dept_dirs)>0:
            dept_paths = [
            os.path.join(pubs,d) for d in dept_dirs
            if os.path.isdir(os.path.join(pubs, d))
            ]
            return [dept_paths,dept_dirs]
        else:
            return None
    

    def get_versions_from_dept(dept_path,list_all_versions=True,padding=3):
        """
        Usage:
            get_version_from_dept(dept_path,list_all_versions=True,padding=3)

        Args:
            dept_path : dept path would be folder in which there would be 
            version folders followed by a geometry file called 'geometry.*'

            list_all_versions : return a list of all the versions in that 
            task/dept folder.
            
            padding : number of digits in the folder string 
            (for example v001 has 3 digits so the padding would be 3)
        """
        search_str = str(dept_path)+'/v*/geometry.*'
        version_dirs = glob.glob(search_str)
        versions = {int(v.replace('\\','/').split('/geometry.')[0][-padding:]):v for v in version_dirs}
        if list_all_versions is True:
            #print (versions)
            return versions
        else:
            return versions[max(versions.keys())]
            



#shot='D:/prod/lgmfx/shots/seq_001/cdev_genericstest_001'
#depts = lsa.list_depts_from_shot(shot)[0]
#dept_path = depts[0]
#print(lsa.get_versions_from_dept(dept_path,list_all_versions=False))