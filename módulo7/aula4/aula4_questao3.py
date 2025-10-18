with open("estomago.txt", "r", encoding="latin-1") as arquivo:
    linhas = arquivo.readlines()

# Primeiras 25 linhas
print("Primeiras 25 linhas:")
for l in linhas[:25]:
    print(l.strip())

# Número de linhas
print("\nNúmero de linhas:", len(linhas))

# Linha com maior número de caracteres
maior_linha = max(linhas, key=lambda x: len(x))
print("\nLinha com mais caracteres:", maior_linha.strip())

# Contagem de nomes Nonato e Íria
cont_nonato = cont_iria = 0
for l in linhas:
    palavras_linha = l.split()
    for p in palavras_linha:
        if p.lower() == "nonato":
            cont_nonato += 1
        elif p.lower() == "íria":
            cont_iria += 1
print("\nMenções a Nonato:", cont_nonato)
print("Menções a Íria:", cont_iria)
