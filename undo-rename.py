import os
import re


def main():
    # get user input
    directory = input("File location: ")
    re.sub(r'\\$', '', directory)
    re.sub(r'\/$', '', directory)

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


if __name__ == '__main__':
    main()
