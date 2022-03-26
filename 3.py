import sys
import time
from abc import ABC, abstractmethod
t_start = time.perf_counter()


class Basic(ABC):
    @abstractmethod
    def first(self):
        print('____Шахматы____')

class Advanced(Basic):
    def first(self):
        super().first()
        print('Ход Ладьи')

Proverka_arr = 'ABCDEFGH123456789'

a = Advanced()
a.first()
print('Выберите изначальную позицию Ладьи. Сначала буква, потом цифра (с новой строки).')
dano = []
for i in range(2):
    var = input()
    if (var not in Proverka_arr):
        while (var not in Proverka_arr): # Прооверка на правильный ввод
            print('Попробуйте ещё раз (1-2): ', end = ' ')
            var = input()
    dano.append(var)



class Chess(ABC):
    def draw(self):
        print("Изначальная позиция", "".join(dano))
    @abstractmethod
    def move(self):
        pass

class rook(Chess):
    def move(self):
        print("Функционал Ладьи")

a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
class St_rook():
    def __init__(self, right, left, up, down, count):
        self.right = right
        self.left = left
        if (str(up) in a):
            self.up = up
        else:
            self.up = dano[0]
            self.count = dano[1]

        if (str(down) in a):
            self.down = down
        else:
            self.down = dano[0]
            self.count = dano[1]

        if (1 <= int(count) <= 8):
            self.count = count
        else:
            self.count = dano[1] # Остается на месте



Step = rook()
Step.draw()
Step.move()
class R_right(St_rook):
    def display_wow(self):
        print('Ход {}{}.'.format(self.right, self.count))
        dano[1] = self.count

class R_left(St_rook):
    def display_wow(self):
        print('Ход {}{}.'.format(self.left, self.count))
        dano[1] = self.count

class R_up(St_rook):
    def display_wow(self):
        print('Ход {}{}.'.format(self.up, self.count))
        dano[0] = self.up
        dano[1] = self.count

class R_down(St_rook):
    def display_wow(self):
        print('Ход {}{}.'.format(self.down, self.count))
        dano[0] = self.down
        dano[1] = self.count

print('Ход по правой стороне (введите число)')
res_1 = R_right(dano[0], '0', '0', '0', str(input()))
res_1.display_wow()
print()

print('Ход по левой стороне (введите число)')
res_1 = R_left('0', dano[0], '0', '0', str(input()))
res_1.display_wow()
print()

print('Ход вверх (введите букву (A-H) и число)')
res_1 = R_up('0', '0', str(input()), '0', str(input()))
res_1.display_wow()
print()

print('Ход вниз (введите букву (A-H) и число)')
res_1 = R_down('0', '0', '0', str(input()), str(input()))
res_1.display_wow()
print()

print('Конечная точка', "".(dano)))
print('Время окончания:', time.perf_counter() - t_start)
