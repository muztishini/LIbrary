import json


def read_library() -> list:
    try:
        with open('library.json', 'r', encoding='utf-8') as file:
            books: list = json.load(file)
    except json.JSONDecodeError:
        books = []
    return books


def find_title() -> None:
    title: str = input("Введите название книги? ")
    books: list = read_library()
    for book in books:
        if book['title'] == title:
            print(book)
            return
    print("Книги с таким названием не найдено!")


def find_author() -> None:
    author: str = input("Введите автора книги? ")
    books: list = read_library()
    for book in books:
        if book['author'] == author:
            print(book)
            return
    print("Книги с таким автором не найдено!")


def find_year() -> None:
    while True:
        try:
            year: int = int(input("Введите год издания(целым числом): "))
            break
        except ValueError:
            print("Ошибка: Пожалуйста, введите целое число.")
    books: list = read_library()
    for book in books:
        if book['year'] == year:
            print(book)
            return
    print("Книги с таким годом издания не найдено!")
