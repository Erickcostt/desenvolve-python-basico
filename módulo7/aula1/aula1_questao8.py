cpf = input("Digite o CPF (XXX.XXX.XXX-XX): ")

cpf_numeros = ""
i = 0
while i < len(cpf):
    if '0' <= cpf[i] <= '9':
        cpf_numeros += cpf[i]
    i += 1

if len(cpf_numeros) != 11:
    print("Inválido")
else:
    cpf_base = ""
    i = 0
    while i < 9:
        cpf_base += cpf_numeros[i]
        i += 1

    digitos_usuario = ""
    i = 9
    while i < 11:
        digitos_usuario += cpf_numeros[i]
        i += 1

    soma = 0
    i = 0
    while i < 9:
        soma += int(cpf_base[i]) * (10 - i)
        i += 1

    resto = soma % 11
    if resto < 2:
        digito1 = 0
    else:
        digito1 = 11 - resto

    soma2 = 0
    i = 0
    while i < 9:
        soma2 += int(cpf_base[i]) * (11 - i)
        i += 1
    soma2 += digito1 * 2

    resto2 = soma2 % 11
    if resto2 < 2:
        digito2 = 0
    else:
        digito2 = 11 - resto2

    if digitos_usuario == str(digito1) + str(digito2):
        print("Válido")
    else:
        print("Inválido")
