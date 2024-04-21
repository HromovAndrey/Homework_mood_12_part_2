# Завдання 2
# Змініть стек із першого завдання таким чином, щоб його
# розмір був нефіксованим.
class StringStack:
    def __init__(self):
        self.stack = []

    def push(self, string):
        self.stack.append(string)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            print("Стек порожній")
            return None

    def count(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0

    def clear(self):
        self.stack.clear()

    def peek(self):
        if self.stack:
            return self.stack[-1]
        else:
            print("Стек порожній")
            return None

def display_menu():
    print("Меню:")
    print("1. Розмістити рядок у стек")
    print("2. Виштовхнути рядок зі стеку")
    print("3. Підрахунок кількості рядків у стеку")
    print("4. Перевірка, чи порожній стек")
    print("5. Очищення стеку")
    print("6. Отримання значення без виштовхування верхнього рядка зі стеку")
    print("0. Вихід")

stack = StringStack()

while True:
    display_menu()
    choice = input("Оберіть операцію: ")

    if choice == '1':
        string = input("Введіть рядок для розміщення у стеку: ")
        stack.push(string)
    elif choice == '2':
        popped_string = stack.pop()
        if popped_string is not None:
            print("Виштовхнуто рядок:", popped_string)
    elif choice == '3':
        print("Кількість рядків у стеку:", stack.count())
    elif choice == '4':
        print("Стек порожній:", stack.is_empty())
    elif choice == '5':
        stack.clear()
        print("Стек очищено")
    elif choice == '6':
        top_string = stack.peek()
        if top_string is not None:
            print("Верхній рядок у стеку:", top_string)
    elif choice == '0':
        print("Дякую за користування! Завершення програми.")
        break
    else:
        print("Некоректний вибір. Спробуйте ще раз.")
