import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return np.log10(x) - np.cos(x)


def bisection_method(func, a, b, tol=1e-4, max_iterations=100):
    global c
    if func(a) * func(b) >= 0:
        print("Функция должна менять знак на интервале [a, b].")
        return None

    for iteration in range(max_iterations):
        c = (a + b) / 2
        if abs(func(c)) < tol:
            return round(c, 4)

        if func(a) * func(c) < 0:
            b = c
        else:
            a = c

    return round(c, 4)


x = np.linspace(0.1, 2, 100)
y = f(x)

plt.plot(x, y, label='f(x) = lg(x) - cos(x)', color='blue')
plt.axhline(0, color='black', lw=0.5, ls='--')
plt.axvline(0, color='black', lw=0.5, ls='--')
plt.title('График функции f(x) = lg(x) - cos(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid()
plt.show()


a, b = 0.1, 2


root = bisection_method(f, a, b)
if root is not None:
    print(f"Приблизительный корень уравнения lg(x) - cos(x) = 0: {root}")