

n = int(input("Digite a quantidade de experimentos: "))

total = 0
total_s = 0
total_r = 0
total_c = 0

cont = 0

while cont < n:
    entrada = input("Digite a quantidade e o tipo (ex: 10 C): ").split()
    quantia = int(entrada[0])
    tipo = entrada[1].upper()

    total += quantia

    if tipo == 'S':
        total_s += quantia
    elif tipo == 'R':
        total_r += quantia
    elif tipo == 'C':
        total_c += quantia

    cont = cont + 1

perc_c = (total_c / total) * 100
perc_r = (total_r / total) * 100
perc_s = (total_s / total) * 100

print(f"Total: {total} cobaias")
print(f"Total de coelhos: {total_c}")
print(f"Total de ratos: {total_r}")
print(f"Total de sapos: {total_s}")
print(f"Percentual de coelhos: {perc_c:.2f} %")
print(f"Percentual de ratos: {perc_r:.2f} %")
print(f"Percentual de sapos: {perc_s:.2f} %")
