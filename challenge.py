# Para o cliente confirmar se o que informou está correto
def Confirmacao():
    print('\nAs informações estão corretas? \n1 - Sim \n2 - Não')
    confirm = int(input('\nSelecione uma opção: '))
    return confirm

# Mostrar os tipos de seguro
def TipoSeguro():
        print('\nEssas são as opções de seguro disponibilizadas pela nossa empresa')
        print("\n1- Para ciclistas que pedalam na rua"
                    + "\n2- Para ciclistas de maratona"
                    + "\n3- Para ciclistas que pedalam em montanhas"
                    + "\n4- Para ciclistas que pedalam em pedras e rochas"
                    + "\n5- Para ciclistas que pedalam em terra e mato"
                    + "\n6- Para ciclistas por hobbie"
                    +"\n7- Para ciclistas que viajam com a bike")
        
# Para identificar o cliente no sistema
def IdentificarCliente():
    opcRegistro = 2
    while opcRegistro == 2:
        cpf = input("Digite seu CPF: ")
        opcRegistro = int(input(f"O CPF {cpf} está correto? \n1 - Sim \n2 - Não \nEscolha uma opção: "))
        
        if opcRegistro == 1:
            tuplaCPF = (cpf)
            print(f"O CPF {tuplaCPF} foi gravado com sucesso!")

# Para enviar as fotos e vídeos para a vistoria
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
        while confirmFoto == 2:
            print("Repita o processo")
            print("\n x - Foto do número de série")
            confirmFoto = Confirmacao()
        if confirmFoto == 1:
            print("\nFoto adicionada")
        
        print("\n x- Foto da roda")
        confirmFoto = Confirmacao()
        while confirmFoto == 2:
            print("Repita o processo")
            print("\n x- Foto da roda")
            confirmFoto = Confirmacao()
        if confirmFoto == 1:
            print("\nFoto adicionada.")

        print("\n x- Foto dos freios")
        confirmFoto = Confirmacao()
        while confirmFoto == 2: 
            print("Repita o processo")
            print("\n x- Foto dos freios")
            confirmFoto = Confirmacao()
        if confirmFoto == 1:
            print("\nFoto adicionada.")
        
        print("\n x- Foto do guidão")
        confirmFoto = Confirmacao()
        while confirmFoto == 2:
            print("Repita o processo")
            print("\n x- Foto do guidão")
            confirmFoto = Confirmacao()
        if confirmFoto == 1:
            print("\nFoto adicionada.")

        print("\n x- Foto dos pedais")
        confirmFoto = Confirmacao()
        while confirmFoto == 2:
            print("Repita o processo")
            print("\n x- Foto dos pedais")
            confirmFoto = Confirmacao()
        if confirmFoto == 1:
            print("\nFoto adicionada.")
        
        print("\n x- Foto da corrente")
        confirmFoto = Confirmacao()
        while confirmFoto == 2:
            print("Repita o processo")
            print("\n x- Foto da corrente")
            confirmFoto = Confirmacao()
        if confirmFoto == 1:
            print("\nFoto adicionada.")

        print("\n x- Foto sua com a bike")
        confirmFoto = Confirmacao()
        while confirmFoto == 2:
            print("Repita o processo")
            print("\n x- Foto sua com a bike")
            confirmFoto = Confirmacao()
        if confirmFoto == 1:
            print("\nFoto adicionada.")

        print("\n x- Foto da bike de frente")
        confirmFoto = Confirmacao()
        while confirmFoto == 2:
            print("Repita o processo")
            print("\n x- Foto da bike de frente")
            confirmFoto = Confirmacao()
        if confirmFoto == 1:
            print("\nFoto adicionada.")

        print("\n x- Foto dos acessórios (se for visível)")
        confirmFoto = Confirmacao()
        while confirmFoto == 2:
            print("Repita o processo")
            print("\n x- Foto dos acessórios (se for visível)")
            confirmFoto = Confirmacao()
        if confirmFoto == 1:
            print("\nFoto adicionada.")

        print("\nClique no x para adicionar os vídeos: ")

        print("\nx -Vídeo mostrando a bike completa")
        confirmFoto = Confirmacao()
        while confirmFoto == 2: 
            print("Repita o processo")
            print("\nx -Vídeo mostrando a bike completa")
            confirmFoto = Confirmacao()
        if confirmFoto == 1:
            print("\nVídeo adicionado.")

        print("\nx -Vídeo mostrando com mais ênfase cada ponto chave que foi tirado foto")
        confirmFoto = Confirmacao()
        while confirmFoto == 2:
            print("Repita o processo")
            print("\nx -Vídeo mostrando com mais ênfase cada ponto chave que foi tirado foto")
            confirmFoto = Confirmacao()
        if confirmFoto == 1:
            print("\nVídeo adicionado.")
        
#Iniciar o processo de vistoria
def Vistoria():
    aprovado = False
    reprovado = False
    emAnalise = True
    faltandoDocs = False

    IdentificarCliente()

    RegistroSeguro()

    print("\nPara finalizar a vistoria é necessário que sejam tiradas: " + 
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
    print("\nObservação: neste momento, como ainda não é possível enviar fotos e vídeos, esta parte não é totalmente funcional")
    
    MidiaVistoria()
    
    print("\nOs seus dados foram enviados para vistoria. Você pode acompanhar o atual status da análise pelo seu e-mail ou aqui pelo site.")
    status =  True
    print("\nDeseja conferir o status da análise da vistoria?")
    confirmVistoria = int(input("\n1 - Sim \n2 - Não \nSelecione uma opção: "))
    if confirmVistoria == 1: 
        if aprovado == True:
            print("\nSeus dados foram aprovados! Agora assine a apólice.")
        elif reprovado == True:
            print("\nSeus dados foram reprovados. Refaça o processo de vistoria.")
        elif emAnalise == True:
            print("\nSeus dados estão em análise. Confira novamente mais tarde.")
        elif faltandoDocs == True:
            print("\nEstá faltando documentos para realizar a vistoria. Revise seus dados.")
    else:
        print(f"{emAnalise}")

# Informa o status de vistoria
def Status():
    faltandoDocs = False
    reprovado = False
    aprovado = False
    emAnalise = True
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
        print("Voltando ao menu")
    print("\nOk. Acompanhe no seu email ou nessa tela o atual status da sua vistoria para saber as informações de como prosseguir.")

    return emAnalise

# Para escolher um tipo de seguro        
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
                    
        except ValueError:
            print("Digite um número válido!")
            
    return confirma
      
# Para perguntar a nota do fedback
def Nota():
    nota = 0
    while nota != -1:
        nota = int(input("Qual a sua nota para esse serviço? (0 - 10): "))
        if nota < 0 or nota > 10:
            print("\nNota incorreta, tente novamente...\n")
            nota = 1
        else:
            tuplaNota = (nota)
            nota = -1
            return f"A nota {tuplaNota} foi gravada com sucesso!"    
    
# Menu de opções
opcaomenu = 0
while opcaomenu != 7:
    print("\nOlá, em que a Technobike pode teseguro para a bike")
    print("1 - Tipo de seguro")
    print("2 - Iniciar processo de vistoria")
    print("3 - Status da vistoria")
    print("4 - Feedback")
    print("5 - Encerrar programa")
    opcaomenu = int(input("\nSelecione uma das opções acima: "))
    match opcaomenu:

# Tipos de seguro
        case 1: 
            # opcSeguro = 0
            # while opcSeguro < 1 or opcSeguro > 7:
            TipoSeguro()
                        
# Vistoria
        case 2:
            Vistoria()
            
# Status da vistoria
        case 3: 
            Status()
            
# Feedback
        case 4:
            opcaofb = [
                {"motivo": "Tempo para fazer vistoria", "nota": None},
                {"motivo": "Serviços fornecido", "nota": None},
                {"motivo": "Problemas", "nota": None},
                {"motivo": "Atendimento", "nota": None},
                {"motivo": "Resolução de dúvidas", "nota": None}
]           

            for feedback in opcaofb:
                motivo = feedback["motivo"]
                print(f"\n{motivo}")
                feedback["nota"] = Nota()
                print("Feedback enviado")
                print(f"Nota: {feedback['nota']}")

## Encerrar o programa
        case 5:
            print("\nEncerrando, até a próxima!")
            break            
            
            