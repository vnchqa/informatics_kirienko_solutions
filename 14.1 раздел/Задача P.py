# В этой задаче нужно придумать генератор — однострочное выражение на языке Python, результатом вычисления которого будет двумерный массив (список вложенных списков), заполненный по некоторому правилу.
# 



[[2 if i > j else 1 if j > i else 0 for j in range(m)] for i in range(n)]