# Переставьте соседние элементы списка (A[0] c A[1],# A[2] c A[3] и т.д.).# Если элементов нечетное число, то последний элемент остается на своем месте.

l = list(map(int, input().split()))


for i in range(0, len(l), 2):
    # берём значения от i до i + 2 и присваиваем им значения наоборот
    l[i:i+2] = l[i:i+2][::-1]

for i in range(len(l)):
    print(l[i], end=' ')
