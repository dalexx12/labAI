#ex 1
lista = [1, 2, 3, 4, 5]
suma = sum(lista)
nr = len(lista)
media = suma/nr
print(media)

#2
lista = [1, -2, 3, -4, 5]
pozitive = []
negative = []
for n in lista:
    if n >= 0:
        pozitive.append(n)
    else:
        negative.append(n)
print("Nr pozitive sunt:", pozitive)
print("Nr negative sunt:", negative)

# 3
lista = [1, 2, 3, 4, 5]
suma = 0
n = len(lista) - 2
for i in range(n):
    suma = suma + lista[i]
print(suma)

# 4
lista = [1, 2, 3, 4, 5, 6]
impare = []
for i in range(len(lista)):
    if i % 2 != 0:
        impare.append(lista[i])
print(impare)

#5
lista = [15, 8, 22, -3, 40]
minim = lista[0]
for n in lista:
    if n < minim:
        minim = n
print(minim)
