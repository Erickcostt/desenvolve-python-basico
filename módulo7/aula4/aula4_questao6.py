musicas_por_ano = {}
resultado = []

with open("spotify-2023.csv", "r", encoding="latin-1") as arquivo:
    linhas = arquivo.readlines()[1:]
    for linha in linhas:
        if '"' in linha:
            continue
        partes = linha.strip().split(",")
        if len(partes) < 9:
            continue
        try:
            ano = int(partes[3])
            streams = int(partes[8])
        except:
            continue
        if 2012 <= ano <= 2022:
            nome = partes[0]
            artista = partes[1]
            if ano not in musicas_por_ano or streams > musicas_por_ano[ano][3]:
                musicas_por_ano[ano] = [nome, artista, ano, streams]

for ano in sorted(musicas_por_ano.keys()):
    resultado.append(musicas_por_ano[ano])

print(resultado)
