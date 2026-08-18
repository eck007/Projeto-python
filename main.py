#   PARTE 1 MENU INTERATIVO 
print("    FinanceIA   ")

opcao=""
receitas = []
despesas = []
while opcao != "5":
 print("\n1 - Adicionar receita")
 print("2 - Adicionar despesa")
 print("3 - Ver saldo")
 print("4 - Ver transações")
 print("5 - Sair")

 opcao = input("Escolha uma opçao:")
 print("Você escolheu:", opcao)

 #   PARTE 2 VALORES
 if opcao == "1":
    valor = float(input("Digite o valor da receita: R$").replace(",","."))
    receitas.append(valor)
    print(f"Receita de R$ {valor:.2f} adicionada!")

 elif opcao == "2":
    valor = float(input("Digite o valor da despesa: R$").replace(",","."))
    despesas.append(valor)
    print(f"Despesa de R$ {valor:.2f} adicionada!")

#   PARTE 4 SALDO
 elif opcao == "3":
    total_receitas = sum(receitas)
    total_despesas = sum(despesas)

    saldo = total_receitas - total_despesas

    print(f"\nSaldo atual: R$ {saldo:.2f}")

#   PARTE 3 TRANSAÇÔES
 elif opcao == "4":
    print("\n     TRANSAÇÔES     ")

    print("Receitas:")

    for receita in receitas:
       print(f"R$ {receita:.2f}")
       
    total_receitas = sum(receitas)
    print(f"\nTotal de receitas: R$ {total_receitas:.2f}")
    print("\nDespesas")

    for despesa in despesas:
       print(f"R$ {despesa:.2f}")
    total_despesas = sum(despesas)
    print(f"\nTotal de despesas: R$ {total_despesas:.2f}")
    
 elif opcao == "5":
    print("Saindo do FinanceIA...")  
 else:
    print("Opção inválida!")



