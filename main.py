palabra="Nacho"

for letra in palabra:
    print(letra + "G"+"R")

indice=0
for letra in palabra:
    print(indice,letra)
    indice=indice+1

marcas=["BMW","Honda","Nissan"]

for marca in marcas:
     print(marca)

for indice,letra in enumerate(palabra):
    print(indice,letra)