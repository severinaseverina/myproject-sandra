#Demonstração do uso if/elif/else...
print("Digite a sua idade:")
IDADE = int(input())

if IDADE < 18:
    print("Voce não é maior de idade!")
    print("Não podera realizar a operação!")
elif IDADE >=65:
    print("Você já esta pronto para se aposentar?")
    print("Poderemos oferecer suporte ténico...")
else:
    print("Voce é maior de idade!")
    print("Não podera realizar a operação!")

    print("Obrigado por optar pelos nossos serviços!")

