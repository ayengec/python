import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1, 2, 20)
x
y = 5/np.sqrt(x**5)
y
y[17]
plt.plot(x, y, color='red', marker='o')
plt.show()