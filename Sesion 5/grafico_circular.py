import matplotlib.pyplot as plt
dias = ['dom','lun','mar' ,'mie' ,'jue', 'vie', 'sab']
dormir = [9,6,7,6]
comer = [3,1,1.30,1]
trabajar = [2,10,9,8]
partes =[7,3,8]

actividades=['dormir','comer','trabajar']
cols=['g','y','r','b']
plt.title('Diagrama circular de la semana')
plt.xlabel=('x')
plt.ylabel=('y')
plt.pie(partes, colors=cols, labels=actividades, startangle=30,
shadow=True, explode=(0.1,0.1,0.1), autopct=('%3.1f%%'))
plt.legend()
plt.show()