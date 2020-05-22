###########################    ╲*-                  -*╱                              
# MFC FILE COMMANDER      #     ╲*█*╲     *      ╱*█*╱     
# core.py - Dev 0.0.3     #      ╲*██*╲  ╱▐╲  ╱*██*╱            
# 2020, Nikita Tarasenko  #        ╲*█ *▄ * ▄* █*╱                                 
###########################          *╱  ╲▐╱  ╲*
#▐#▐#▐#▐#▐#▐#▐#▐#▐#▐#▐#▐#▐#               *
from __future__ import (absolute_import, division, print_function)
import os
import sys
import shutil
import tempfile
from os.path import join, isdir, realpath, exists


class DirectoryControl(object):
    """The main class of core.py.
       Have a simple actions, like
       watching files in current directory,
       archive it, remove current dir,
       rename it, etc.
    """
    
    def __init__(self, cdir):
        self.cdir = cdir
        cdir = str(os.getcwd())
        global path_list
        path_list = [cdir] #to write path-history

    

    def DirectoryView(self, cur_disc=os.listdir()):
        """Method 'DirectoryBaseActions' with actions,
           like make new dir(s), remove dir(s), archive dir(s)
           with diverse formats (.7z, .bzip, .tar, .zip)
        """
        current_path = os.getcwd()
        print(f'Current path now: {current_path}')
        print(*cur_disc, sep='\n')
      
    def DirectoryMake(self):
        """Method 'DirectoryMake' - make new dir
        """
        dir_name = str(input('Get name to new dir: '))
        os.mkdir(dir_name)
        try:
           for i in range(os.listdir()):
              if os.mkdir(dir_name) == i:
                 os.mkdir(dir_name)
        except FileExistsError:
           print('Directory with this name was already exists!')
        print('Complete!')
        
      
    def DirectoryRemove(self, cdir):
        """Method 'DirectoryRemove' - rename chosen dir
        with arg 'dir'
        """
        os.rmdir(cdir)
        print('Complete!')
        

    def DirectoryRename(self, cdir):
        """Method 'DirectoryRename' - rename chosen dir
        with arg 'dir'
        """
        new_dirname = str(input('Get new name to dir: '))
        os.rename(cdir, new_dirname)
        print(f'Complete! Now its {cdir}') #debug
    

    def DirectoryChange(self, cdir):
        """Method 'DirectoryChange' - change the current 
        working directory to the specified with arg 'cdir'
        """
        nplace = str(input('Path with dir to change: '))
        try:
            os.chdir(cdir, nplace)
            print('Dir was change')
        except OSError:
            print(f'Directory "{nplace}" is not exist in this path')
            sys.exit()

        if os.path.exists(nplace):
            os.chdir(nplace)
        else:
            raise OSError


    def DirectoryMove(self, cdir):
        """Method 'DirectoryMove' - moving the current
        working directory to the another path with arg 'cdir'
        """
        new_path = str(input('Insert here new absolute path: '))
        shutil.move(cdir, new_path)
        print(f'Complete! Now its {cdir}') #debug



class FilesControl(DirectoryControl): 
    """Sub-main class 'FilesControl' -
       have some methods with
       rename, remove, add new, open
       and get info about current file(s) in dir(s)
    """


    def __init__(self, file):
        self.file = file

    def DirectoryRename(self, file):
        """Polimorfed method to rename chosen file
        with arg 'file'
        """
        new_filename = str(input('Get new name to file: '))
        os.rename(file, new_filename)
        print(f'Complete! Now its {file}')

        

    def Remover(self, file):
        """
        Remove chosen file with help
        of arg 'file'
        """
        tmp_file = tempfile.NamedTemporaryFile(file + 'tmp.txt')
        shutil.copy(file, tmp_file, )
        os.remove(file)
        print('Complete this shit!')
        try:
            for i in range(0, os.listdir()):
               if file == i:
                  os.remove(file)
        except FileNotFoundError:
            raise FileNotFoundError
        
    def Touch(self):
        """
        Make new file
        """
        name = str(input('Give name to new file: '))
        new_file = open(name, 'tw', encoding='utf-8')
        new_file.close()
        print(f'Complete of making file: {name}')
        
           


    def FilesOpenFunction(self, file):
        """Method 'FilesOpenFunction' -
           get filename like arg and
           parse available text-editors
           (and some other programs to open files)
           or open editor.py
        """
        pass


           
