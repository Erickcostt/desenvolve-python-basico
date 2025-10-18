numero = input("Digite o número: ")

if len(numero) == 8:
    numero = "9" + numero
elif len(numero) == 9 and numero[0] != "9":
    print("Número inválido! O número com 9 dígitos deve começar com 9.")
else:
    if len(numero) != 9:
        print("Número inválido! Deve ter 8 ou 9 dígitos.")

if len(numero) == 9 and numero[0] == "9":
    numero_formatado = numero[:5] + "-" + numero[5:]
    print(f"Número completo: {numero_formatado}")
