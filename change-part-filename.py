import os
import re


def main():
    # Get information from user
    directory = input("Directory: ")
    pattern = input("Pattern to replace: ")
    replacement = input("Replacement: ")

    print('\nOld filenames:')
    for filename in os.listdir(directory):
        print(filename)
        # Substitute the pattern with replacements
        new_name = re.sub(f"{pattern}", replacement, filename)

        # Rename the files
        dst = f"{directory}/{new_name}"
        src = f"{directory}/{filename}"
        os.rename(src, dst)

    print('\nNew filenames:')
    for filename in os.listdir(directory):
        print(filename)


if __name__ == '__main__':
    main()