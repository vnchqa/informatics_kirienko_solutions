# В этой задаче нужно придумать генератор — однострочное выражение на языке Python, результатом вычисления которого будет двумерный массив (список вложенных списков), заполненный по некоторому правилу.
# 



[[0 if j % 2 == 1 and i %
  2 == 1 else 1 for j in range(m)] for i in range(n)]
