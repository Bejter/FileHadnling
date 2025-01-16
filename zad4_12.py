import csv

def read_books_from_csv(filename):
    books = []
    with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader, None)
        for row in reader:
            books.append(row) 
    return books

def filter_books_by_genre(books, genre):
    filtered_books = []
    for book in books:
        if book[2].lower() == genre.lower(): 
            filtered_books.append(book)
    return filtered_books

def save_books_to_file(books, genre):
    filename = f'books_{genre.lower()}.txt'
    with open(filename, 'w', encoding='utf-8') as f:
        for book in books:
            f.write(f"{book[0]}, {book[1]}, {book[2]}, {book[3]}\n")

def main():
    genre_to_filename = {
        'Fantasy': 'books_fantasy.txt',
        'Historical': 'books_historical.txt',
        'Romance': 'books_romance.txt',
        'Classic': 'books_classic.txt'
    }

    books = read_books_from_csv('books.csv')

    for genre, filename in genre_to_filename.items():
        filtered_books = filter_books_by_genre(books, genre)

        save_books_to_file(filtered_books, genre)
        print(f"Books from the genre '{genre}' have been saved to {filename}")

if __name__ == "__main__":
    main()
