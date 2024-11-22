import json
from book import Book
from findbook import read_library, find_title, find_author, find_year


def show_all_books() -> None:
    books: list = read_library()
    if books:
        print("Список книг")
        for book in books:
            print(book)
    else:
        print("Книг не найдено")


# функция добавления книги
def add_book() -> None:
    print("Добавление книги")
    books: list = read_library()
    if books:
        id: int = books[-1]['id'] + 1
    else:
        id = 1
    title: str = input("Введите название: ")
    author: str = input("Введите автора: ")
    while True:
        try:
            year: int = int(input("Введите год издания(целым положительным числом): "))
            if year <= 0:
                print("Ошибка: Год должен быть больше нуля")
            else:
                break  
        except ValueError:
            print("Ошибка: Пожалуйста, введите целое число.")
    
    status: str = "В наличии"
    book: Book = Book(id, title, author, year, status)

    # Добавляем новую книгу в список
    books.append(book.to_dict())
    
    # Сохраняем список в файл
    with open('library.json', 'w', encoding='utf-8') as file:
        json.dump(books, file, ensure_ascii=False, indent=4)
        print("Книга добавлена")


def find_book():
    while True:
        print("Поиск книги")
        print("Выберете по какому свойству книги будем искать:")
        print("1. По названию")
        print("2. По автору")
        print("3. По году издания")
        print("0. Выход")
        operation: str = input("? ")
        match operation:
            case "1":
                find_title()
            case "2":
                find_author()
            case "3":
                find_year()
            case "0":
                break
            case _:
                print("Нет такого свойства")


def update_status() -> None:
    print("Изменение статуса книги")
    while True:
        try:
            id: int = int(input("Введите id книги(целым числом): "))
            break
        except ValueError:
            print("Ошибка: Пожалуйста, введите целое число.")
    books: list = read_library()
    for book in books:
        if book['id'] == id:
            status: str = input("Введите статус? ")
            new_book_data: dict = {
                "id": id,
                "title": book['title'],
                "author": book['author'],
                "year": book['year'],
                "status": status
            }
            book.update(new_book_data)
            with open('library.json', 'w', encoding='utf-8') as file:
                json.dump(books, file, ensure_ascii=False, indent=4)
                print(f"У книги с id = {id} изменен статус")
                print(book)
            return
    print("Книги с таким id не найдено")
    return


def delete_book():
    print("Удаление книги")
    while True:
        try:
            id: int = int(input("Введите id книги(целым числом): "))
            break
        except ValueError:
            print("Ошибка: Пожалуйста, введите целое число.")
    books: list = read_library()
    for book in books:
        if book['id'] == id:
            books_after_deletion = [book for book in books if book['id'] != id]
            with open('library.json', 'w', encoding='utf-8') as file:
                json.dump(books_after_deletion, file, ensure_ascii=False, indent=4)
                print(f"Книга с id = {id} удалена!")
            return
    print("Книги с таким id не найдено")
    return


# главная функция
def main():
    print("Добро пожаловать в систему управления библиотекой!")
    while True:
        print("Какую операцию хотите выполнить:")
        print("1. Список всех книг")
        print("2. Добавление книги")
        print("3. Изменение статуса книги")
        print("4. Поиск книги")
        print("5. Удаление книги")
        print("0. Выход")
        operation: str = input("? ")
        match operation:
            case "1":
                show_all_books()
            case "2":
                add_book()
            case "3":
                update_status()
            case "4":
                find_book()
            case "5":
                delete_book()
            case "0":
                print("До свидания!")
                break
            case _:
                print("Нет такой операции")


if __name__ == "__main__":
    main()
