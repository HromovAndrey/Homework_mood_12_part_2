# Завдання 1
# Реалізуйте клас стеку для роботи з рядками (стек рядків).
# Стек має бути фіксованого розміру. Реалізуйте набір операцій
# для роботи зі стеком:
# o розміщення рядка у стек;
# o виштовхування рядка зі стеку;
# o підрахунок кількості рядків у стеку;
# o перевірку, чи порожній стек;
# o перевірку, чи повний стек;
# o очищення стеку;
# o отримання значення без виштовхування
# верхнього рядка зі стеку.
# На старті додатка відобразіть меню, в якому користувач
# може вибрати необхідну операцію.
class StringStack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.stack = []

    def push(self, string):
        if len(self.stack) < self.max_size:
            self.stack.append(string)
        else:
            print("Стек повний")

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

    def is_full(self):
        return len(self.stack) == self.max_size

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
    print("5. Перевірка, чи повний стек")
    print("6. Очищення стеку")
    print("7. Отримання значення без виштовхування верхнього рядка зі стеку")
    print("0. Вихід")

stack_size = 5
stack = StringStack(stack_size)

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
        print("Стек повний:", stack.is_full())
    elif choice == '6':
        stack.clear()
        print("Стек очищено")
    elif choice == '7':
        top_string = stack.peek()
        if top_string is not None:
            print("Верхній рядок у стеку:", top_string)
    elif choice == '0':
        print("Дякую за користування! Завершення програми.")
        break
    else:
        print("Некоректний вибір. Спробуйте ще раз.")
