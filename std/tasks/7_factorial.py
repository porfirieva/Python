# Мы всё ближе и ближе подбираемся к серьёзной математике.
# Одна из классических задач - задача на нахождение факториала числа.
# И в будущем мы с ней ещё встретимся.
# 
# Дано натуральное число N. Напишите программу, которая находит N! (N факториал)
# 
# Запись N! означает следующее:
# 
# N! = 1 * 2 * 3 * 4 * 5 * … * N
# 
# Пример:
# 
# Введите число: 5
# Факториал числа 5 равен 120
users_number = int(input('Введите число: '))

summ = 1

for numbers in range (1, users_number + 1):
  summ *= numbers
print ('Факториал числа', users_number, 'равен', summ)