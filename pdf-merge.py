import os
import re
from PyPDF2 import PdfFileMerger

def check_suffix(filename):
    '''
    Check output file for .pdf suffix.
    Add suffix if not existing.
    '''
    if not re.match(r'\.pdf$', filename):
        return '.'.join([filename, 'pdf'])
    return filename


def merge(files, output):
    '''
    Merge and write the files
    '''
    merger = PdfFileMerger()

    for pdf in files:
        merger.append(pdf)

    merger.write(output)
    merger.close()


def path_check(path):
    '''
    Check if file path exists
    '''
    if os.path.exists(path):
        return True
    
    # directory does not exist
    print(f'The directory {path} does not exist!')
    return False


def remove_slash(path):
    '''
    Remove slash at the end of path
    '''
    return re.sub(r'\/$', '', path)


def main():
    '''
    Merge pdf files
    '''
    print('This program merges pdf files from a directory')
    
    while True:
        source_dir = input('\nLocation of pdf files:\n')
        source_dir = remove_slash(source_dir)
        if path_check(source_dir):
            # path valid
            break

    while True:
        output_dir = input('\nWhere do you want to save the file?\n')
        output_dir = remove_slash(output_dir)
        if path_check(output_dir):
            # path valid
            break

    merged_file = input('\nWhat do you want to call the merged file?\n')
    
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