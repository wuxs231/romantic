import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

x = np.linspace(-2, 2, 200)
y1 = np.sqrt(1-np.square(np.fabs(x)-1))
y2 = np.arccos(1-np.fabs(x))-np.pi

plt.plot(x, y1, 'r', x, y2, 'r')
plt.axis([-2.5, 2.5, -3.5, 1.5])

plt.title('coded by Lancer Wu', fontsize=16)
plt.show()

