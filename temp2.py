lista=['R1',6,6.8,True,"R1"]
print(lista)
print(type(lista))
print(len(lista))
print(lista[0],'\n')
print(lista[4],'\n')
print(lista[-1],'\n')
print(lista[-5],'\n')
print(lista[-2],'\n')
lista[3]=False
print(lista)
del lista[4]
print(lista)