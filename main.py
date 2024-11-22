class Book:
    def __init__(self, id: int, title: str, author: str, year: int, status: str) -> None:
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def __str__(self) -> str:
        return {"id": self.id, "title": self.title, "author": self.author, "year": self.year, "status": self.status}


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
                pass
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
