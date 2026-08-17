#PARTE 1 /MENU INTERATIVO/ COMPLETO
print("    FinanceIA   ")

opcao=""

while opcao != "5":
 print("\n1 - Adicionar receita")
 print("2 - Adicionar despesa")
 print("3 - Ver saldo")
 print("4 - Ver transações")
 print("5 - Sair")

 opcao = input("Escolha uma opçao:")
 print("Você escolheu:", opcao)
 if opcao == "1":
    valor = float(input("Digite o valor da receita: R$").replace(",","."))
    print(f"Receita de R$ {valor:.2f} adicionada!")
    print("Adicionar receita")
 elif opcao == "2":
    print("Adicionar despesa")
 elif opcao == "3":
    print("Ver saldo")
 elif opcao == "4":
    print("Ver transações")
 elif opcao == "5":
    print("Saindo do FinanceIA...")  
 else:
    print("Opção inválida!")          