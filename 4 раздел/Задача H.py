# Напишите программу, которая по данному числу n от 1 до 9 выводит на экран n пингвинов. Изображение одного пингвина# имеет размер 5×9 символов, между двумя соседними пингвинами также имеется пустой (из пробелов) столбец. Разрешается# вывести пустой столбец после последнего пингвина. Для упрощения рисования скопируйте пингвина из примера в среду# разработки.# #    

n = int(input())

a = "   _~_    "
b = "  (o o)   "
c = " /  V  \\  "
d = "/(  _  )\\ "
e = "  ^^ ^^   "


print(n * a)
print(n * b)
print(n * c)
print(n * d)
print(n * e)
