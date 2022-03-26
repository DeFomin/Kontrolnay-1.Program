import sys
import time
from abc import ABC, abstractmethod
t_start = time.perf_counter()

class Basic(ABC):
    @abstractmethod
    def first(self):
        print('Bank')

class Advanced(Basic):
    def first(self):
        super().first()
        print('________Калькульятор вкладов________')

a = Advanced()
a.first()

a = ['Срочный вклад (1)', 'Вклад с капитализацией процентов (2)']
Proverka_arr = ['1', '2', '3']

print('Введите сумму, которую хотите вложить: ')
s = int(input())

if (s < 15000):
    print('Введите номер варианта вклада, который вас интересует (1-2)')
    print("; ".join(a))
    var = input()
    if (var not in Proverka_arr):
        while (var not in Proverka_arr): # Прооверка на правильный ввод
            print('Попробуйте ещё раз (1-2): ', end = ' ')
            var = input()
else:
    var = '3'

class bank():
    def __init__(self, summa, percent, time):
        self.summa = summa
        if 1 <= int(percent) <= 100:
            self.percent = percent
        else:
            self.percent = 'Не определен'
            sys.exit()
        self.time = time
    def __private(self):
        print("Это приватный метод! Деньги не вернем.")

if (var == '1'):
    class easy(bank):
        def display_wow(self):
            print('Вклад размером: {}. Процент: {}%. Время {} месяц(-a/-ев)'.format(self.summa, self.percent, self.time))
            answer = int(self.summa)*(int(self.time)*0.05 + 1)
            print('Итоговая сумма:', round(answer, 2))

    print('Выбран срочный вклад, введите срок')
    res_1 = easy(s, '5', str(input()))
    res_1.display_wow()


if (var == '2'):
    class cap(bank):
        def setSumma(self):
            self.summa = summa
        def setTime(self):
            self.time = time
        def display_wow(self):
            print('Вклад размером: {}. Процент: {}%. Время {} месяц(-a/-ев)'.format(self.summa, self.percent, self.time))
            answer = int(self.summa)*(int(self.percent)/100 + 1)**int(self.time)
            print('Итоговая сумма:', round(answer, 2))

    print('Выбран вклад с капитализацией процентов, введите срок')
    res_1 = cap(s, '12', str(input()))
    res_1.display_wow()


if (var == '3'):
    class bonus(bank):
        def display_wow(self):
            print('Вклад размером: {}. Процент: {}%. Время {} месяц(-a/-ев)'.format(self.summa, self.percent, self.time))
            answer = int(self.summa)*(int(self.time)*int(self.percent)/100 + 1)
            bonus = (answer - int(self.summa))*int(self.percent)/100
            print('Итоговая сумма (+ бонус):', round(answer, 2) + int(bonus), 'Бонус: ', int(bonus))

    print('Бонусный вклад. Введите срок')
    res_1 = bonus(s, '7', str(input()))
    res_1.display_wow()

print('Время окончания:', time.perf_counter() - t_start)
