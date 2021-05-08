# Módulo de carga
from mpl_toolkits.mplot3d import Axes3D
import numpy as np 
import matplotlib.pyplot as plt
# Generar datos
x = np.linspace(-6 * np.pi, 6 * np.pi, 1000)
y = np.sin(x)
z = np.cos(x)
# Crear objetos gráficos 3D
fig = plt.figure()
ax = Axes3D(fig)

# Dibujar un gráfico lineal
ax.plot(x,y,z)
# Mostrar la imagen
plt.show()