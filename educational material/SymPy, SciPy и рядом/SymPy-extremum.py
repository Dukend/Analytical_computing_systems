import sympy
from sympy import symbols, diff, solve, integrate


# стр. 196 книжки "Введение в научный Python"

# Вначале определим экстремальные точки функции, приравняв нулю ее
# производные. Затем вычислим значения вторых производных в экстремальных
# точках.
x = symbols('x')
f = x**3 - 2*x**2 + x
f1 = diff(f, x) # f.diff(x)
print("f1 = ", f1)
sols = solve(f1, x)
print(sols)  # [1/3, 1]
res = diff(f1, x).subs({x : sols[0]})
print(res)  # -2
res = diff(f1, x).subs({x : sols[1]})
print(res)  # 2
# В точке 1/3 вторая производная отрицательна, а это означает, что это точка
# максимума. Т.о. локальный максимум равен
res = f.subs({x : sols[0]})
print(res)  # 4/27
print(res)
# Если первообразную не удалось найти, то возвращается невычисляемый
# объект Integral.
res = integrate(x**x, x)
print(res)  # Integral(x**x, x)
# Для вычисления определенного интеграла в функцию integrate() вторым
# аргументом нужно передать кортеж вида (var,lower_limit,upper_limit)
