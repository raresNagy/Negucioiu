import matplotlib.pyplot as plt
import numpy as np

T = float(input("T(s) = "))
A = float(input("A = "))
t = np.arange(0, T, 0.1)

w = 2 * np.pi / T;
y = A * np.sin(w*t)
v = w * A * np.cos(w * t)
a = -w**2 * A * np.sin(w * t)

plt.xlabel('Timp (s)')
plt.ylabel('y')

plt.plot(t, y, label = "Distanță", color = "blue")
plt.plot(t, v, label = "Viteză", color = "red")
plt.plot(t, a, label = "Accelerație", color = 'green')

plt.title('Miscarea oscilatorie armonica')
# showing legend
plt.legend()

plt.show()
