import os


def main():
    # Get information from user
    directory = input("File location: ")

    for filename in os.listdir(directory):
        # extract parts and lower case of filename
        file_parts = filename.split('.')
        prefix = file_parts[0]
        suffix = file_parts[1].lower()

        # set destination, source, and rename file
        dst = f"{directory}/{prefix}.{suffix}"
        src = f"{directory}/{filename}"
        os.rename(src, dst)

    print("Done!")

if __name__ == '__main__':
    main()
