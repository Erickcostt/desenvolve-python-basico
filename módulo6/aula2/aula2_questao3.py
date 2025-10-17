import random

lista1 = [random.randint(0, 50) for _ in range(20)]
lista2 = [random.randint(0, 50) for _ in range(20)]

interseccao = sorted(list(set(lista1) & set(lista2)))

print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Interseção (ordenada, sem duplicatas):", interseccao)
print("Quantidade de vezes que cada elemento aparece em cada lista:")

for valor in interseccao:
    print(valor, "-", lista1.count(valor), "vezes na lista1 e", lista2.count(valor), "vezes na lista2")
