
a = {1,2,3,4}
b = {3,4,5,6}

#UNIAO

print(a)
print(b)
print("")

print(a.union(b))

#INTERSECAO
print(a.intersection(b))

#DIFERENCAO
print(a.difference(b))

#DIFERENCAO SIMETRICA
print(a.symmetric_difference(b))

#SE UM CONJUNTO EH UM SUBCONJUNTO DE OUTRO
print(a.issubset(b))

#SE UM CONJUNTO EH UM SUBCONJUNTO DE OUTRO
print(a.issuperset(b))

#DISJUNCAO
print(a.isdisjoint(b))

#REMOVENDO DUPLICADOS
lista = [1,1,2,3,4,4,5]
print(lista)
conjunto = set(lista)
print(conjunto)
