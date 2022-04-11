import os
import re


def cleanup(text):
    '''
    Cleans up user input.
    Replaces whitespace and hyphen with underscore.
    Exits if non-alphanunerical characters are used.
    Lowers all letters.
    '''
    text = text.replace(" ", "_")
    text = text.replace("-", "_")
    if not re.match(r'^[a-zA-Z0-9_]+$', text):
        print('\nPlease only use letters, numbers, and underscore "_".')
        exit()
    return text.lower()


def get_info(choice):
    '''
    Collects information from user for new filename
    '''
    # Get information from user
    directory = input("\nFile location: ")
    # remove end backslash, if existing
    re.sub(r'\/$', '', directory)

    if not os.path.exists(directory):
        # given directory does not exist
        print('The given directory does not exist!')
        exit()

    if choice != 3:
        # user wants to change filenames, get more info
        date = input("Date (yymmdd): ")
        if not re.match(r'^\d{6}$', date):
            print("Please enter the date as yymmdd, using six digits.")
            exit()

        project = cleanup(input("Project name: "))

        source = cleanup(input("Source (camera, person, organisation, etc.): "))

        info = cleanup(input("Other info (card number, colour space, location, etc.): "))

        # Give feedback to user
        print(f"\nYou will be changing filenames in the folder:\n{directory}")

    if choice == 1:
        # keep original filname
        keep_original(directory, date, project, source, info)
    elif choice == 2:
        change_all(directory, date, project, source, info)
    else:
        # choice is 3
        undo(directory)

def proceed(question):
    '''
    Checks if a user wants to proceed based on question
    '''
    # check to proceed with user
    answer = input(f'\n{question}\n')

    if re.match(r'^[Yy].*', answer):
        # user responded yes
        return True

    # user not agreeing
    return False


def change_all(directory, date, project, source, info):
    '''
    Completely changes a filename, replacing original with a four digit count
    '''
    print(
        f"\nYour new filenames will be:\n{project}_{date}_{source}_{info}_<count>.<filetype>")

    if proceed('Are you sure everything above is correct? (yes/no)'):
        # sort files in alphabetical order
        list_dir = os.listdir(directory)
        list_dir = [f.lower() for f in list_dir]
        sorted(list_dir)

        for count, filename in enumerate(list_dir):
            # extract the prefix and suffix of the filename
            file_parts = filename.split('.')
            suffix = file_parts[1]

            # set destination, source, and rename file
            dst = f"{directory}/{project}_{date}_{source}_{info}_{count:04d}.{suffix}"
            src = f"{directory}/{filename}"
            os.rename(src, dst)
    else:
        print("Nothing changed, exiting the program.")
        exit()

    print("Done!")       


def keep_original(directory, date, project, source, info):
    '''
    Adds new information to filename, keeping the original name
    '''
    print(
        f"\nYour new filenames will be:\n{project}_{date}_{source}_{info}_<original>.<filetype>")

    if proceed('Are you sure everything above is correct? (yes/no)'):
        for filename in os.listdir(directory):
            # extract the prefix and suffix of the filename
            file_parts = filename.split('.')
            prefix = file_parts[0]
            suffix = file_parts[1]

            # If prefix has underscores, replace with dashes
            # to use with regex when undoing the action
            prefix = prefix.replace("_", "-")

            # set destination, source, and rename file
            dst = f"{directory}/{project}_{date}_{source}_{info}_{prefix}.{suffix}"
            src = f"{directory}/{filename}"
            os.rename(src, dst)
    else:
        print("\nNothing changed, exiting the program.")
        exit()

    print("\nDone!")


def undo(directory):
    '''
    Reverts filename to the original or count only
    '''
    for filename in os.listdir(directory):
        # split filename by underscores
        file_parts = filename.split('_')

        # use the last part as the restored name
        restored_file = file_parts[-1]
        # replace dashes with underscores
        restored_name = restored_file.replace("-", "_")

        # set destination, source and rename file
        dst = f"{directory}/{restored_name}"
        src = f"{directory}/{filename}"
        os.rename(src, dst)
        
    print("Done!")


def main():
    '''
    Gives user choices of what to do
    '''
    # ask user what to do
    print('\nPlease choose one of the following options:')
    print('1. Keep original filenames when renaming')
    print('2. Discard original filenames when renaming')
    print('3. Undo filename change from 1, or only keep count from 2')
    choice = input('\nChoice: ')

    # check user input
    if not re.match(r'^[123]$', choice):
        print('Please enter one digit: 1, 2, or 3')
        exit()

    response = False
    choice = int(choice)

    if choice == 1:
        response = proceed('Do you want to KEEP the original filenames? (yes/no)')
    elif choice == 2:
        response = proceed('Do you want to DISCARD the original filenames? (yes/no)')
    else:
        # choice is 3
        response = proceed('Do you want to REMOVE all but the original filenames / counts? (yes/no)')

    if response:
        get_info(choice)
    elif not response:
        # response is False, exit the program
        print('No changes made, exiting the program.')
        exit()


if __name__ == '__main__':
    main()
