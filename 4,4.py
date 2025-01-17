def display_csv_in_chunks(file_path, chunk_size = 5):
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            chunk = []
            for line in file:
                chunk.append(line)
                if len(chunk) == chunk_size:
                    for row in chunk:
                        print(row)
                    input('Press Enter key to continue...')
                    chunk = []
            if chunk:
                for row in chunk:
                    print(row)
    except FileNotFoundError:
        print(f'File {file_path} was not found')

file_name = 'it_company.csv'

display_csv_in_chunks(file_name)