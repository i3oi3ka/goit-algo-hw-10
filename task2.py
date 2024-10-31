import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi
import random

a = 0  # Нижня межа
b = 3  # Верхня межа
num_samples = 10000  # кількість випадкових даних


# Визначення функції
def f(x):
    return x**2


def monte_carlo_integrall(num_samples, a, b):
    inside = 0
    x_inside, y_inside = [], []
    x_outside, y_outside = [], []

    # 2. Генерація випадкових вхідних даних
    for _ in range(num_samples):
        x = random.uniform(a, b)
        y = random.uniform(f(a), f(b))

        # 3. Виконання обчислень
        if y <= f(x):
            inside += 1
            x_inside.append(x)
            y_inside.append(y)
        else:
            x_outside.append(x)
            y_outside.append(y)

    # 4. Агрегування та аналіз результатів
    result = (b - a) * (f(b) - f(a)) * inside / num_samples
    return result, x_inside, y_inside, x_outside, y_outside


# Створення діапазону значень для x
x = np.linspace(a - 0.5, b + 0.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, "r", linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color="gray", alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel("x")
ax.set_ylabel("f(x)")

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color="gray", linestyle="--")
ax.axvline(x=b, color="gray", linestyle="--")
ax.set_title("Графік інтегрування f(x) від " + str(a) + " до " + str(b))

# Обчислення інтеграла
result, error = spi.quad(f, a, b)
print("Інтеграл обчислений за допомогою бібліотеки scipy: ", result, error)

integrall, x_inside, y_inside, x_outside, y_outside = monte_carlo_integrall(
    num_samples, a, b
)
print(f"Інтеграл обчислений методом Монте-Карло: {integrall}")

# Додавання випадкових точок
plt.scatter(x_inside, y_inside, color="blue", s=1, label="Точки всередині")
plt.scatter(x_outside, y_outside, color="red", s=1, label="Точки поза межами")
plt.legend()

plt.grid()
plt.show()
