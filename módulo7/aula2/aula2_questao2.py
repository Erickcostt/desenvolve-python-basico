frase = input("Digite uma frase: ")
vogais = "aeiouAEIOU"
nova_frase = ""

for c in frase:
    if c in vogais:
        nova_frase += "*"
    else:
        nova_frase += c

print("Frase modificada:", nova_frase)
