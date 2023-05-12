
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

def Confirmacao():
    confirm = int(input('1 - Sim \n2 - Não \nAs informações estão corrtas?: '))
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
                print('\nCadastro realizado')
            else:
                print('\nFaça novamente o cadastro')    
                seguro = 0

        except ValueError:
            print("Digite um número válido!")
            seguro = 0
        return seguro
      

    
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
        case 3: 
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
        case 4:
            print("\nRelatório dos dados adcionados: ")
            if opcSeguro == 1:
               print(f'Opção de Seguro: {seg1}')
            if opcSeguro == 2:
               print(f'Opção de Seguro: {seg2}')
            if opcSeguro == 3:
               print(f'Opção de Seguro: {seg3}')
            if opcSeguro == 4:
               print(f'Opção de Seguro: {seg4}')
            if opcSeguro == 5:
               print(f'Opção de Seguro: {seg5}')
            if opcSeguro == 6:
               print(f'Opção de Seguro: {seg6}')
            if opcSeguro == 7:
               print(f'Opção de Seguro: {seg7}')


            elif opcSeguro == 0:
                print("Nenhum cadastro foi adicionado.")
            if registro_bike == 1:
                print(f"\nRelatório do registro da bike:  \nModelo: {modelo}")
                print(f"Número de série: {numserie}")
                print(f"Nota fiscal: {ntfiscal}")
                print(f"Cor: {cor}")
                if acessorios != 0:
                    print(f"Valor dos acessórios: {acessorios}")

#contrato 
        case 5:
            print("Revisando seus dados: ")
            if opcSeguro < 1:
                print("Primeiro realize o cadastro.")
            elif registro_bike != 1: 
                print("Primeiro realize o registro da bike.")
            else:
                print("\nTodos os dados estão corretos!")
               
            
