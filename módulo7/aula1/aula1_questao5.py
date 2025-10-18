frase = input("Digite uma frase: ")

vogais = "aeiouAEIOU"
indices = []

for i, letra in enumerate(frase):
    if letra in vogais:
        indices.append(i)

print(f"{len(indices)} vogais")
print(f"Índices {indices}")
