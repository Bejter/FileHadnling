def counter(file_path):
    try:
        total_lines = 0
        total_words = 0
        total_characters = 0
        with open(file_path) as file:
            for line in file:
                total_lines += 1
                total_characters += len(line)
                total_words += len(line.split())
        print(f'File name: {file_path}')
        print(f'Number of lines: {total_lines}')
        print(f'Number of words: {total_words}')
        print(f'Number of character: {total_characters}')
    except FileNotFoundError:
        print(f'File {file_path} was not found')

file_path = input('Enter file name: ')
counter(file_path)