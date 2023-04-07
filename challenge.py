cont = 0
cadastro = 0
opcao = 0
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

print("Olá, em que a Technobike pode te ajudar hoje?")
while opcao != 5:
    print("\n1 - cadastro")
    print("2 - registrar bike")
    print("3 - feedback")
    print("4 - contrato")
    print("5 - encerrar")
    print("1 - cadastro")
    print("1 - cadastro")
    print("1 - cadastro")
    opcao = int(input("\nSelecione uma das opções acima: "))

    if opcao == 5:
          print("\nEncerrando, até a próxima!")

#cadastro
    
    if opcao == 1:
        nome = input("\nDigite seu nome: ")
        dianascimento = int(input("Digite o dia de seu nascimento: "))
        mesnascimento = int(input("Digite o mes de seu nascimento: "))
        anonascimento = int(input("Digite o ano de seu nascimento: "))
        if dianascimento > 0 and dianascimento < 32 and  mesnascimento > 0 and mesnascimento < 13 and anonascimento < 2006 and anonascimento > 1903:
            print("\n1 - RG")
            print("2 - CNH")
            cdopcao2 = int(input("\nSelecione uma opção: "))

            if cdopcao2 == 1:
                    rg = input("\nDigite seu RG: ")
            elif cdopcao2 == 2: 
                    cnh = int(input("\nDigite sua CNH: "))
            else:
                    print("\nDigite um número válido!")
                    cadastro == 1
        else:
                print("Digite uma data válida!")
                cadastro == 1 
        cpf = int(input("Digite seu CPF: "))
        if cpf > 99999999999 and cpf < 1:
                print("Digite um número válido!")
                cadastro == 1
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
        rgopcao = int(input("\n1 - Sim \n2 - Não \nSelecione uma opção: "))
        if rgopcao == 1:
            print("\nCadstro realizado.")
        else:
            print("Faça novamente o cadastro.")
            



          

