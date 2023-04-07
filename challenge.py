cont = 0
cadastro = 0
opcao = 0
diahoje = 0
meshoje = 0
nome = 0
dianascimento = 0
mesnascimento = 0
anonascimento = 0
email = 0
rg = 0
cnh = 0
cpf = 0
telefone = 0
endereco = 0
numresidencia = 0
complemento = 0
numserie = 0
modelo = 0
valor = 0
cor = 0
ntfiscal = 0
fbtempo = 0
fbservicos = 0
fbproblemas = 0
fbatendimentos = 0
fbduvidas = 0

print("Olá, em que a Technobike pode te ajudar hoje?")
while opcao != 5:
    print("\n1 - Cadastro")
    print("2 - Registrar bike")
    print("3 - Feedback")
    print("4 - Contrato")
    print("5 - Relatório")
    print("6 - Encerrar")
    opcao = int(input("\nSelecione uma das opções acima: "))

    if opcao == 6:
          print("\nEncerrando, até a próxima!")

#cadastro
    #while cadastro != 1:    
    if opcao == 1: 
        diahoje = int(input("Digite o dia de hoje: "))
        meshoje = int(input("Digite o mês atual: "))
        nome = input("\nDigite seu nome: ")
        dianascimento = int(input("Digite o dia de seu nascimento: "))
        if dianascimento > 0 and dianascimento < 32:
            mesnascimento = int(input("Digite o mes de seu nascimento: "))
        elif  mesnascimento > 0 and mesnascimento < 13:
            anonascimento = int(input("Digite o ano de seu nascimento: "))
        elif anonascimento < 2006 and anonascimento > 1903:
            print(" ")
        if meshoje == mesnascimento and anonascimento == 2005 and diahoje > dianascimento:
                print("\n1 - RG")
                print("2 - CNH")
                cdopcao2 = int(input("\nSelecione uma opção: "))
            

                if cdopcao2 == 1:
                        rg = input("\nDigite seu RG: ")
                elif cdopcao2 == 2: 
                        cnh = int(input("\nDigite sua CNH: "))
                else:
                        print("\nDigite um número válido!")
                        break
        else:
            print("Digite uma data válida!")
            cadastro += 1 
            break
        cpf = int(input("Digite seu CPF: "))
        if cpf > 99999999999 and cpf < 1:
                print("Digite um número válido!")
                cadastro += 1
        else:
            endereco = input("Digite a rua: ")
            numresidencia = int(input("Digite o número da residência: "))
            print("\nÉ necessário complemento? \n1 - Sim \n2 - Não")
            cdopcao3 = int(input("\nSelecione uma opção: "))
            if cdopcao3 == 1:
                complemento = input("Informe o complemento: ")
                print(f"As informações estão corretas? \nNome: {nome}")
                print(f"Data de nascimento{dianascimento}/{mesnascimento}/{anonascimento}")
                if cnh ==0:
                    print(f"RG: {rg}")
                elif rg == 0:
                    print(f"CNH: {cnh}")
                print(f"CPF: {cpf}")
                print(f"Endereço: {endereco} {numresidencia}  {complemento}")
                cdopcao4 = int(input("\n1 - Sim \n2 - Não \nSelecione uma opção: "))
                if cdopcao4 == 1:
                    print("Cadstro realizado.")
            else: 
                print(f"\nAs informações estão corretas? \nNome: {nome}")
                print(f"Data de nascimento: {dianascimento}/{mesnascimento}/{anonascimento}")
                if cnh ==0:
                    print(f"RG: {rg}")
                elif rg == 0:
                    print(f"CNH: {cnh}")
                print(f"CPF: {cpf}")
                print(f"Endereço: {endereco} {numresidencia}  {complemento}")
                cdopcao4 = int(input("1 - Sim \n2 - Não \nSelecione uma opção: "))
                if cdopcao4 == 1:
                    print("\nCadstro realizado.")
                else:
                    print("Faça novamente o cadastro.")
                    cadastro += 1
                            
#registro da bike

    if opcao == 2:
        modelo = input("Informe o modelo da bike: ")
        numserie = int(input("Digite o número de série: "))
        ntfiscal = int(input("Informe a nota fiscal: "))
        cor = input("Informe a cor: ")
        print(f"\nAs informações estão corretas? \nModelo: {modelo}")
        print(f"Número de série: {numserie}")
        print(f"Nota fiscal: {ntfiscal}")
        print(f"Cor: {cor}")
        print("\n1 - Sim \n2 - Não")
        rgopcao = int(input("\nSelecione uma opção: "))
        if rgopcao == 1:
            print("\nCadstro realizado.")
        else:
            print("Faça novamente o registro.")
            
#feedback
    if opcao == 3: 
        print("\nQual o motivo do feedback? \n1 - Tempo de espera")
        print("2 - Serviços")
        print("3 - Problemas")
        print("4 - Atendimeto")
        print("5 - Dúvidas")
        fbopcao = int(input("Selecione uma opção: "))
        if fbopcao ==1:
            fbtempo = input("\nEscreva seu feedback: ")
            print("\nTem certeza que vai enviar o feedback? \n1 - Sim \n2 - Não")
            fbopcao2 = int(input("\nSelecione uma opção: "))
            if fbopcao2 == 1:
                print("Feedback enviado!")
            elif fbopcao2 == 2:
                print("Feedbck cancelado!")
            else:
                print("Digite uma opção válida!")
        elif fbopcao == 2:
            fbservicos = input("\nEscreva seu feedback: ")
            print("\nTem certeza que vai enviar o feedback? \n1 - Sim \n2 - Não")
            fbopcao2 = int(input("\nSelecione uma opção: "))
            if fbopcao2 == 1:
                print("Feedback enviado!")
            elif fbopcao2 == 2:
                print("Feedbck cancelado!")
            else:
                print("Digite uma opção válida!")
        elif fbopcao == 3 :
            fbproblemas = input("\nEscreva seu feedback: ")
            print("\nTem certeza que vai enviar o feedback? \n1 - Sim \n2 - Não")
            fbopcao2 = int(input("\nSelecione uma opção: "))
            if fbopcao2 == 1:
                print("Feedback enviado!")
            elif fbopcao2 == 2:
                print("Feedbck cancelado!")
            else:
                print("Digite uma opção válida!")
        elif fbservicos == 4:
            fbatendimentos = input("\nEscreva seu feedback: ")
            print("\nTem certeza que vai enviar o feedback? \n1 - Sim \n2 - Não")
            fbopcao2 = int(input("\nSelecione uma opção: "))
            if fbopcao2 == 1:
                print("Feedback enviado!")
            elif fbopcao2 == 2:
                print("Feedbck cancelado!")
            else:
                print("Digite uma opção válida!")
        elif fbopcao == 5:
            fbduvidas = input("\nEscreva seu feedback: ")
            print("\nTem certeza que vai enviar o feedback? \n1 - Sim \n2 - Não")
            fbopcao2 = int(input("\nSelecione uma opção: "))
            if fbopcao2 == 1:
                print("Feedback enviado!")
            elif fbopcao2 == 2:
                print("Feedbck cancelado!")
            else:
                print("Digite uma opção válida!")
        else:
             print("\nDigite uma opção válida!")


