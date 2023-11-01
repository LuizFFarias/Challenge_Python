import re
import json
notas = []


def Confirmacao():
    """
    Esta função pede para o cliente confirmar se o que foi passado por ele está correto.
    """

    print('\nAs informações estão corretas?' 
          + '\n1 - Sim '
          + '\n2 - Não')
    confirm = int(input('\nSelecione uma opção: '))
    return confirm


def TratarCPF(cpf):
    """
    Esta função verifica se o CPF informado pelo usuário possui exatamente 11 dígitos numéricos
    """

    if re.match(r'^\d{11}$', cpf):
        return True
    else:
        return False


def TipoSeguro():
        """
        Esta função serve para mostrar os tipos de seguros disponibilizados pela TechnoBike
        """

        print('\nEssas são as opções de seguro disponibilizadas pela nossa empresa: '
                    + '\n1- Para ciclistas que pedalam na rua'
                    + '\n2- Para ciclistas de maratona'
                    + '\n3- Para ciclistas que pedalam em montanhas'
                    + '\n4- Para ciclistas que pedalam em pedras e rochas'
                    + '\n5- Para ciclistas que pedalam em terra e mato'
                    + '\n6- Para ciclistas por hobbie'
                    + '\n7- Para ciclistas que viajam com a bike'
                    + '\n--------------------------------------------')


def IdentificarCliente():
    """
    Esta função salva o CPF do cliente no sistema
    """
    
    while True:
        arquivo = open('clientesvistoria.txt', 'a')
        cpf = input('\nDigite seu CPF: ')
        
        if TratarCPF(cpf):
            arquivo.write(cpf + '\n')
            arquivo.close()

            if VerificarCPF(cpf):
                break
        else:
            print(f'CPF {cpf} inválido. Tente novamente!')


def VerificarCPF(cpf):
    """
    Esta função verifica se o CPF informado pelo usuário existe no sistema para que ele possa prosseguir com sua vistoria
    """
    
    with open('clientesvistoria.txt', 'r') as arquivo:
        linhas = arquivo.readlines()
        cpfs = [linha.strip() for linha in linhas]
    
    if cpf in cpfs:
        print(f'O CPF {cpf} foi encontrado. Seja bem vindo!')
        return True
    else:
        print(f'O cpf {cpf} não foi encontrado no sistema. Tente novamente!')
        return False
        

def RegistroSeguro():
    """
    Esta função apresenta os tipos de seguro disponibilizados pela TechnoBike e pergunta qual destes o cliente quer
    """

    while True:
        TipoSeguro()
        seguro = int(input('\nQual dessas opções combina mais com seu estilo? '))
        
        try:
            if seguro < 1 or seguro > 7:
                print('\nDigite uma opção válida!')

            confirma = Confirmacao()
            if confirma == 1:
                print('\nSeguro selecionado!')
                break
            elif confirma == 2:
                print('\nEscolha novamente o seguro!')
                    
        except ValueError:
            print("Digite um número válido!")


def MidiaVistoria():
        """
        Esta função simula o envio das fotos e vídeos para a vistoria
        """
        
        print('\nClique no x para adicionar a foto: ')
        print('-----------------------------------------')
        
        try:
            print('\n x- Foto da bike inteira de lado')
            confirmFoto = Confirmacao()
        
            if confirmFoto == 1:
                print('\nFoto adicionada.')
            elif confirmFoto == 2:
                print('Repita o processo')
                print('\n x- Foto da bike inteira de lado')
                confirmFoto = Confirmacao()
            else:
                print('\nDigite um número válido!')
        
        except ValueError:
            print('\nDigite um número válido!')

        try:
            print('\n x- Foto do número de série')
            confirmFoto = Confirmacao()
        
            if confirmFoto == 1:
                print('\nFoto adicionada')
            elif confirmFoto == 2:
                print('Repita o processo')
                print('\n x - Foto do número de série')
                confirmFoto = Confirmacao()
            else:
                print('\nDigite um número válido!')
        
        except ValueError:
            print('\nDigite um número válido!')


        try:
            print('\n x- Foto da roda')
            confirmFoto = Confirmacao()

            if confirmFoto == 1:
                print('\nFoto adicionada.')
            elif confirmFoto == 2:
                print('Repita o processo')
                print('\n x- Foto da roda')
                confirmFoto = Confirmacao()
            else:
                print('\nDigite um número válido!')
        
        except ValueError:
            print('\nDigite um número válido!')

        try:
            print('\n x- Foto dos freios')
            confirmFoto = Confirmacao()
            
            if confirmFoto == 1:
                print('\nFoto adicionada.')
            elif confirmFoto == 2: 
                print('Repita o processo')
                print('\n x- Foto dos freios')
                confirmFoto = Confirmacao()
            else:
                print('\nDigite um número válido!')
        
        except ValueError:
            print('\nDigite um número válido!')

        try:
            print('\n x- Foto do guidão')
            confirmFoto = Confirmacao()

            if confirmFoto == 1:
                print('\nFoto adicionada.')
            elif confirmFoto == 2:
                print('Repita o processo')
                print('\n x- Foto do guidão')
                confirmFoto = Confirmacao()
            else:
                print('\nDigite um número válido!')
        
        except ValueError:
            print('\nDigite um número válido!')

        try:
            print('\n x- Foto dos pedais')
            confirmFoto = Confirmacao()

            if confirmFoto == 1:
                print('\nFoto adicionada.')
            elif confirmFoto == 2:
                print('Repita o processo')
                print('\n x- Foto dos pedais')
                confirmFoto = Confirmacao()
            else:
                print('\nDigite um número válido!')
        
        except ValueError:
            print('\nDigite um número válido!')
            
        try:
            print('\n x- Foto da corrente')
            confirmFoto = Confirmacao()
            if confirmFoto == 1:
                print('\nFoto adicionada.')
            elif confirmFoto == 2:
                print('Repita o processo')
                print('\n x- Foto da corrente')
                confirmFoto = Confirmacao()
            else:
                print('\nDigite um número válido!')
        
        except ValueError:
            print('\nDigite um número válido!')

        try:
            print('\n x- Foto sua com a bike')
            confirmFoto = Confirmacao()
            
            if confirmFoto == 1:
                print('\nFoto adicionada.')
            elif confirmFoto == 2:
                print('Repita o processo')
                print('\n x- Foto sua com a bike')
                confirmFoto = Confirmacao()
            else:
                print('\nDigite um número válido!')
        
        except ValueError:
            print('\nDigite um número válido!')

        try:
            print('\n x- Foto da bike de frente')
            confirmFoto = Confirmacao()
            
            if confirmFoto == 1:
                print('\nFoto adicionada.')
            elif confirmFoto == 2:
                print('Repita o processo')
                print('\n x- Foto da bike de frente')
                confirmFoto = Confirmacao()
            else:
                print('\nDigite um número válido!')
        
        except ValueError:
            print('\nDigite um número válido!')

        try:
            print('\n x- Foto dos acessórios (se for visível)')
            confirmFoto = Confirmacao()
            
            if confirmFoto == 1:
                print('\nFoto adicionada.')
            elif confirmFoto == 2:
                print('Repita o processo')
                print('\n x- Foto dos acessórios (se for visível)')
                confirmFoto = Confirmacao()
            else:
                print('\nDigite um número válido!')
        
        except ValueError:
            print('\nDigite um número válido!')

 
            print('\nClique no x para adicionar os vídeos: ')


        try:
            print('\nx -Vídeo mostrando a bike completa')
            confirmFoto = Confirmacao()
            
            if confirmFoto == 1:
                print('\nVídeo adicionado.')
            elif confirmFoto == 2: 
                print('Repita o processo')
                print('\nx -Vídeo mostrando a bike completa')
                confirmFoto = Confirmacao()
            else:
                print('\nDigite um número válido!')
        
        except ValueError:
            print('\nDigite um número válido!')

        try:
            print('\nx -Vídeo mostrando com mais ênfase cada ponto chave que foi tirado foto')
            confirmFoto = Confirmacao()
            
            if confirmFoto == 1:
                print('\nVídeo adicionado.')
            elif confirmFoto == 2:
                print('Repita o processo')
                print('\nx -Vídeo mostrando com mais ênfase cada ponto chave que foi tirado foto')
                confirmFoto = Confirmacao()
            else:
                print('\nDigite um número válido!')
        
        except ValueError:
            print('\nDigite um número válido!')



def Vistoria():
    """
    Esta função inicia, de fato, o processo de vistoria
    Ela chama a função de identificar o cliente, de registrar o tipo de seguro, de enviar as mídias da vistoria e deixa conferir o status da vistoria ao fim
    """
    
    aprovado = False
    reprovado = False
    emAnalise = True
    faltandoDocs = False

    IdentificarCliente()
        
    RegistroSeguro()

    print('\n-------------------------------------------')
    print('Para finalizar a vistoria é necessário que sejam tiradas: '
            + '\n-Foto da bike inteira de lado'
            + '\n-Foto do número de série'
            + '\n-Foto da roda'
            + '\n-Foto dos freios'
            + '\n-Foto do guidão'
            + '\n-Foto dos pedais'
            + '\n-Foto da corrente'
            + '\n-Foto sua com a bike'
            + '\n-Foto da bike de frente'
            + '\n-Foto dos acessórios (se for visível)'
            + '\n-Vídeo mostrando a bike completa'
            + '\n-Vídeo mostrando com mais ênfase cada ponto chave que foi tirado foto')
    print('\nObservação: neste momento, como ainda não é possível enviar fotos e vídeos, esta parte não é totalmente funcional')
    print('-----------------------------------')
   
    MidiaVistoria()
    
    print('\nOs seus dados foram enviados para vistoria. Você pode acompanhar o atual status da análise pelo seu e-mail ou aqui pelo site.')
    print('------------------------------')
    print('\nDeseja conferir o status da análise da vistoria?')
    confirmVistoria = int(input('\n1 - Sim'
                            + '\n2 - Não'
                            + '\nSelecione uma opção: '))

    if confirmVistoria == 1: 
        if aprovado == True:
            print('\nSeus dados foram aprovados!')
        elif reprovado == True:
            print('\nSeus dados foram reprovados. Refaça o processo de vistoria!')
        elif emAnalise == True:
            print('\nAguarde um pouco. Seus dados estão em análise!')
        elif faltandoDocs == True:
            print('\nEstá faltando documentos para realizar a vistoria. Revise seus dados!')
    elif confirmVistoria == 2:
        print('\nOk! Você pode acompanhar no seu email ou voltar aqui para conferir o atual status da sua vistoria.')
    else:
        print('Opção incorreta. Tente novamente!')


def Status():
    """
    Esta função informa o status da vistoria a partir da busca de seu CPF no sistema
    """
    
    faltandoDocs = False
    reprovado = False
    aprovado = False
    emAnalise = True

    cpf = input('\nDigite seu CPF: ')
    
    if VerificarCPF(cpf):
        print('\nOs seus dados foram enviados para vistoria. Você pode acompanhar o atual status da análise pelo seu e-mail ou aqui pelo site.')
        print('\nDeseja conferir o status da análise da vistoria?')
        confirmVistoria = int(input('\n1 - Sim'
                                  + '\n2 - Não' 
                                  + '\nSelecione uma opção: '))
        if confirmVistoria == 1: 
            if aprovado:
                print('Seus dados foram aprovados!')
            elif reprovado:
                print('Seus dados foram reprovados. Refaça o processo de vistoria!')
            elif emAnalise:
                print('\nSeus dados estão em análise!')
            elif faltandoDocs:
                print('Está faltando documentos para realizar a vistoria. Revise seus dados!')
        elif confirmVistoria == 2:
            print('\nOk! Você pode acompanhar no seu email ou voltar aqui para conferir o atual status da sua vistoria.')
        else:
            print('Opção incorreta. Tente novamente!')
        return emAnalise

      
def Nota():
    """
    Esta função pergunta o feedback do cliente em relação à TechnoBike
    """
    
    while True:
        try:
            nota = int(input('Qual a sua nota para esse serviço? (0 - 10): '))
            if 0 <= nota <= 10:
                notas.append(nota)
                return nota
            else:
                print('\nNota inválida. Por favor, Insira uma nota entre 0 e 10!')
        except ValueError:
            print('\nNota inválida. Por favor, insira um número entre 0 e 10!')


#Menu
while True:
    """
    Menu com as funcionalidades do sistema
    """
    
    print('\nOlá, em que a Technobike pode te ajudar?')
    print('1 - Tipo de seguro')
    print('2 - Iniciar processo de vistoria')
    print('3 - Conferir status da vistoria')
    print('4 - Feedback')
    print('5 - Encerrar programa')

    try:
        opcaomenu = int(input('\nSelecione uma das opções acima: '))
    except ValueError:
        print('O valor deve ser um número inteiro')
        continue
    
    match opcaomenu:

#Tipos de seguro
        case 1: 
            TipoSeguro()


#Iniciar processo de vistoria
        case 2:
            Vistoria()
            

#Conferir status da vistoria
        case 3: 
            Status()


# Feedback
        case 4:
            feedbacks = {
                '--Tempo para fazer a vistoria': None,
                '--Servicos fornecidos': None,
                '--Problemas': None,
                '--Atendimento': None,
                '--Resolucao de duvidas': None
            }          

            for motivo, _ in feedbacks.items():
                print(f'\n{motivo}')
                feedbacks[motivo] = Nota()
                print(f'Nota {feedbacks[motivo]} enviada com sucesso!')
            
            notas = list(feedbacks.values())
            media = sum(notas)/ len(notas)
            print(f'\nA sua média de satisfação com a Technobike é de {media}. Muito obrigado!')

            with open('feedbacks.json', 'w') as arquivo:
                json.dump(feedbacks, arquivo, indent = 4) 


## Encerrar o programa
        case 5:
            print('\nFim de programa, até a próxima!')
            break            


## Para opções incorretas   
        case _:
            print('\nOpção incorreta')