import os
import re
list_file = []
for folders, subfolders, files in os.walk(os.getcwd()):
    if not folders == os.getcwd():
        for file in files:
            list_file.append(folders + '\\' + file)
pattern = r'https://[-?_=./\w]+'
for file in list_file:
    text = open(file, 'r')
    text_content = text.read()
    match = re.search(pattern, text_content)
    if match:
        count = match.start()
        while True:
            print(text_content[count], end='')
            if text_content[count] == ' ':
                break
            count += 1
        print()
    text.close()