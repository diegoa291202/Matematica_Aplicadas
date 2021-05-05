import  matplotlib.pyplot as plt
data = {'manzana': 10, 'naranjas': 15, 'limones' : 5, 'limas' : 20}
names = list (data.keys())
values = list(data.values())

fig, axsw = plt.subplots(1,3, figsize=(12,3), sharey= True)
axsw[0].bar(names, values)
axsw[1].scatter(names,values)
axsw[2].plot(names, values)
fig.suptitle('Categoría de gráficas')
plt.show()
