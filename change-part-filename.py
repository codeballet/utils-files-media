import os
import re


def main():
    # Get information from user
    directory = input("Directory: ")

    # Print out existing files in directory
    print("\nExisting files:")
    for filename in os.listdir(directory):
        print(filename)

    # Get pattern and replacement from user
    pattern = input("\nPattern to replace: ")
    replacement = input("Replacement: ")

    for filename in os.listdir(directory):
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