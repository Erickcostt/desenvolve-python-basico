def validador_senha(senha):
    if len(senha) < 8:
        return False

    tem_maiuscula = tem_minuscula = tem_numero = tem_especial = False
    especiais = "@#$%&*!"

    for c in senha:
        if "A" <= c <= "Z":
            tem_maiuscula = True
        elif "a" <= c <= "z":
            tem_minuscula = True
        elif "0" <= c <= "9":
            tem_numero = True
        elif c in especiais:
            tem_especial = True

    return tem_maiuscula and tem_minuscula and tem_numero and tem_especial

# Exemplo
senha1 = "Senha123@"
senha2 = "senhafraca"
senha3 = "Senha_fraca"

print(validador_senha(senha1))  # True
print(validador_senha(senha2))  # False
print(validador_senha(senha3))  # False
