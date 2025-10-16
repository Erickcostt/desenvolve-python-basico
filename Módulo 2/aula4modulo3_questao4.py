distancia=int(input("Digite a distância em km:"))
peso=int(input("Digite o peso em kg:"))
peso=10*peso
if distancia <=100:
    print("O preço é R$", peso*1) 
if distancia >100 and distancia <=300:
    print("O preço é R$", peso*1.5)
else:
    print("O preço é R$", {peso*2})

