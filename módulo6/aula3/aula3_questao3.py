import random

lista = [random.randint(-10, 10) for _ in range(20)]
print("Original:", lista)

# Encontra o intervalo consecutivo com mais números negativos
max_negativos = 0
start = end = 0
i = 0
while i < len(lista):
    if lista[i] < 0:
        j = i
        while j < len(lista) and lista[j] < 0:
            j += 1
        if j - i > max_negativos:
            max_negativos = j - i
            start, end = i, j
        i = j
    else:
        i += 1

# Deleta o intervalo encontrado
del lista[start:end]

print("Editada:", lista)
