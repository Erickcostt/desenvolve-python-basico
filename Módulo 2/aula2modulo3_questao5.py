#5 - Solicite de um usuário seu gênero ("M" ou "F"), sua idade e seu tempo de serviço 
#(em anos) e escreva uma expressão que imprima True se a pessoa já pode se aposentar,
#  ou False caso contrário, de acordo com as seguintes regras:

#A: Para mulheres, ter mais de 60 anos. Para homens, 65.
#B: Ou ter trabalhado pelo menos 30 anos
#C: Ou ter 60 anos  e trabalhado pelo menos 25.

gnr= str(input("Qual seu gênero?(M/F)"))
idd=int(input("Qual sua idade?"))
srv=int(input("Quantos anos de serviço?"))


aposentadoria = (
    (gnr == "F" and idd > 60) or
    (gnr == "M" and idd > 65) or
    (srv >= 30) or
    (idd >= 60 and srv >= 25)
)
print("Pode se aposentar:", aposentadoria)