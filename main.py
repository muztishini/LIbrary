import json


class Book:
    def __init__(self, id: int, title: str, author: str, year: int, status: str) -> None:
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status
        }


# функция добавления книги
def add_book() -> None:
    id: int = int(input("Введите id: "))
    title: str = input("Введите название: ")
    author: str = input("Введите автора: ")
    year: int = int(input("Введите год издания: "))
    status: str = input("Введите статус: ")
    book: Book = Book(id, title, author, year, status)
    # Если файл не существует, создаем пустой список книг
    try:
        with open('library.json', 'r', encoding='utf-8') as file:
            books = json.load(file)
    except json.JSONDecodeError:
        books = []

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
                pass
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
