from file_extension_functions import *
import send2trash


def are_you_sure_prompt():
    """Asks the user if they are sure that they want to delete the files.
    Ends the program if they don't enter Y/y"""

    prompt = "Are you sure you want to delete these files? (Y/y or N/n): "
    responce = input(prompt)

    if len(responce) == 0:
        print()
        return are_you_sure_prompt()    # re-prompt if no answer was given

    if responce[0] != 'Y' and responce[0] != 'y':
        print("\nEnding program without deleting the files")
        exit()


def main():
    print('\n')

    # get the file extension type as tuple that contains:
    #   [0] file extension with a dot prepended to it
    #   [1] file extension without the dot
    file_extension_type = get_file_extension()

    # get all the files to be deleted, display them, and prompt the user before finally deleting the files
    files_to_delete = []
    files_to_delete = generate_files(files_to_delete, file_extension_type)
    display_files(files_to_delete)
    are_you_sure_prompt()

    for f in files_to_delete:
        send2trash.send2trash(f)    # sends to trash to avoid permanately deleting
    
    print(f"Successfully delete the files\n")


if __name__ == '__main__':
    main()

    print('\n')