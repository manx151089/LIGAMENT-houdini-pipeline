import os
import glob
class lsa:
    '''
    This is a shot api that can be used in various tools to resolve show,shot,sequence and various other metadata

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
        

    def get_show_from_shot(shot,path=False):
        '''
        This function returns the seq name or path
        Args:
            path (boolean): To return the path instead of just the seq name
        Returns:
            show
        '''
        folders = os.path.split(shot)
        offset = 1
        idx_seq = self.get_prod_folder_from_path(folders)+offset
        if path:
            list_of_folders = folders[:idx_show]
            show = os.path.join(list_of_folders)
        else:
            show = folders[idx_show]


    def list_depts_from_shot(shot):
        '''
        This will create a list of departments that have published usds for a shot

        Returns:
            list_of_depts
        '''
        folders = os.path.split(shot)
        offset = 1
        idx_seq = self.get_prod_folder_from_path(folders)+offset
        if path:
            list_of_folders = folders[:idx_show]
            show = os.path.join(list_of_folders)
        else:
            show = folders[idx_show]

        list_of_depts
        return list_of_depts
    
