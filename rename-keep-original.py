import os
import re


def cleanup(text):
    # remove whitespaces, hyphens, and non-alphanumerical characters
    text = text.replace(" ", "_")
    text = text.replace("-", "_")
    if not re.match(r'^[a-zA-Z0-9_]+$', text):
        print('Please only use letters, numbers, and underscore "_".')
        exit()
    return text.lower()


def main():
    # Get information from user
    directory = input("File location: ")
    # remove final backslash, if existing
    re.sub(r'\/$', '', directory)

    date = input("Date (yymmdd): ")
    if not re.match(r'^\d{6}$', date):
        print("Please enter the date as yymmdd, using six digits.")
        exit()

    project = cleanup(input("Project name: "))
    # project = project.replace(" ", "_")
    # project = project.replace("-", "_")

    camera = cleanup(input("Camera: "))
    # camera = camera.replace(" ", "_")
    # camera = camera.replace("-", "_")

    info = cleanup(input("Other info (card number, colour space, etc.): "))
    # info = info.replace(" ", "_")
    # info = info.replace("-", "_")

    # Give feedback to user
    print("")
    print(f"\nYou will be changing filenames in the folder: {directory}")
    print(
        f"\nYour new filenames will look like this: {project}_{date}_{camera}_{info}_<count>.<filetype>\n")
    print("")

    # Ask to proceed
    answer = input(
        "Are you sure everything above is correct? (yes/no): ")

    if re.match(r'^[Yy].*', answer):
        for filename in os.listdir(directory):
            # extract the prefix and suffix of the filename
            file_parts = filename.split('.')
            prefix = file_parts[0]
            suffix = file_parts[1]

            # If the prefix has underscores, replace with dashes
            prefix = prefix.replace("_", "-")

            # set destination, source, and rename file
            dst = f"{directory}/{project}_{date}_{camera}_{info}_{prefix}.{suffix}"
            src = f"{directory}/{filename}"
            os.rename(src, dst)
    else:
        print("Nothing changed, exiting the program.")
        exit()

    print("Done!")

if __name__ == '__main__':
    main()
