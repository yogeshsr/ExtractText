import os
from os import listdir
from os.path import isfile, join
import PyPDF2
import re


dir_path = os.path.dirname(os.path.realpath(__file__))
input_dir = join(dir_path, 'input')

PATTERN = 'INCIDENT .+'

def print_matching_pattern(file_name):
    global PATTERN  

    pdf = open(file_name, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdf)
    pageObj = pdfReader.getPage(0)
    try:
        title_text=re.search(PATTERN, pageObj.extractText()).group(0)
        print(title_text)
    except:
        print("Failed to read file: " + file_name)
if __name__ == '__main__':
    onlyfiles = [join(input_dir, f) for f in listdir(input_dir) if f.endswith('pdf') and isfile(join(input_dir, f))]
    list(map(lambda f: print_matching_pattern(f), onlyfiles))
    print('Extracting text done!')