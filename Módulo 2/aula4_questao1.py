#area_m2 = comprimento * largura

#preco_total = preco_m2 * area_m2

largura=int(input("Digite a largura(m):"))
comprimento=int(input("Digite o comprimento(m):"))
area_m2 = comprimento * largura
preco_m2 = float(input("Digite o preço do metro quadrado (R$): "))
preco_total = preco_m2 * area_m2
print(f"O terreno possui {area_m2}m2 e custa R${preco_total:,.2f}")