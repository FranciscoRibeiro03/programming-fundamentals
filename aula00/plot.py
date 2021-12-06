# Try running this program.
# Then change it to generate another subplot with the product of y1 and y2.

import numpy as np
import matplotlib.pyplot as plt

plt.figure(1)

t = np.arange(0.0, 5.0, 0.1)  # try printing t

# Plot no lado superior esquerdo
plt.subplot(3, 2, 1)
y1 = np.exp(-t)
plt.plot(t, y1, 'g+')  # try 'g' or 'bo' or 'k+'

# Plot no lado inferior esquerdo
plt.subplot(3, 2, 5)
y2 = np.cos(2*np.pi*t)
plt.plot(t, y2, 'ro-')

# Plot no lado direito
plt.subplot(3, 2, 4)
y3 = y1 * y2
plt.plot(t, y3, 'go-')

plt.show()

