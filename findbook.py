import json

# функция чтения json-файла
def read_library() -> list:
    try:
        with open('library.json', 'r', encoding='utf-8') as file:
            books: list = json.load(file)
    except json.JSONDecodeError:
        books = []
    return books

# функция получения книг по названию 
def find_title() -> None:
    title: str = input("Введите название книги? ")
    books: list = read_library()
    found_books: list = []
    for book in books:
        if book['title'] == title:
            found_books.append(book)
    if found_books:
        for book in found_books:
            print(book)
    else:
        print("Книги с таким названием не найдено!")

# функция получения книг по автору
def find_author() -> None:
    author: str = input("Введите автора книги? ")
    books: list = read_library()
    found_books: list = []
    for book in books:
        if book['author'] == author:
            found_books.append(book)
    if found_books:
        for book in found_books:
            print(book)
    else:
        print("Книги с таким автором не найдено!")

# функция получения книг по году издания
def find_year() -> None:
    while True:
        try:
            year: int = int(input("Введите год издания(целым числом): "))
            break
        except ValueError:
            print("Ошибка: Пожалуйста, введите целое число.")
    books: list = read_library()
    found_books: list = []
    for book in books:
        if book['year'] == year:
            found_books.append(book)
    if found_books:
        for book in found_books:
            print(book)
    else:
        print("Книги с таким годом издания не найдено!")
