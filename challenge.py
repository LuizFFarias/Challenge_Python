
import datetime
#cadastro
dtatual = datetime.datetime.now()
cont = 0
opcao = 0
diahoje = 0
meshoje = 0
data = 0
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
complemento = ""
#bike
numserie = 0
modelo = 0
valorbike = 0
cor = 0
ntfiscal = 0
acessorios = 0
#feedback
fbtempo = 0
fbservicos = 0
fbproblemas = 0
fbatendimentos = 0
fbduvidas = 0
#relatório
cadastro = 0
registro_bike = 0


print("Olá, em que a Technobike pode te ajudar hoje?")
while opcao != 5:
    print("\n1 - Cadastro")
    print("2 - Registrar bike")
    print("3 - Feedback")
    print("4 - Relatório")
    print("5 - Contrato")
    print("6 - Encerrar")
    opcao = int(input("\nSelecione uma das opções acima: "))

    if opcao == 6:
          print("\nEncerrando, até a próxima!")
          break

#cadastro
    #while cadastro != 1:    
    if opcao == 1: 
        nome = input("\nDigite seu nome: ")
        email = input("Digite seu e-mail: ")
        data = input("Digite uma data no formato DD/MM/AAAA: ")
        dianascimento, mesnascimento, anonascimento = data.split('/')
        dianascimento = int(dianascimento)
        mesnascimento = int(mesnascimento)
        anonascimento = int(anonascimento)
        idade = dtatual.year - anonascimento - ((dianascimento, mesnascimento) > (dtatual.day, dtatual.month))

        if idade >= 18:  
            print("Dia:", dianascimento)
            print("Mês:", mesnascimento)
            print("Ano:", anonascimento)
            print("\n1 - RG")
            print("2 - CNH")
            cdopcao2 = int(input("\nSelecione uma opção: "))
            if cdopcao2 == 1:
                    rg = input("\nDigite seu RG: ")
            elif cdopcao2 == 2: 
                    cnh = int(input("\nDigite sua CNH: "))
            cpf = input("Digite seu CPF: ")
                
            endereco = input("Digite a rua: ")
            numresidencia = int(input("Digite o número da residência: "))
            print("\nÉ necessário complemento? \n1 - Sim \n2 - Não")
            cdopcao3 = int(input("\nSelecione uma opção: "))
            if cdopcao3 == 1:
                complemento = input("Informe o complemento: ")
                print(f" \nNome: {nome}")
                print(f"E-mail: {email}")
                print(f"Data de nascimento: {dianascimento}/{mesnascimento}/{anonascimento}")
                if cnh ==0:
                    print(f"RG: {rg}")
                elif rg == 0:
                    print(f"CNH: {cnh}")
                print(f"CPF: {cpf}")
                print(f"Endereço: {endereco} {numresidencia}  {complemento}")
                cdopcao4 = int(input("\nAs informações estão corretas? \n1 - Sim \n2 - Não \nSelecione uma opção: "))
                if cdopcao4 == 1:
                    print("Cadstro realizado.")
                    cadastro = 1
            else: 
                print(f"Nome: {nome}")
                print(f"E-mail: {email}")
                print(f"Data de nascimento: {dianascimento}/{mesnascimento}/{anonascimento}")
                if cnh ==0:
                    print(f"RG: {rg}")
                elif rg == 0:
                    print(f"CNH: {cnh}")
                print(f"CPF: {cpf}")
                print(f"Endereço: {endereco} {numresidencia}  {complemento}")
                cdopcao4 = int(input("\nAs informações estão corretas? \n1 - Sim \n2 - Não \nSelecione uma opção: "))
                if cdopcao4 == 1:
                    print("\nCadstro realizado.")
                    cadastro = 1
                elif cdopcao4 == 2:
                    print("Faça novamente o cadastro.")
                
                else:
                        print("\nDigite um número válido!")
                        break
        else:
            print("\nVocê não é maior de idade, não podemos continuar!")
            
    

        
        
            
        
                            
#registro da bike

    if opcao == 2:
        modelo = input("Informe o modelo da bike: ")
        numserie = int(input("Digite o número de série: "))
        ntfiscal = int(input("Informe a nota fiscal: "))
        cor = input("Informe a cor: ")
        valorbike = float(input("Informe o valor da bike: R$"))
           
        print("\nSua bike possui acessórios? \n1 - Sim \n2 - Não")
        bikeopcao = int(input("\nSelecione uma opção: "))
        if bikeopcao == 1:
            acessorios = float(input("Informe o valor total dos acessórios: R$"))
        print(f"\nModelo: {modelo}")
        print(f"Número de série: {numserie}")
        print(f"Nota fiscal: {ntfiscal}")
        print(f"Cor: {cor}")
        print(f"Valor da bike: R${valorbike}")
        if acessorios != 0:
            print(f"Valor dos acessórios: R${acessorios}")
        print("\nAs informações estão corretas? \n1 - Sim \n2 - Não")
        rgopcao = int(input("\nSelecione uma opção: "))
        if rgopcao == 1:
            print("\nRegistro realizado.")
            registro_bike = 1
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
        elif fbopcao == 4:
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

#Relatório
    if opcao == 4:
        print("\nRelatório dos dados adcionados: ")
        if cadastro == 1:
            print(f"\nRelatório do cadastro:  \nNome: {nome}")
            print(f"Data de nascimento: {dianascimento}/{mesnascimento}/{anonascimento}")
            if cnh ==0:
                print(f"RG: {rg}")
            elif rg == 0:
                print(f"CNH: {cnh}")
            print(f"CPF: {cpf}")
            print(f"Endereço: {endereco} {numresidencia}  {complemento}")
        elif cadastro == 0:
            print("Nenhum cadastro foi adicionado.")
        if registro_bike == 1:
            print(f"\nRelatório do registro da bike:  \nModelo: {modelo}")
            print(f"Número de série: {numserie}")
            print(f"Nota fiscal: {ntfiscal}")
            print(f"Cor: {cor}")
            if acessorios != 0:
                print(f"Valor dos acessórios: {acessorios}")

#contrato 
    if opcao == 5:
        print("Revisando seus dados: ")
        if cadastro != 1:
            print("Primeiro realize o cadastro.")
        elif registro_bike != 1: 
            print("Primeiro realize o registro da bike.")
        else:
            print("\nTodos os dados estão corretos!")
            print("\n1 - Cartão de crédito \n2 - Cartão de débito \n3 - Boleto \n4 - Pix")
            cntopcao = int(input("Selecione um método de pagamento: "))
            if cntopcao == 1: 
                nmr_cartao_credito = input("Digite o número do cartão: ")
                titular = input("Nome do titular: ")
                cdg_seguranca = input("Código de segurança: ") 
                dtvalidade = input("Digite uma data no formato MM/AAAA: ")
                mes_validade, ano_validade = dtvalidade.split('/') 
                mes_validade = int(mes_validade)
                ano_validade = int(ano_validade)
                validade = dtatual.year - ano_validade - (dtatual.month < mes_validade)
                if validade <= 0: 
                    print("O cartão não é válido")
                    break
                print("Cartão registrado!")
            if cntopcao == 2:
                nmr_cartao_debito = input("Digite o número do cartão: ")
                titular = input("Nome do titular: ")
                cdg_seguranca = input("Código de segurança: ") 
                if cdg_seguranca >= 1 and cdg_seguranca <= 999:
                    dtvalidade = input("Digite a data de validade no formato MM/AAAA: ")
                    mes_validade, ano_validade = dtvalidade.split('/') 
                    mes_validade = int(mes_validade)
                    ano_validade = int(ano_validade)
                    validade = dtatual.year - ano_validade - (dtatual.month < mes_validade)
                    if validade <= 0: 
                        print("O cartão não é válido")
                        break
                    print("Cartão registrado!")
                else:
                    print("Código inválido!")
                    break
            elif cntopcao == 3: 
                print("Um boleto foi enviado para o seu e-mail.")
            elif cntopcao == 4:
                print("A chave para realizar o pix foi enviado para o seu e-mail.")
            else: 
                print("Digite uma opção válida!")

