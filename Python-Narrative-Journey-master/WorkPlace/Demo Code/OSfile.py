import os
import shutil
import send2trash
import re

path = os.getcwd()


def walk():
    for folders, subfolders, files in os.walk('D:\\'):
        print("Currently looking at folder: " + folders)
        print('\n')
        print("THE SUBFOLDERS ARE: ")
        for sub_fold in subfolders:
            print("\t Subfolder: " + sub_fold)
        print("THE FILES ARE: ")
        for f in files:
            print("\t File: " + f)
        print('\n')


def find_txt():
    for folders, subfolders, files in os.walk('D:\\'):
        pattern = r'[\w]+.txt'
        for file in files:
            if re.search(pattern, file):
                print(file, end='\n')
                print(os.path.abspath(file))

find_txt()


