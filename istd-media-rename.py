from copy import deepcopy
import os
import re


# list of existing syllabi
syllabi = ['ci', 'c', 'a1']


def cleanup(text):
    """
    Clean up the text
    """
    # preprocess text
    text = text.replace("__", "_ôçô_")
    text = text.replace("_", " ")

    # clean
    words = text.split(" ")
    clean_words = []
    for word in words:
        # only keep alphanumeric characters
        letters = []
        for letter in word:
            if re.match(r'[a-zA-Z0-9]', letter):
                letters.append(letter)
        clean_word = ''.join(letters)
        
        # only add words containing letters
        if len(clean_word) > 0:
            clean_words.append(clean_word)

        # replace 'ôçô' artefacts
        if word == "ôçô":
            clean_words.append("-")

        # replace '&' artefacts
        if word == "&":
            clean_words.append("and")

    clean_text = '_'.join(clean_words)

    # remove hyphens
    clean_text = clean_text.replace("-", "")

    return clean_text


def fileparts(filename):
    """Split filename in prefix and suffix"""
    parts = filename.split('.')
    suffix = parts[-1].lower()
    parts.pop(-1)

    draft_prefix = ' '.join(parts).lower()
    prefix = cleanup(draft_prefix)

    return(prefix, suffix)


def standardize(text):
    """Standardize the numbering of files"""
    # get the digits first in the filename
    num = int(text.split('_')[0])
    return re.sub(r'^\d+', f"{num:02d}", text, count=1)


def main():
    """Cleaning up and renaming ISTD files"""
    # get user input
    while True:
        # get directory
        directory = input('\nDirectory of files:\n')
        # remove end /, if existing
        re.sub(r'\/$', '', directory)
        if os.path.exists(directory):
            break
        print('\nThat directory does not exist!')        

    while True:
        # get syllabus
        syllabus = input('\nAbbreviation of syllabus: ')
        if syllabus in syllabi:
            break
        else:
            print('\nPlease enter one of the following syllabi:')
            for s in syllabi:
                print(f"  {s}")

    list_dir = os.listdir(directory)
    for file in list_dir:
        prefix, suffix = fileparts(file)
        prefix = standardize(prefix)

        # rename file  
        dst = f"{directory}/{syllabus}_{prefix}.{suffix}"
        src = f"{directory}/{file}"
        os.rename(src, dst)

    print("\nFiles renamed!")


if __name__ == '__main__':
    main()