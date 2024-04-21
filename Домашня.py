# Завдання 3
# Дано три вежі та n дисків різного розміру, відсортованих
# за зростанням, розміщених на першій вежі у вигляді піраміди.
# Потрібно перемістити всі диски на третю вежу,
# використовуючи проміжну вежу, за умови, що можна
# переміщати тільки один диск за раз та диск завжди можна
# покласти лише на диск більшого розміру або на порожню
# вежу.
# Ця задача може бути вирішена за допомогою
# рекурсивного алгоритму, використовуючи стек для
# зберігання проміжних ходів при переміщенні дисків між
# вежами.

class TowerOfHanoi:
    def __init__(self, n):
        self.n = n
        self.towers = [[i for i in range(n, 0, -1)], [], []]
        self.moves = []

    def move_disk(self, source, target):
        disk = self.towers[source].pop()
        self.towers[target].append(disk)
        self.moves.append((source, target))

    def solve(self, n, source, target, auxiliary):
        if n == 1:
            self.move_disk(source, target)
        else:
            self.solve(n-1, source, auxiliary, target)
            self.move_disk(source, target)
            self.solve(n-1, auxiliary, target, source)

    def display_moves(self):
        for move in self.moves:
            print(f"Перемістити диск з вежі {move[0]+1} на вежу {move[1]+1}")

n = 3
tower_of_hanoi = TowerOfHanoi(n)
tower_of_hanoi.solve(n, 0, 2, 1)
tower_of_hanoi.display_moves()
