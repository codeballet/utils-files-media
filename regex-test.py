import os
import re

# examples of using regex

def main():
    # Get information from user
    directory = input("File location: ")

    for filename in os.listdir(directory):

        # extract the prefix and suffix of the filename
        file_parts = filename.split('.')
        prefix = file_parts[0]
        suffix = file_parts[1]

        r1 = re.findall(r'^\w+', prefix)
        print(r1)

        r2 = re.split(r'_a7m3', prefix)
        print(r2)

        r3 = re.findall(r'_edit\d{2}', prefix)
        print(r3)

        r4 = re.split(r'_edit\d{2}', prefix)
        print(r4)


    print("Done!")

if __name__ == '__main__':
    main()
