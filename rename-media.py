import os
import re


def cleanup(text):
    # clean up whitespaces, hyphens, non-alphanumerical characters, capitals
    text = text.replace(" ", "_")
    text = text.replace("-", "_")
    if not re.match(r'^[a-zA-Z0-9_]+$', text):
        print('\nPlease only use letters, numbers, and underscore "_".')
        exit()
    return text.lower()


def get_info(choice):
    # Get information from user
    directory = input("File location: ")
    # remove end backslash, if existing
    re.sub(r'\/$', '', directory)

    if not os.path.exists(directory):
        # given directory does not exist
        print('The given directory does not exist!')
        exit()

    date = input("Date (yymmdd): ")
    if not re.match(r'^\d{6}$', date):
        print("Please enter the date as yymmdd, using six digits.")
        exit()

    project = cleanup(input("Project name: "))

    camera = cleanup(input("Camera: "))

    info = cleanup(input("Other info (card number, colour space, location, etc.): "))

    # Give feedback to user
    print(f"\nYou will be changing filenames in the folder:\n{directory}")

    if choice == 1:
        # keep original filname
        keep_original(directory, date, project, camera, info)
    else:
        # choice is 2, discard original filename
        change_all(directory, date, project, camera, info)


def proceed(question):
    # check to proceed with user
    answer = input(f'\n{question}: ')

    if re.match(r'^[Yy].*', answer):
        # user responded yes
        return True

    # user not agreeing
    return False


def change_all(directory, date, project, camera, info):
    print(
        f"\nYour new filenames will be:\n{project}_{date}_{camera}_{info}_<count>.<filetype>")

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
            dst = f"{directory}/{project}_{date}_{camera}_{info}_{count:04d}.{suffix}"
            src = f"{directory}/{filename}"
            os.rename(src, dst)
    else:
        print("Nothing changed, exiting the program.")
        exit()

    print("Done!")       


def keep_original(directory, date, project, camera, info):
    print(
        f"\nYour new filenames will be:\n{project}_{date}_{camera}_{info}_<original>.<filetype>")

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
            dst = f"{directory}/{project}_{date}_{camera}_{info}_{prefix}.{suffix}"
            src = f"{directory}/{filename}"
            os.rename(src, dst)
    else:
        print("\nNothing changed, exiting the program.")
        exit()

    print("\nDone!")


def main():
    # ask user what to do
    print('\nPlease choose one of the following options:')
    print('1. Keep original filenames when renaming')
    print('2. Discard original filenames when renaming')
    choice = input('\nChoice: ')

    # check user input
    if not re.match(r'^[12]$', choice):
        print('Please enter either digit 1 or 2')
        exit()

    response = False
    choice = int(choice)

    if choice == 1:
        response = proceed('Are you sure you want to KEEP the original filenames?')
    else:
        # choice is 2
        response = proceed('Are you sure you want to DISCARD the original filenames?')

    if response:
        get_info(choice)
    elif not response:
        # response is False, exit the program
        print('No changes made, exiting the program.')
        exit()


if __name__ == '__main__':
    main()
