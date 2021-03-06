from sympy import *


# стр. 197

# Для символьного интегрирования предназначена функция
# integrate(...). С ее помощью можно вычислять как определенные, так и
# неопределенные интегралы. Первым аргументом она принимает символьное
# выражение, которое будет интегрироваться, вторым – переменную
# интегрирования или кортеж, состоящий из имени переменной и ее нижнего и
# верхнего предела. Если второй аргумент – имя, то вычисляется
# неопределенный интеграл, т.е. первообразная подынтегральной функции.
x, y, a, b = symbols('x y a b')
res = integrate(1/x, x)
print(res)  # log(x)
res = integrate(cos(x)**2, x)
print(res)  # x/2 + sin(x)*cos(x)/2
res = integrate(log(x), x)
print(res)  # x*log(x) – x
# Проверим результат дифференцированием.
res = res.diff(x)
print(res)  # log(x)
# Обратите внимание, что SymPy не включает в результат постоянную
# интегрирования. Вы можете добавить константу самостоятельно, или можете
# сформулировать задачу как решение соответствующего дифференциального
# уравнения (ОДУ). Во втором случае произвольная постоянная будет
# включаться в результат.

# определенный интеграл
res = integrate(exp(-x), (x, 0, oo))
print(res)

# повторный интеграл
res = integrate(x*y, (x, 0, 1), (y, 0, 1))
print(res)
# У integrate()есть невычисляемый эквивалент – функция Integral(). Она
# возвращает объект типа 'sympy.integrals.integrals.Integral'. Чтобы
# потом вычислить интеграл, нужно использовать метод doit().
expr = Integral(log(x)**2, x)
print(expr)  # Integral(log(x)**2, x)
res = expr.doit()
print(res)  # x*log(x)**2 - 2*x*log(x) + 2*x
