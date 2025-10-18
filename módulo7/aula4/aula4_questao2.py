with open("frase.txt", "r", encoding="utf-8") as arquivo:
    texto = arquivo.read()

palavras = []
palavra_atual = ""
for c in texto:
    if ('a' <= c <= 'z') or ('A' <= c <= 'Z') or c == "é" or c == "É":  # letras e acentos simples
        palavra_atual += c
    else:
        if palavra_atual:
            palavras.append(palavra_atual)
            palavra_atual = ""
if palavra_atual:
    palavras.append(palavra_atual)

with open("palavras.txt", "w", encoding="utf-8") as arquivo:
    for p in palavras:
        arquivo.write(p + "\n")

# Imprimir conteúdo
with open("palavras.txt", "r", encoding="utf-8") as arquivo:
    print(arquivo.read())
