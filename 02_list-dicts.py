lista_cadena = ["uno","dos","tres"]
lista_enteros =  [1,2,3]
lista_mezcla = ["Python", 27, 34.6]

print(lista_cadena)
print(lista_enteros)
print(lista_mezcla)

for x in lista_cadena:
    print(x)

for i in lista_enteros:
    print(i)

for j in lista_mezcla:
    print(j)

Ultima_entero = lista_enteros[-1]
Ultima_mezcla = lista_mezcla[-1]
Ultima_cadena = lista_cadena[-1]

print( "Las variables son:" +Ultima_cadena +" " +str(Ultima_entero) + " " + str(Ultima_mezcla))


Dic_pelis = {"a":"El señor de los anillos", "James Cameron":"Avatar", "b":"La bella y la bestia"}

print(Dic_pelis)
for a,b in Dic_pelis.items():
    print(a +" es el autor de: " +b)

for a,b in Dic_pelis.items():
    print(a)

for a,b in Dic_pelis.items():
    print(b)
