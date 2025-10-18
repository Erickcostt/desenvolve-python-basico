frase = input("Digite uma frase: ")

vogais = sorted([letra for letra in frase if letra in 'aeiouAEIOU'])
consoantes = [letra for letra in frase if letra not in 'aeiouAEIOU ']

print("Vogais:", vogais)
print("Consoantes:", consoantes)
