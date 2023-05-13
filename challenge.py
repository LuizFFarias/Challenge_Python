
import datetime
i = 0
#Tipo de Seguro
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


#bike
numserie = 0
modelo = 0
valorbike = 0
cor = 0
ntfiscal = 0
acessorios = 0
#feedback
fbescolha = 0
fbtempo = 0
fbservicos = 0
fbproblemas = 0
fbatendimentos = 0
fbduvidas = 0
#relatório
cadastro = 0
registro_bike = 0

def Confirmacao():
    confirm = int(input('\n1 - Sim \n2 - Não \nAs informações estão corretas?: '))
    return confirm

def TipoSeguro():
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
            else:
                print('\nEscolha novamente o seguro!')    
                seguro = 0

        except ValueError:
            print("Digite um número válido!")
            seguro = 0
        return seguro
def RegistroBike():
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
    rgopcao = Confirmacao()
    if rgopcao == 1:
        print("\nRegistro realizado.")
    else:
        print("\nFaça novamente o registro.")
    return rgopcao

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



      

    
print("Olá, em que a Technobike pode te ajudar hoje?")

while opcao != 6:
    print("\n1 - Escolha do tipo de Seguro para a bike")
    print("2 - Registrar bike")
    print("3 - Feedback")
    print("4 - Relatório")
    print("5 - Contrato")
    print("6 - Encerrar")
    opcao = int(input("\nSelecione uma das opções acima: "))
    match opcao:
        case 6:
          print("\nEncerrando, até a próxima!")
          break

#Tipo de seguro
        case 1: 
            opcSeguro = 0
            while opcSeguro < 1 or opcSeguro > 7:
                opcSeguro = TipoSeguro()
            
            
            
                
#registro da bike

        case 2:
            registro = 2
            while registro == 2:
                registro = RegistroBike()
            registro_bike = 1 
            
#feedback
        case 3: 
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
                        case 2:
                            fbescolha = 2
                            while fbescolha == 2:
                                fbescolha, fbservicos = Feedback()
                        case 3:
                            fbescolha = 2
                            while fbescolha == 2:
                                fbescolha, fbproblemas = Feedback()
                        case 4:
                            fbescolha = 2
                            while fbescolha == 2:
                                fbescolha, fbatendimentos = Feedback()
                        case 5:
                            fbescolha = 2
                            while fbescolha == 2:
                                fbescolha, fbduvidas = Feedback()
                        case 6:
                            print('\nVoltando para o menu')
                        case _:
                            print("Escolha uma opção válida!")  
                except ValueError:
                    print("Formato de escolha incorreta!")
                    nmrinvalido = 1

#Relatório
        case 4:
            print("\nRelatório dos dados adcionados: ")
            TpSeguro_Relatorio(seg1, seg2, seg3, seg4, seg5, seg6, seg7)
            

            if registro_bike == 1:
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
                

#contrato 
        case 5:
            print("Revisando seus dados: ")
            if opcSeguro == 0:
                print("Primeiro escolha o tipo de seguro.")
            elif registro_bike != 1: 
                print("Primeiro realize o registro da bike.")
            else:
                print("\nTodos os dados estão corretos!")
               
            
