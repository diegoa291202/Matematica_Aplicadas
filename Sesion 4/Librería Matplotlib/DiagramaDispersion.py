import  matplotlib.pyplot as plt

#definir los datos
x1 = [0.25, 1.25, 2.25, 3.25, 4.25]
y1 = [10, 55, 80, 32, 40]
x2 = [0.75, 1.75, 2.75, 3.75, 4.75]
y2 = [42, 26, 10, 29, 66]


# configurar las características del gráfico

plt.scatter(x1,y1, label = 'Datos 1', color = 'red')
plt.scatter(x2,y2, label = 'Datos 2',  color = 'purple')

# Definir títulos y nombres de ejes
plt.title('Gráfico de dispersión')
plt.ylabel('Eje Y')
plt.xlabel('Eje X')

# Mostrar leyenda
plt.legend()

# Mostrar figura
plt.show()
