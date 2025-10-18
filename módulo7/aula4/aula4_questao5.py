livros = [
    ["O Caçador de Pipas", "Khaled Hosseini", 2003, 368],
    ["Torto Arado", "Itamar Vieira Junior", 2019, 264],
    ["1984", "George Orwell", 1949, 328],
    ["Dom Quixote", "Miguel de Cervantes", 1605, 992],
    ["O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943, 96],
    ["Cem Anos de Solidão", "Gabriel García Márquez", 1967, 417],
    ["A Metamorfose", "Franz Kafka", 1915, 128],
    ["O Senhor dos Anéis", "J.R.R. Tolkien", 1954, 1178],
    ["Harry Potter e a Pedra Filosofal", "J.K. Rowling", 1997, 223],
    ["Moby Dick", "Herman Melville", 1851, 635]
]

with open("meus_livros.csv", "w", encoding="utf-8") as arquivo:
    arquivo.write("Título,Autor,Ano de publicação,Número de páginas\n")
    for l in livros:
        arquivo.write(",".join([str(i) for i in l]) + "\n")
