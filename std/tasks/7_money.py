# Пока бухгалтер считала среднюю зарплату сотрудников,
# ей стало интересно, а не зря ли она работает столько времени на одном месте?
# Ей захотелось узнать, увеличивается ли её зарплата с каждым месяцем или нет.

# Пользователь вводит 10 чисел.
# Напишите программу, которая проверяет, упорядочены ли они по возрастанию.

cash_first = int(input("Введите зарплату: "))

for array in range (9):
  cash = int(input("Введите зарплату: "))
  if cash > cash_first:
    if array == 8: 
      print('Зарплата растет')
    cash = cash_first
    continue
  else:
    print("Зарплата не увеличивается")
    break