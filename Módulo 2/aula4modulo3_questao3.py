ano=int(input("Digite um ano:"))

     
if ano/4 and ano%4==0 or ano/400 and ano%400==0:
     print("bisexto")
else:
     print("Não é bissexto")
