import random

def embaralhar_palavras(frase):
    palavras = frase.split()
    resultado = []

    for p in palavras:
        if len(p) > 3:
            meio = list(p[1:-1])
            random.shuffle(meio)
            resultado.append(p[0] + "".join(meio) + p[-1])
        else:
            resultado.append(p)

    return " ".join(resultado)

# Exemplo
frase = "Python é uma linguagem de programação"
print(embaralhar_palavras(frase))
