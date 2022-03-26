import sys
import time
import random
from abc import ABC, abstractmethod
from random import randint
t_start = time.perf_counter()


print('Бой борцов')
print()
health = 100
class Basic(ABC):
    @abstractmethod
    def first(self):
        print("Начало боя.")

class Advanced(Basic):
    def first(self):
        super().first()
        print("Здоровье каждого бойца: 100")

a = Advanced()
a.first()
health_1 = health_2 = 100
class fight():
    def __init__(self, health_1, health_2):
        self.health_1 = health_1
        self.health_2 = health_2



class Fighter_1(fight):
    def display_wow(self):
        if (int(self.health_1) >= 0):
            print('А. Атаковал второй боец. Осталось здоровья у первого бойца: {}'.format(self.health_1))
        else:
            print('Победил второй боец!')
            print()
            print('Время окончания:', time.perf_counter() - t_start)
            sys.exit()


class Fighter_2(fight):
    def display_wow(self):
        if (int(self.health_2) >= 0):
            print('B. Атаковал первый боец. Осталось здоровья у второго бойца: {}'.format(self.health_2))
        else:
            print('Победил первый боец!')
            print()
            print('Время окончания:', time.perf_counter() - t_start)
            sys.exit()


a = ['A', 'B']
while (health_1 != 0) or (health_2 != 0):
    res = random.choice(a)
    if (res == 'A'):
        health_1 -= 20
        res_1 = Fighter_1(health_1, health_2)
        res_1.display_wow()
    if (res == 'B'):
        health_2 -= 20
        res_2 = Fighter_2(health_1, health_2)
        res_2.display_wow()
