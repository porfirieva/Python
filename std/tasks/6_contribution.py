# Вклад в банке составляет X рублей.
# Ежегодно он увеличивается на P процентов,
# после чего дробная часть копеек отбрасывается.

# Определите, через сколько лет вклад составит не менее Y рублей.

# Напишите программу,
# которая по данным числам X, Y, P определяет,
# сколько лет пройдёт, прежде чем сумма достигнет значения Y.
x = int(input('Введите сумму вклада: '))
p = int(input('Введите процент: '))
y = int(input('Введите необходимую сумму: '))
year = 0

while x < y:
  x *= 1 + p / 100
  year += 1
print('Понадобится ', year, 'лет')