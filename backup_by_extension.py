from file_extension_functions import *      # my import file
import os, shutil


def make_new_folder(ORIGINAL_NAME, incremented_name, number_at_end):
    """Tries to make a new folder called ORIGINAL_NAME.
    If this folder already exists in the cwd, a number is appended to its name,
    and the function calls itself again to try again, (each time the number at the end increments).
    This process continues until a folder with a unique name is made.
    Finally, a new folder is created with that name and its name is returned as a string."""

    if number_at_end == 1: 
        incremented_name = ORIGINAL_NAME    # This block is always reached on the first call
        # the original name needs to be preserved
        # otherwise, name increments like: folder_name1 -> folder_name12 -> folder_name123
        # instead of: folder_name1 -> folder_name2 -> folder_name3
    
    try:
        os.mkdir(incremented_name)
        return incremented_name
    except FileExistsError:
        number_at_end += 1
        incremented_name = f"{ORIGINAL_NAME}{str(number_at_end)}"
        return make_new_folder(ORIGINAL_NAME, incremented_name, number_at_end)


def main():
    print('\n')

    # get the file extension type as tuple that contains:
    #   [0] file extension with a dot prepended to it
    #   [1] file extension without the dot
    file_extension_type = get_file_extension()
    
    # Get the files that will be copied as a list and set up the folder the copies will be sent to
    files_to_copy = []
    files_to_copy = generate_files(files_to_copy, file_extension_type)
    folder_name = make_new_folder(f"{file_extension_type[1]}_Backup_Folder", "", 1)

    # perform the copy
    for f in files_to_copy:
        shutil.copy(f, folder_name)

    print(f"Successfuly copied all the {file_extension_type[1]} files", end=" ")
    print(f"to a folder called {folder_name}\n")


if __name__ == '__main__':
    main()

    print('\n')
