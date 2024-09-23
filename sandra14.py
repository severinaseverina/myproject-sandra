print("Digite o número referente à sua avaliação do filme/série: ")
print("1.Péssimo")
print("2.Ruim")
print("3.Razoável")
print("4.Bom")
print("5.Ótimo")


avaliacao = int(input())
match avaliacao:
    case 1:
        print("Você avaliou como: Péssimo")
        descricao= input("Por que você avaliou dessa forma?")
        print(f"Motivo: {descricao}")
    case 2:
        print("Você avaliou como: Ruim")
        descricao= input("Por que você avaliou dessa forma?')
        print(f"Motivo:{descricao")
    case 3:
        print("Você avaliou como: Rázoavel")
        descricao=input("No que podemos melhorar?")
        print(f'Motivo: {descricao}")
    case 4:
        print("Você avaliou como: Bom")
        Descricao= input("O que falta para ser ótimo?")
              
