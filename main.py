import json
from book import Book


def read_library() -> list:
    # Если файл не существует, создаем пустой список книг
    try:
        with open('library.json', 'r', encoding='utf-8') as file:
            books = json.load(file)
    except json.JSONDecodeError:
        books = []
    return books


def show_all_books() -> None:
    books = read_library()
    for book in books:
        print(book)


# функция добавления книги
def add_book() -> None:
    books = read_library()
    id: int = books[-1]['id'] + 1    
    title: str = input("Введите название: ")
    author: str = input("Введите автора: ")
    while True:
        try:
            year = int(input("Введите год (целым числом): "))
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


# главная функция
def main():
    while True:
        print("Какую операцию хотите выполнить:")
        print("1. Отображение всех книг")
        print("2. Добавление книги")
        print("3. Изменение статуса книги")
        print("4. Поиск книги")
        print("5. Удаление книги")
        print("0. Выход")
        oper: str = input("? ")
        match oper:
            case "1":
                show_all_books()
            case "2":
                add_book()
            case "3":
                pass
            case "4":
                pass
            case "5":
                pass
            case "0":
                break
            case _:
                print("Нет такой операции")


if __name__ == "__main__":
    main()
