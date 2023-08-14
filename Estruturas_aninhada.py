conta_corrente = 1000
conta_poupanca = 2000
limite = 500


operacao = int(input("O que deseja fazer?\n [1]Ver saldo/limite\n [2]saque ")) #Tela inicial do banco
1
#Codigo tela inicial
if operacao == 1:
    opcao = int(input("Digite uma opção:\n [1]Saldo conta corrente\n [2]Saldo poupança\n [3]Limite "))# TEla após selecionar que quer ver saldo limite
        #Codigo de escolha de saldo/limite a ser verificado
    if opcao == 1:
        print(conta_corrente)
    elif opcao == 2:
        print(conta_poupanca)
    elif opcao == 3:
        print(limite)
    else:
        exit("Código invalido, refaça a operação!")

elif operacao == 2:
    saque = int(input("Digite o tipo de conta:\n [1]Conta corrente\n [2]Conta poupança ")) #tipo de conta para saque
    valor = float(input("Digite o valor do saque: ")) #Valor do saque

    #saque corrente
    if saque == 1:
        valor
        if valor <= conta_corrente:
            conta_corrente -= valor
            print("Saque efetuado")
        else: 
            print("Saque não efetuado, verifique seu saldo")
        print("O saldo da conta corrente é: ", conta_corrente)
    
    #Saque poupança
    if saque == 2:
        
        valor
        if valor <= conta_poupanca:
            conta_poupanca -= valor
            print("Saque efetuado")
        else:
            print("Saque não efetuado, verifique seu saldo")
        print("O saldo da conta poupança é: ", conta_poupanca)

else:
    exit("Opção invalida refaça a operação")





