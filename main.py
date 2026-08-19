#   PARTE MENU INTERATIVO 
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

 #   PARTE VALORES
 if opcao == "1":
    valor = float(input("Digite o valor da receita: R$").replace(",","."))
    descricao = input("digite a descrição da receita:")

    receitas.append({"valor": valor,
                     "descricao": descricao})

    print(f"Receita de R$ {valor:.2f} adicionada!")

 elif opcao == "2":
    valor = float(input("Digite o valor da despesa: R$").replace(",","."))
    descricao = input("Digite a descrição da despesa:")
    categoria = input("digite a categoria da despesa:")

    despesas.append({ "valor": valor,"descricao":descricao,"categoria":categoria})
    
    print(f"Despesa de R$ {valor:.2f} adicionada!")

#   PARTE  SALDO
 elif opcao == "3":
    total_receitas = 0

    for receita in receitas:
       total_receitas += receita["valor"]

       total_despesas = 0
    for despesa in despesas:
       total_despesas += despesa["valor"]

    saldo = total_receitas - total_despesas

    print(f"\nSaldo atual: R$ {saldo:.2f}")

#   PARTE  TRANSAÇÔES5
 elif opcao == "4":
    print("\n     TRANSAÇÔES     ")

    print("Receitas:")

    for receita in receitas:
       print(f"R$ {receita['valor']:.2f} - {receita['descricao']}")
       
    total_receitas = 0
    for receita in receitas:
       total_receitas +=receita["valor"]

    print(f"\nTotal de receitas: R$ {total_receitas:.2f}")
    print("\nDespesas")

    for despesa in despesas:
       print(f"R$ {despesa['valor']:.2f} - "
             f"{despesa['descricao']}"
             f"({despesa['categoria']})")

    total_despesas = 0
    for despesa in despesas:
       total_despesas += despesa["valor"]

    print(f"\nTotal de despesas: R$ {total_despesas:.2f}")
    
 elif opcao == "5":
    print("Saindo do FinanceIA...")  
 else:
    print("Opção inválida!")



