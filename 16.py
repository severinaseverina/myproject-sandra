#ATIVIDADES...
NOTA1 = float(input("Digite primeira nota?"))
NOTA2 = float(input("Digite segunda nota?"))
NOTA3 = float(input("Digite terceira nota?"))
NOTA4 = float(input("Digite quarta nota?"))

#Calculando a média
MEDIA = (NOTA1 + NOTA2 + NOTA3 + NOTA4)/4

#Verificando o resultado
if MEDIA >= 6:
   print("aprovado")
else:
   print("reprovado")

