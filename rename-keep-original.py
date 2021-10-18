import os
import re


def main():
    # Get information from user
    directory = input("File location: ")
    re.sub(r'\/$', '', directory)

    date = input("Date (yymmdd): ")
    if not re.match(r'\d{6}', date):
        print("Please enter the date as yymmdd.")
        exit()

    project = input("Project name: ")
    project = project.replace(" ", "")

    camera = input("Camera: ")
    camera = camera.replace(" ", "")

    card = input("Card number: ")
    card = card.replace(" ", "")

    # Give feedback to user
    print("")
    print(f"You will be changing filenames in the folder: {directory}")
    print(
        f"Your new filenames will look like this: {project}_{date}_{camera}_{card}_<count>.<filetype>")
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
            dst = f"{directory}/{project}_{date}_{camera}_{card}_{prefix}.{suffix}"
            src = f"{directory}/{filename}"
            os.rename(src, dst)
    else:
        print("Nothing changed, exiting the program.")
        exit()

    print("Done!")

if __name__ == '__main__':
    main()
