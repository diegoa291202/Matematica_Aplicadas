import  matplotlib.pyplot as plt

#definir los datos
x1 = [3,4,5,6]
y1= [5,6,3,4]
x2= [2,5,8]
y2= [3,4,3]

# configurar las características del gráfico

plt.plot(x1,y1, label = 'Línea 1', linewidth=4, color='blue')
plt.plot(x2,y2, label = 'Línea 2', linewidth=4, color='green')

# Definir títulos y nombres de ejes
plt.title('Diagramas de Líneas')
plt.ylabel('Eje Y')
plt.xlabel('Eje X')

# Mostrar leyenda
plt.legend()
# Mostrar cuadrícula
plt.grid()
# Mostrar figura
plt.show()
