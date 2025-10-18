while True:
    frase = input('Digite uma frase (digite "fim" para encerrar): ')
    if frase.lower() == "fim":
        break

    frase_limpa = ""
    for c in frase:
        if c.isalnum():
            frase_limpa += c.lower()

    if frase_limpa == frase_limpa[::-1]:
        print(f'"{frase}" é palíndromo')
    else:
        print(f'"{frase}" não é palíndromo')
