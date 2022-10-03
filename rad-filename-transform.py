import os
import re
import sys


def clean_day(day):
    try:
        p = re.compile('day')
        new_day, n = p.subn('', day)
        return int(new_day)
    except:
        # print('Day must contain a number')
        sys.exit('Day must contain a number')


def clean_set(set):
    try:
        p = re.compile('^0')
        new_set, n = p.subn('', set)
        return int(new_set)
    except:
        # print('Set must be a number')
        sys.exit('Set must be a number')


def fileparts(file):
    """Split filename into prefix and suffix"""
    parts = file.split('.')
    prefix = parts[0]
    suffix = parts[1].lower()
    return prefix, suffix


def split_prefix(prefix):
    # Get relevant prefix parts
    parts = prefix.split('_')
    id = parts[2]
    day = parts[3]
    set = parts[4]

    # Clean up the parts
    day = clean_day(day)
    set = clean_set(set)

    return id, day, set


def main():
    """Transform CISCA filenames into RAD filnames"""
    # Get directory from user
    while True:
        directory = input('\nFile directory:\n')
        if os.path.exists(directory):
            break
        print('\nDirectory does not exist!')

    list_dir = os.listdir(directory)
    for file in list_dir:
        # Get the relevant parts from the filenames
        prefix, suffix = fileparts(file)
        id, day, set = split_prefix(prefix)
        
        # rename file
        dst = f"{directory}/{id} - D{day} - {set}.{suffix}"
        src = f"{directory}/{file}"
        os.rename(src, dst)

    print("\nDone!")


if __name__ == '__main__':
    main()