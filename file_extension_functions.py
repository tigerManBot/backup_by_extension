import sys
from pathlib import Path 


# The functions in this file will be imported to both files


def get_file_extension():
    """Gets the file extension type either by command line or by user input if command line was not used.
    Returns a tuple with two strings:
        1) file extension with a dot prepended to it
        2) file extension without the dot
    """

    if len(sys.argv) > 1:
        file_extension_type = sys.argv[1]
    else:
        file_extension_type = input("Enter a file extension type: ")
    
    if file_extension_type[0] == '.':
        return file_extension_type, file_extension_type.replace('.', '')

    return f".{file_extension_type}", file_extension_type, 


def get_extension_pattern(file_extension_type): 
    """Takes in the file_extension_type (with a dot in front of it) and
    returns a string that will be passed into the glob function."""

    return f"*{file_extension_type}"    # '*' allows for any characters up to the file extension


def generate_files(files, file_extension_type):
    """Returns a list of files whose extension matches extension pattern.
    Ends the program if this list is empty."""

    extension_regex = get_extension_pattern(file_extension_type[0])
    files = list(Path.cwd().glob(extension_regex))
   
    if len(files) <= 0:
        print(f"\nThere are no {file_extension_type[1]} files in the cwd.")
        print(f"Ending program.\n")
        exit()
    
    return files


def display_files(files):
    """Sorts the files alphabetically, then prints them all"""

    files.sort()

    print("\nFiles to be deleted: ")
    for f in files:
        print(f.name)   # only prints the file's name, not including the path
    print()
    