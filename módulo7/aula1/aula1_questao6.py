frase = input("Digite uma frase: ")
objetivo = input("Digite a palavra objetivo: ")

palavras = frase.split()
anagramas = []

for palavra in palavras:
    if sorted(palavra) == sorted(objetivo) or sorted(palavra) == sorted(objetivo.capitalize()):
        anagramas.append(palavra)

print(f"Anagramas: {anagramas}")
