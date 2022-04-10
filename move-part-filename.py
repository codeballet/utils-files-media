import os
import re


def main():
    # Get information from user
    directory = input("File location: ")

    for filename in os.listdir(directory):

        # extract the prefix and suffix of the filename
        file_parts = filename.split('.')
        prefix = file_parts[0]
        suffix = file_parts[1]

        # extract the parts of the prefix
        prefix_parts = prefix.split('_')

        # get the edited number
        image_version = prefix_parts[4].split('-')[0]
        image_name = prefix_parts[4].split('-')[1]

        # set destination, source, and rename file
        dst = f"{directory}/{prefix_parts[0]}_{prefix_parts[1]}_{prefix_parts[2]}_{prefix_parts[3]}_{image_name}_{image_version}.{suffix}"
        src = f"{directory}/{filename}"
        os.rename(src, dst)


    print("Done!")

if __name__ == '__main__':
    main()
