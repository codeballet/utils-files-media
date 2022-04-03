import os
import re


def main():
    # Get information from user
    directory = input("File location: ")
    re.sub(r'\/$', '', directory)

    date = input("Date (yymmdd): ")
    if not re.match(r'\d{6}', date):
        print("Please enter the date as yymmdd, using six digits.")
        exit()

    project = input("Project name: ")
    project = project.replace(" ", "_")
    project = project.replace("-", "_")

    camera = input("Camera: ")
    camera = camera.replace(" ", "_")
    camera = camera.replace("-", "_")

    info = input("Other information (i.e. card number, colour space, etc.): ")
    info = info.replace(" ", "_")
    info = info.replace("-", "_")

    # Give feedback to user
    print("")
    print(f"You will be changing filenames in the folder: {directory}")
    print(
        f"Your new filenames will look like this: {project}_{date}_{camera}_{info}_<count>.<filetype>")
    print("")

    # Ask to proceed
    answer = input(
        "Are you sure everything above is correct? (yes/no): ")

    if re.match(r'^[Yy].*', answer):
        for count, filename in enumerate(os.listdir(directory)):
            # extract the prefix and suffix of the filename
            file_parts = filename.split('.')
            #prefix = file_parts[0]
            suffix = file_parts[1]

            # If the prefix has underscores, replace with dashes
            #prefix = prefix.replace("_", "-")

            # set destination, source, and rename file
            dst = f"{directory}/{project}_{date}_{camera}_{info}_{count:04d}.{suffix}"
            src = f"{directory}/{filename}"
            os.rename(src, dst)
    else:
        print("Nothing changed, exiting the program.")
        exit()

    print("Done!")


if __name__ == '__main__':
    main()
