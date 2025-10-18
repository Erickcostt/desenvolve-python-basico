import random

def encrypt(nomes):
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    chave = random.randint(1, 10)
    nomes_cript = []

    for nome in nomes:
        novo_nome = ""
        for c in nome:
            if c in alfabeto:
                i = alfabeto.index(c)
                i = (i + chave) % len(alfabeto)
                novo_nome += alfabeto[i]
            else:
                novo_nome += c
        nomes_cript.append(novo_nome)

    return nomes_cript, chave

nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
nomes_criptografados, chave = encrypt(nomes)

print("Chave aleatória:", chave)
print("Nomes criptografados:", nomes_criptografados)
