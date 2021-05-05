nombte = input("ingrese su nombre")
eda = input("ingrese si edad")
ecivil = input("estado civil")
if ecivil == "C":
    valorec = "CASADO"
elif ecivil == "V":
    valorec = "VIUDO"
elif ecivil == "D":
    valorec = "DIVORCIADO"
else:
    valorec = "soltero"
precivilint("hola", nombre, "su estado civil es:", valorec)
print("hola como estan todos aqui")
