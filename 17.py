# Demonstraoção...
print("Digite o seu nome: ")
NOME = input()
print("Digite a sua idade: ")
IDADE = int(input())
print("Digite a sua altura: ")
ALTURA = float(input())
print("Digite o seu peso")
PESO = int(input())

# Exibição dos dados...
print("O meu nomeé: ", NOME)
print("A minha idade: ", IDADE)
print("A minha altura é:",  ALTURA)

#cálculo do ICM...
IMC = PESO / ALTURA ** 2

#Exibição dos resultados...
if IMC < 18:
    print("Seu peso esta abaixo...")
elif IMC >25:
    print("Seu peso esta acima...")
else:
    print("Seu peso esta ideal!")
          
