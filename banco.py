valor_conta = 0

#funcao upper para verificacoes
def capsLock(string):
    return string.upper()

#funcao de saque
def sacar():
    global valor_conta 
    valor_saque = float(input('Insira o valor a sacar: '))
    #verificacao de valor de saque e valor em conta
    if valor_saque > valor_conta:
        print(f"Você não possui R${valor_saque} para ser sacado.\nVocê tem R${valor_conta} disponível em conta")
    else: 
        print(f"Saque realizado no valor de: R${valor_saque}")

        #tirando da conta o valor solicitado em saque
        valor_conta = valor_conta - valor_saque

        print(f"\nVocê possui R${valor_conta} na sua conta")

#funcao de deposito
def depositar():
    valor_deposito = float(input("Insira o valor a depositar: "))
    print(f"Deposito realizado no valor de: R${valor_deposito}")

    global valor_conta
    #adicionado valor de deposito a conta
    valor_conta = valor_conta + valor_deposito

    print(f"\nVocê possui R${valor_conta} na sua conta")

#funcao para solicitar ajuda apos a primeira escolha
def ajuda():
    global escolha
    global escolha_upper
    escolha = input("\n1) SACAR\n2) DEPOSITAR\n3) VISUALIZAR EXTRATO\nEscolha a opção que deseja: ")
    escolha_upper = capsLock(escolha)
    option()

#inicio do codigo
escolha = input("BEM VINDO AO BANCO!\n1) SACAR\n2) DEPOSITAR\n3) VISUALIZAR EXTRATO\nEscolha a opção desejada: ")

#deixa a escolha em caps, para evitar que o codigo de erro ao escrever em minuscula ou com alguma letra em caixa alta
escolha_upper = capsLock(escolha)

#condicionais para sacar, depositar e extrato
def option(): 
    if escolha_upper == "1" or escolha_upper == "SACAR" or escolha_upper == "SAQUE":
        sacar()
        question = input("Te ajudo em algo mais? (S/N): ")
        question_upper = capsLock(question)
        if question_upper == "N" or question_upper == "NAO" or question_upper == "NÃO":
            print("Fico feliz em ter ajudado!")
        elif question_upper == "S" or question_upper == "SIM":
            ajuda()
    elif escolha_upper == "2" or escolha_upper == "DEPOSITAR" or escolha_upper == "DEPOSITO":
            depositar()
            question = input("Te ajudo em algo mais? (S/N): ")
            question_upper = capsLock(question)
            if question_upper == "N" or question_upper == "NAO" or question_upper == "NÃO":
                print("Fico feliz em ter ajudado!")
            elif question_upper == "S" or question_upper == "SIM":
                ajuda()
    elif escolha_upper == "3" or escolha_upper == "VISUALIZAR EXTRATO" or escolha_upper == "EXTRATO":
        print(f"Você tem R${valor_conta}")
        question = input("Te ajudo em algo mais? (S/N): ")
        question_upper = capsLock(question)
        if question_upper == "N" or question_upper == "NAO" or question_upper == "NÃO":
            print("Fico feliz em ter ajudado!")
        elif question_upper == "S" or question_upper == "SIM":
            ajuda()

option()

