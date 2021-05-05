# Módulo de carga
from mpl_toolkits.mplot3d import Axes3D
import numpy as np 
import matplotlib.pyplot as plt

# Crear objetos gráficos 3D
fig = plt.figure()
ax = Axes3D(fig)

# Generar datos y trazar
x = [0,1,2,3,4,5,6]
for i in x:
 y = [0,1,2,3,4,5,6,7,8,9]    
 z = abs(np.random.normal(1,10,10))
ax.bar(y, z , i, zdir='y', color=['r', 'g', 'b','y'])
plt.ylabel('Histograma tridimensional')
plt.legend()
plt.show()
