###########################    ╲*-                  -*╱                              
# MFC FILE COMMANDER      #     ╲*█*╲     *      ╱*█*╱     
# core.py - Dev 0.0.3     #      ╲*██*╲  ╱▐╲  ╱*██*╱            
# 2020, Nikita Tarasenko  #        ╲*█ *▄ * ▄* █*╱                                 
###########################          *╱  ╲▐╱  ╲*
#▐#▐#▐#▐#▐#▐#▐#▐#▐#▐#▐#▐#▐#               *

"""'core' - MFC Basic files and directory control module - 
took arguments 'cdir' and 'file' before start
(or goes to the home dir and choose first dir or file by default)"""

from __future__ import (absolute_import, division, print_function)
import os
import sys
import shutil
import tempfile
from timeit import default_timer as oper_time
import numpy
from os.path import join, isdir, realpath, exists


class DirectoryControl(object):
    """The main class of core.py.
       Have a simple actions, like
       watching files in current directory,
       archive it, remove current dir,
       rename it, etc.
    """
    
    def __init__(self, cdir = None, path_list = None):
        self.cdir = cdir
        path_list = []

    
    def DirectoryView(self, cur_disc=os.listdir()):
        """Method 'DirectoryBaseActions' with actions,
           like make new dir(s), remove dir(s), archive dir(s)
           with diverse formats (.7z, .bzip, .tar, .zip)
        """
        oper_timetest = oper_time()
        current_path = os.getcwd()
        elapsed = oper_time() - oper_timetest
        print_format = "{:<2} function was executed in {:.10f} secs."
        print(print_format.format(current_path, elapsed))
      
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
            print('Dir was changed')
        except OSError:
            print(f'Directory "{nplace}" is not exist in this path')
            sys.exit()

        if os.path.exists(nplace):
            os.chdir(nplace)
        else:
            raise OSError
  
""" def FileMove(self, file):
        file = os.listdir([0])
        print(file) #debug
        sys.getsizeof(file)""" #not working


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
        #print(f'Complete! Now its {file}')

        

    def Remover(self, file):
        """
        Remove chosen file with help
        of arg 'file'
        """
        oper_timetest = oper_time()
        os.remove(file)
        elapsed = oper_time() - oper_timetest
        print_format = "{:<2} function was executed in {:.10f} secs."
        print(print_format.format(os.__name__, elapsed))
        
    def FileTouch(self):
        """
        Make new file
        """
        name = str(input('Give name to new file: '))
        new_file = open(name, 'tw', encoding='utf-8')
        new_file.close()
        #print(f'Complete of making file: {new_file}')
     
           
     # TODO: Make queue method for files

    def FilesOpenFunction(self, file):
        """Method 'FilesOpenFunction' -
           get filename like arg and
           parse available text-editors
           (and some other programs to open files)
           or open editor.py
        """
        pass


           
