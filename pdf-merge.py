import os
import re
from PyPDF2 import PdfFileMerger

def check_suffix(filename):
    if not re.match(r'\.pdf$', filename):
        return '.'.join([filename, 'pdf'])
    return filename


def merge(files, output):
    merger = PdfFileMerger()

    for pdf in files:
        merger.append(pdf)

    merger.write(output)
    merger.close()


def path_check(path):
    if not os.path.exists(path):
        # directory does not exist
        print(f'The directory {path} does not exist!')
        exit()


def main():
    '''
    Merge pdf files
    '''
    print('This program merges pdf files from a directory')
    source_dir = input('\nLocation of pdf files:\n')
    output_dir = input('\nWhere do you want to save the file?\n')
    merged_file = input('\nWhat do you want to call the merged file?\n')
    
    # remove end backslash, if existing on paths
    re.sub(r'\/$', '', source_dir)
    re.sub(r'\/$', '', output_dir)

    # check if paths are valid
    path_check(source_dir)
    path_check(output_dir)

    # make sure merged_file has .pdf suffix
    merged_file = check_suffix(merged_file)

    # create output path
    output = os.path.join(output_dir, merged_file)

    # sort files in alphabetical order
    list_dir = os.listdir(source_dir)
    list_dir = [f.lower() for f in list_dir]
    sorted(list_dir)

    # create list of file paths
    file_paths = list()
    for file in list_dir:
        file_paths.append(os.path.join(source_dir, file))


    # merge files
    merge(file_paths, output)

    print(f'\nYour merged file is here:\n{output}')
    exit()

if __name__ == '__main__':
    main()