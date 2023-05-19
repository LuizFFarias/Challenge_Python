import datetime
i = 0

#Tipo de seguro
dtatual = datetime.datetime.now()
cont = 0
opcao = 0
seg1 = '1- Para ciclistas que pedalam na rua'
seg2 = '2- Para ciclistas de maratona'
seg3 = '3- Para ciclistas que pedalam em montanhas'
seg4 = '4- Para ciclistas que pedalam em pedras e rochas'
seg5 = '5- Para ciclistas que pedalam em terra e mato'
seg6 = '6- Para ciclistas por hobbie'
seg7 = '7- Para ciclistas que viajam com a bike'
opcSeguro = 0

#Dados do cliente
nome = 0
email = 0
rg = 0
cnh = 0
cpf = 0
telefone = 0
endereco = 0
cep = 0
bairro = ''
numresidencia = 0
complemento = ""
cidade = ""
estado = ""
pais = ""
cadastro = 0
confCli = 0

#Bike
numserie = 0
modelo = 0
valorbike = 0
cor = 0
ntfiscal = 0
acessorios = 0
registro = 0

#Vistoria
aprovado = 0
reprovado = 0
emAnalise = 0
faltandoDocs = True

#Feedback
fbescolha = 0
fbtempo = 0
fbservicos = 0
fbproblemas = 0
fbatendimentos = 0
fbduvidas = 0

#Relatório
cadastro = 0
registro_bike = 0

#Para o cliente confirmar se o que informou está correto
def Confirmacao():
    print('\nAs informações estão corretas? \n1 - Sim \n2 - Não')
    confirm = int(input('\nSelecione uma opção: '))
    return confirm

#Mostrar os tipos de seguro
def TipoSeguro():
        print('\nEssas são as opções de seguro disponibilizadas pela nossa empresa')
        print("\n1- Para ciclistas que pedalam na rua"
                    + "\n2- Para ciclistas de maratona"
                    + "\n3- Para ciclistas que pedalam em montanhas"
                    + "\n4- Para ciclistas que pedalam em pedras e rochas"
                    + "\n5- Para ciclistas que pedalam em terra e mato"
                    + "\n6- Para ciclistas por hobbie"
                    +"\n7- Para ciclistas que viajam com a bike")
        
        # try:
        #     seguro = int(input('\nQual dessas opções combina mais com seu estilo?: '))
        #     if seguro < 1 or seguro > 7:
        #         print("\nDigite um número válido!")
        #     confirma = Confirmacao()
        #     if confirma == 1:
        #         print('\nSeguro selecionado')
        #     else:
        #         print('\nEscolha novamente o seguro!')    
        #         seguro = 0

        # except ValueError:
        #     print("Digite um número válido!")
        #     seguro = 0
        # return seguro

#Para escolher um tipo de seguro        
def RegistroSeguro():
    confirma = 2
    while confirma != 1:
        print('\nEssas são as opções de seguro disponibilizadas pela nossa empresa')
        print("\n1- Para ciclistas que pedalam na rua"
                    + "\n2- Para ciclistas de maratona"
                    + "\n3- Para ciclistas que pedalam em montanhas"
                    + "\n4- Para ciclistas que pedalam em pedras e rochas"
                    + "\n5- Para ciclistas que pedalam em terra e mato"
                    + "\n6- Para ciclistas por hobbie"
                    +"\n7- Para ciclistas que viajam com a bike")
        
        try:
            seguro = int(input('\nQual dessas opções combina mais com seu estilo?: '))
            if seguro < 1 or seguro > 7:
                print("\nDigite um número válido!")
            confirma = Confirmacao()
            if confirma == 1:
                print('\nSeguro selecionado')
            elif confirma == 2:
                print('\nEscolha novamente o seguro!')    
                seguro = 0
        except ValueError:
            print("Digite um número válido!")
            seguro = 0 
            return confirma

#Para pegar as informações do cliente
def RegistroCliente():
    complemento = ""
    rg = ""
    cnh = 0
    cdopcao4 = 2

    while cdopcao4 != 1:
        nome = input("\nDigite seu nome: ")
        email = input("\nInforme seu email: ")
        print("\n1 - RG")
        print("2 - CNH")
        cdopcao2 = int(input("\nSelecione uma opção: "))
        if cdopcao2 == 1:
                rg = input("\nDigite seu RG: ")
        elif cdopcao2 == 2: 
                cnh = int(input("\nDigite sua CNH: "))
        cpf = input("Digite seu CPF: ")
        pais = input("Informe o seu país: ")
        estado = input("Informe seu estado: ")
        cidade = input("Informe sua cidade: ")
        cep = int(input("Informe seu cep: "))
        bairro = input("Informe seu bairro: ")
        endereco = input("Informe sua rua: ")
        numresidencia = int(input("Informe o número da residência: "))
        
        print("\nÉ necessário complemento? \n1 - Sim \n2 - Não")
        cdopcao3 = int(input("\nSelecione uma opção: "))
        if cdopcao3 == 1:
            complemento = input("Informe o complemento: ")

        if cdopcao2 == 1:
                print(f" \nNome: {nome}")
                print(f"RG: {rg}")
                print(f"CPF: {cpf}")
                print(f"Endereço: {endereco} {numresidencia}  {complemento}")
                cdopcao4 = Confirmacao()
                if cdopcao4 == 1:
                    print("Cadstro realizado.")
        if cdopcao2 == 2:
                print(f"Nome: {nome}")
                print(f"CNH: {cnh}")
                print(f"CPF: {cpf}")
                print(f"Endereço: {endereco} {numresidencia}  {complemento}")
                cdopcao4 = Confirmacao()
                if cdopcao4 == 1:
                    print("\nCadstro realizado.")
                elif cdopcao4 == 2:
                    print("Faça novamente o cadastro.")
                else:
                    print("\nDigite um número válido!")
    return cdopcao4, cdopcao2
            
#Para pegar as informações do bike
def RegistroBike():
    rgopcao = 2

    while rgopcao != 1:
        modelo = input("\nInforme o modelo da bike: ")
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
                print(f'Valor total: R${valorbike + acessorios}')
        rgopcao = Confirmacao()

        if rgopcao == 1:
            print("\nRegistro realizado.")
        else:
            print("\nFaça novamente o registro.")
    return rgopcao

#Para enviar as fotos e vídeos para a vistoria
def MidiaVistoria():
        print("\nClique no x para adicionar a foto: ")
        
        print("\n x- Foto da bike inteira de lado")
            
        confirmFoto = Confirmacao()
        while confirmFoto == 2:
            print("Repita o processo")
            print("\n x- Foto da bike inteira de lado")
            confirmFoto = Confirmacao()
        if confirmFoto == 1:
            print("\nFoto adicionada.")
            
                    
            
        print("\n x- Foto do número de série")
        confirmFoto = Confirmacao()
        if confirmFoto == 1:
            print("\nFoto adicionada.")
        else: 
            print("Repita o processo")
        print("\n x- Foto da roda")
        confirmFoto = Confirmacao()

        if confirmFoto == 1:
            print("\nFoto adicionada.")
        else: 
            print("Repita o processo")
        print("\n x- Foto dos freios")
        confirmFoto = Confirmacao()

        if confirmFoto == 1:
            print("\nFoto adicionada.")
        else: 
            print("Repita o processo")
        print("\n x- Foto do guidão")
        confirmFoto = Confirmacao()

        if confirmFoto == 1:
            print("\nFoto adicionada.")
        else: 
            print("Repita o processo")
        print("\n x- Foto dos pedais")
        confirmFoto = Confirmacao()

        if confirmFoto == 1:
            print("\nFoto adicionada.")
        else: 
            print("Repita o processo")
        print("\n x- Foto da corrente")
        confirmFoto = Confirmacao()

        if confirmFoto == 1:
            print("\nFoto adicionada.")
        else: 
            print("Repita o processo")
        print("\n x- Foto sua com a bike")
        confirmFoto = Confirmacao()

        if confirmFoto == 1:
            print("\nFoto adicionada.")
        else: 
            print("Repita o processo")
        print("\n x- Foto da bike de frente")
        confirmFoto = Confirmacao()

        if confirmFoto == 1:
            print("\nFoto adicionada.")
        else: 
            print("Repita o processo")
        print("\n x- Foto dos acessórios (se for visível)")
        confirmFoto = Confirmacao()

        if confirmFoto == 1:
            print("\nFoto adicionada.")
        else: 
            print("Repita o processo")
        print("\nClique no x para adicionar os vídeos: ")
        print("\nx -Vídeo mostrando a bike completa")
        confirmFoto = Confirmacao()

        if confirmFoto == 1:
            print("\nVídeo adicionado.")
        else: 
            print("Repita o processo")
        print("\nx -Vídeo mostrando com mais ênfase cada ponto chave que foi tirado foto")
        confirmFoto = Confirmacao()

        if confirmFoto == 1:
            print("\nVídeo adicionado.")
        else: 
            print("Repita o processo")

#Para informar um feedback
def Feedback():
    fb = input("\nEscreva seu feedback: ")
    fbopcao2 = Confirmacao()
    if fbopcao2 == 1:
        print("Feedback enviado!")
    elif fbopcao2 == 2:
        print("Feedbck cancelado!")
    else:
        print("Digite uma opção válida!")
    return fbopcao2, fb

#Para mostrar o tipo de seguro escolhido no relatório
def TpSeguro_Relatorio(seg1, seg2, seg3, seg4, seg5, seg6, seg7):
    match opcSeguro:
        case 1:
            print(f'Opção de Seguro: {seg1}')
        case 2:
            print(f'Opção de Seguro: {seg2}')
        case 3:
            print(f'Opção de Seguro: {seg3}')
        case 4:
            print(f'Opção de Seguro: {seg4}')
        case 5:
            print(f'Opção de Seguro: {seg5}')
        case 6:
            print(f'Opção de Seguro: {seg6}')
        case 7:
            print(f'Opção de Seguro: {seg7}')
        case 0:
            print("\nNenhum seguro foi adicionado.")

#Para fazer um feedback
def FB_Relatorio(fbtempo, fbservicos, fbproblemas, fbatendimentos, fbduvidas):
    match fbopcao:
        case 1:
            print(fbtempo)
        case 2:
            print(fbservicos)
        case 3:
            print(fbproblemas)
        case 4:
            print(fbatendimentos)
        case 5:
            print(fbduvidas)

#Para mostrar o status da vistoria
def Apolice():
    if aprovado == True:
        print("A apólice foi enviada para o seu email. No seu email, foram enviadas instruções de como assinar a apólice e como enviar ela de volta para empresa.")
    elif reprovado == True:
        print("Sua apólice não foi emitida pois sua vistoria não foi aprovada.")
    elif emAnalise == True:
        print("Sua vistoria ainda está em análise.")
    elif faltandoDocs == True:
        print("Há arquivos reprovados. Confira quais são e reenvie eles.")

#Para emitir a apólice
def EmitirApolice():
    #pegar todos os dados do cliente, dados da bike, assinatura do cliente karaio
    print(f'Eu, {nome}, portador do rg nº {rg} e cpf nº{cpf}, morador do enedreço {endereco}  {numresidencia}  {complemento}, cep: {cep}' 
          +f'afirmo que escolhi o tipo de seguro {TpSeguro_Relatorio} e que os dados da bike modelo: {modelo}, cor: {cor}, valor total: R${valorbike + acessorios}, número de série: {numserie}, nota fiscal: {ntfiscal}, são verdadeiros. Tenho ciência da veracidade e da importância da prestação de informações corretas.'
          + 'Visto isso, eu concordo com a realização dessa vistoria e do seguro adquirido por mim')
    print('__ (assinatura do cliente) __ (assinatura da empresa) __(data)')
      
#Para perguntar a nota do fedback
def Nota():
    nota = int(input("Qual a sua nota para esse serviço? (0 - 10): "))
    return nota

    
#Menu de opções
while opcao != 6:
    print("\nOlá, em que a Technobike pode te ajudar hoje?")
    print("1 - Conheça os tipos de seguro para a bike")
    print("2 - Iniciar processo de vistoria")
    print("3 - Relatório")
    print("4 - Verificar status da vistoria")
    print("5 - Emissão da apólice")
    print("6 - Feedback")
    print("7 - Encerrar")
    opcao = int(input("\nSelecione uma das opções acima: "))
    match opcao:
        case 7:
          print("\nEncerrando, até a próxima!")
          break

#Tipo de seguro
        case 1: 
            # opcSeguro = 0
            # while opcSeguro < 1 or opcSeguro > 7:
            TipoSeguro()
            
            

#Vistoria
        case 2:
            registro = 2
            confSeguro = 2
            confCli = 2
            # while confSeguro == 2:
            confSeguro = RegistroSeguro()
            # while confCli == 2:
            confCli, rgcpf = RegistroCliente()
            # while registro == 2:
            registro = RegistroBike()
            registro_bike = 1 
            print("\nPara finalizar a vistoria é necessário que sejam tiradas: "+ 
                    "\n-Foto da bike inteira de lado"
                    + "\n-Foto do número de série"
                    + "\n-Foto da roda"
                    + "\n-Foto dos freios"
                    + "\n-Foto do guidão"
                    + "\n-Foto dos pedais"
                    + "\n-Foto da corrente"
                    + "\n-Foto sua com a bike"
                    + "\n-Foto da bike de frente"
                    + "\n-Foto dos acessórios (se for visível)"
                    + "\n-Vídeo mostrando a bike completa"
                    + "\n-Vídeo mostrando com mais ênfase cada ponto chave que foi tirado foto")
            
            MidiaVistoria()
            print("\nOs seus dados foram enviados para vistoria. Você pode acompanhar o atual status da análise pelo seu email ou aqui pelo site.")
            print("Deseja conferir o status da análise da vistoria?")
            confirmVistoria = int(input("\n1 - Sim \n2 - Não \nSelecione uma opção: "))
            if confirmVistoria == 1: 
                if aprovado == True:
                    print("Seus dados foram aprovados! Agora assine a apólice.")
                elif reprovado == True:
                    print("Seus dados foram reprovados. Refaça o processo de vistoria.")
                elif emAnalise == True:
                    print("Seus dados estão em análise. Confira novamente mais tarde.")
                elif faltandoDocs == True:
                    print("Está faltando documentos para realizar a vistoria. Revise seus dados.")
            else:
                print("Ok. Acompanhe no seu email ou nessa tela o atual status da sua vistoria para saber as informações de como prosseguir.")


        
#Relatório
        case 3:
            print("\nRelatório dos dados adcionados: ")
            TpSeguro_Relatorio(seg1, seg2, seg3, seg4, seg5, seg6, seg7)
            
            if confCli == 1:
                print(f"Nome: {nome}")
                if rgcpf ==1:
                    print(f"RG: {rg}")
                elif rgcpf == 2:
                    print(f"CNH: {cnh}")
                print(f"CPF: {cpf}")
                print(f"Endereço: {endereco} {numresidencia}  {complemento}")
            else:
                print(f'\nNenhum dado foi adicionado.')


            if registro == 1:
                print(f"\nRelatório do registro da bike:  \nModelo: {modelo}")
                print(f"Número de série: {numserie}")
                print(f"Nota fiscal: {ntfiscal}")
                print(f"Cor: {cor}")
                if acessorios != 0:
                    print(f"Valor dos acessórios: {acessorios}")
            else:
                print("\nNenhum registro foi adicionado.")
            
            if fbescolha == 1:
                print("FeedBack adicionado: ")
                FB_Relatorio(fbtempo, fbservicos, fbproblemas, fbatendimentos, fbduvidas)



#Status da vistoria
        case 4: 
            print("Os seus dados foram enviados para vistoria. Você pode acompanhar o atual status da análise pelo seu email ou aqui pelo site.")
            print("Deseja conferir o status da análise da vistoria?")
            confirmVistoria = int(input("\n1 - Sim \n2 - Não \nSelecione uma opção: "))
            if confirmVistoria == 1: 
                if aprovado == True:
                    print("Seus dados foram aprovados! Agora assine a apólice.")
                elif reprovado == True:
                    print("Seus dados foram reprovados. Refaça o processo de vistoria.")
                elif emAnalise == True:
                    print("Seus dados estão em análise. Confira novamente mais tarde.")
                elif faltandoDocs == True:
                    print("\nEstá faltando documentos para realizar a vistoria. Revise seus dados.")
            else:
                print("\nOk. Acompanhe no seu email ou nessa tela o atual status da sua vistoria para saber as informações de como prosseguir.")



#Apólice 
        case 5:
            Apolice()
               
            
            
#Feedback
        case 6: 
            print("\nQual o motivo do feedback? \n1 - Tempo de espera")
            print("2 - Serviços")
            print("3 - Problemas")
            print("4 - Atendimeto")
            print("5 - Dúvidas")
            print("6 - Voltar ao menu")
            fbescolha = 0 
            fbopcao = 0 
            while fbopcao < 1 or fbopcao > 6 or nmrinvalido == 1:
                nmrinvalido = 0
                try:
                    fbopcao = int(input("Selecione uma opção: "))
                    match fbopcao:
                        case 1:
                            fbescolha = 2
                            while fbescolha == 2:
                                fbescolha, fbtempo = Feedback()
                                ntTempo = Nota()
                        
                        case 2:
                            fbescolha = 2
                            while fbescolha == 2:
                                fbescolha, fbservicos = Feedback()
                                ntServicos = Nota()

                        case 3:
                            fbescolha = 2
                            while fbescolha == 2:
                                fbescolha, fbproblemas = Feedback()
                                ntProblema = Nota()

                        case 4:
                            fbescolha = 2
                            while fbescolha == 2:
                                fbescolha, fbatendimentos = Feedback()
                                ntAtendimento = Nota()

                        case 5:
                            fbescolha = 2
                            while fbescolha == 2:
                                fbescolha, fbduvidas = Feedback()
                                ntDuvidas = Nota()

                        case 6:
                            print('\nVoltando para o menu')

                        case _:
                            print("Escolha uma opção válida!") 

                except ValueError:
                    print("Formato de escolha incorreta!")
                    nmrinvalido = 1

        case 0:
            MidiaVistoria()