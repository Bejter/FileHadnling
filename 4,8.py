import re

def four_char_extension(file_path):
    try:    
        with open(file_path) as file:
            files = []
            for line in file:
                matches = re.findall(pattern, line)
                files.extend(matches)
        print('Found extensions: ')
        for x in files:
            print(x)
    except FileNotFoundError:
        print(f'File {file_path} was not found')

pattern = r'\b\w+\.\w{4}\b'
file_path = 'files.txt'
four_char_extension(file_path)