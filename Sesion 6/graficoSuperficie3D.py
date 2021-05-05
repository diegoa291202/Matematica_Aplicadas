# Módulo de carga
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# Crea objetos gráficos 3D
fig = plt.figure()  
ax = Axes3D(fig)
# Generar datos
X = np.arange(-2, 2, 0.1)
Y = np.arange(-2, 2, 0.1)  
X, Y = np.meshgrid(X, Y)
Z = np.sqrt(X ** 2 + Y ** 2)
# Dibuja un mapa de superficie y usa cmap para colorearlo
ax.plot_surface(X, Y, Z, cmap=plt.cm.spring)
plt.show()
