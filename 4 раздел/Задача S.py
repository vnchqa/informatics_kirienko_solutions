# Дано натуральное число n. Выведите в порядке возрастания# все трехзначные числа, сумма цифр которых равна n.

n = int(input())

for i in range(100, 1000):
    if n == (i // 100) + (i % 100 // 10) + (i % 10):
        print(i, ' ')
