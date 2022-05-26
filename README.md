Project description
-------------------

These two programs perform backups/deletes by file extension type. 
The delete program sends the files to the trash/recycle bin in case you need those files back. 


Input options
-------------

The user can enter the extension type as a command line argument.  
If no command line argument was entered, the program will ask for a file extension type 
through terminal input.

The user is free to enter the extension type with a dot or without.  
For example, pdf and .pdf are both acceptable inputs. 


Files included
--------------

backup_by_extension.py:   
The program makes a new folder in the cwd called "extension_type_Backup_Folder and copies all the files 
with the chosen extension type to this folder.  
For example, if the chosen extension type is txt, the new folder's name will be txt_Backup_Folder.  
If this folder already exists, then a number is appended(and possibly incremented) to the folder name until a unique 
folder can be made.


delete_by_extension.py: 
This deletes all the files with the entered extension type.  
These files are sent to the trash/recycle bin, so they are still recoverable.  
The program displays which files are going to be deleted and allows you to exit early 
if you don't want to delete those files. 

file_extension_functions.py:
Contains some functions used in both files.  

3 sample files to test these programs on.  
    * An empty pdf  
    * Two txt files containing dialogue from Mr.Robot  


Requirements
------------

1) python  

2) send2trash  

3) sys, os, shutil, pathlib are all used as well.

4) do not forget the included file_extension_functions.py file


