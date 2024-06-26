person = {
    "id": 1,
    "last_name": "А.",
    "first_name": "Анна",
    "group": "ІПЗс-22-2",
    "course": 2,
    "books_in_use": [],
    "books_statistics": [],
}


def show_person():
    print("ID", person["id"])
    print("Прізвище", person["last_name"])
    print("Ім'я", person["first_name"])
    print("Група", person["group"])
    print("Курс", person["course"])

    if person["books_in_use"]:
        print("Книги в використанні:", ", ".join(person["books_in_use"]))
    else:
        print("Читач не брав книги в використання")

    if person["books_statistics"]:
        print("Статистика книг:", ", ".join(person["books_statistics"]))
    else:
        print("Немає статистики книг")


show_person()
while True:
    print("1. Видати картку читача")
    print("2. Взяти книгу")
    print("3. Повернути книгу")
    print("0. Вихід")

    choice = int(input("Виберіть дію: "))

    if choice == 1:
        show_person()
    elif choice == 2:
        book = input("Введіть назву книги: ")
        if book in person["books_in_use"]:
            print("В читача є книга з таким іменем")
        else:
            person["books_in_use"].append(book)
    elif choice == 3:
        if person["books_in_use"]:
            print("Книги в використанні:", ", ".join(person["books_in_use"]))
            book = input("Введіть назву книги: ")
            if book in person["books_in_use"]:
                person["books_in_use"].remove(book)
                person["books_statistics"].append(book)
            else:
                print("В читача немає книги з таким іменем")
        else:
            print("У читача немає книг у використанні")
    elif choice == 0:
        break
