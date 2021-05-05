import matplotlib.pyplot as plt
# ingreso de datos
meses = ["Enero","Febrero","Marzo"]
hipoteca = [700,800, 850]
servicios = [500,300, 380]
reparaciones = [100,120,100]
# datos del propio gráfico
plt.plot([],[], color='blue', label='hipoteca')
plt.plot([],[], color='orange', label='servicios')
plt.plot([],[], color='brown', label='reparaciones')
plt.stackplot(meses,hipoteca, servicios,reparaciones,
colors=['blue', 'orange', 'brown'])
plt.legend()
plt.title('Gastos de la casa')
plt.xlabel('Meses del año')
plt.ylabel('costo')
plt.show()