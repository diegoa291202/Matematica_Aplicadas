# siempre se tiene que importar estas librerias
from mpl_toolkits.mplot3d import Axes3D
import numpy as np 
import matplotlib
import matplotlib.pyplot as plt 

fig = plt.figure()
ax = Axes3D(fig)
x = [6,3,6,9,12,24]
y= [3,5,78,12,23,56]
ax.plot(x, y, zs=0, zdir='z', label='zs=0, zdir=z')
plt.show()




