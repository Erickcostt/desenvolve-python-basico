numeros = []

while len(numeros) < 4:
    numeros = [int(x) for x in input("Digite pelo menos 4 números inteiros separados por espaço: ").split()]

print("Lista original:", numeros)
print("3 primeiros elementos:", numeros[:3])
print("2 últimos elementos:", numeros[-2:])
print("Lista invertida:", numeros[::-1])
print("Elementos de índice par:", numeros[::2])
print("Elementos de índice ímpar:", numeros[1::2])
