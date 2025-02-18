import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return x ** 2 - 3.2 * x - 1

def f_prime(x):
    return 2 * x - 3.2

def newton_method(x0, tolerance=1e-7, max_iterations=100):
    x_n = x0
    for i in range(max_iterations):
        f_x_n = f(x_n)
        f_prime_x_n = f_prime(x_n)


        if f_prime_x_n == 0:
            print("Производная равна нулю, метод не сработает.")
            return None


        x_n1 = x_n - f_x_n / f_prime_x_n


        if abs(x_n1 - x_n) < tolerance:
            return x_n1

        x_n = x_n1
    print("Достигнуто максимальное количество итераций.")
    return x_n


initial_guess = 0


root = newton_method(initial_guess)


x = np.linspace(-1, 5, 400)
y = f(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y, label='f(x) = x^2 - 3.2x - 1', color='blue')
plt.axhline(0, color='red', lw=0.5, ls='--')
plt.scatter(root, f(root), color='green', zorder=5)
plt.text(root, f(root), f'  корень: x = {root:.4f}', color='green')
plt.title('График функции с найденным корнем')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.legend()
plt.axvline(root, color='green', ls='--', lw=0.8)
plt.show()

print(f"Найденный корень: x = {root:.6f}")
