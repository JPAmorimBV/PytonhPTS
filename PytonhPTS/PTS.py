import os
import random

def iniciar():
    input('Precione ENTER para volar ao login.')
    os.system('cls')
    funcaoUsuario()


#Usuario 
def funcaoUsuario():
    usuarioC='JosinelRodriguesson'
    senhaC='12345678910'
    print('Bem vindo a Porto!\nFaça o login para acessar a plataforma!\n')
    user=input('Digite o nome do usuário: ')
    cemNha=input('Digite a senha: ')
    if user == usuarioC and cemNha == senhaC:
        print('Login bem sucedido!')
    else:
        print('Credenciais inválidas. Tente novamente.')
        iniciar()

def menu():
    os.system('cls')
    print('''Bem vindos a plataforma da Porto Seguro
        ''')
    print('''Escolha uma das opções abaixo para prosseguir
        ''')
    print('1 - Agendar revisão/mantenção veicular')
    print('2 - Solicitar um guincho')
    print('3 - Nossos seguros veiculares')
    print('4 - Identificar problemas usando IA')
    print('5 - Ouvidoria ')
    print('6 - Sair \n')
         
def voltar():
    input('Aperte ENTER para voltar ao menu principal')
    main()

def opcaoInvalida():
    print('Opção Invalida! \n')
    input('Aperte ENTER para voltar ao menu principal')
    main()

def faleConosco():
    print('Ouvidoria\n')
    print('Entre em contato com a gente! Nossos atendentes estão disponíveis 24h!')
    print('Telefone:(11)2213-6177')
    print('WhatsApp: (11)3003 9303')
    voltar()

def finalizar():
    input('Aperte ENTER para finalizar a sessão')
    os.system('cls')
    print('Sessão finalizada!')

def opcao_do_cliente():
   #opção agendar revisão
    opcao_cliente = int(input('Digite o número atribuido ao seguimento desejado: '))
    if opcao_cliente == 1:
        os.system('cls')
        print('Agendar revisão/manutenção veicular\n')
        print('Escolha uma opção para prosseguir\n') 
        print('1 - Escolher a data da revisão/manutenção veicular')
        print('2 - Voltar ao menu principal\n')
        manutencao=int(input('Escolha uma opção para prosseguir:'))
        
        if manutencao == 1:
            carro=input('Informe o modelo do seu veículo:')
            print('Escolha a localização dos nossos mecânicos parceiros:\n')
            print('1 - Lapa SP - OFICINA MOTOR POINT ')
            print('2 - Vila Plana SP - MVS Preparações')
            print('3 - Tatuapé SP -TPS Automotive')
            print('4 - Itaim Bibi SP - Shida Serviços Automotivos\n')
            localizacao=int(input('Escolha uma opção para prosseguir:'))
            
            if localizacao ==1:
                m1='Rua Faustolo, 834 - Lapa SP - OFICINA MOTOR POINT'
                hora=input('Digite o horário desejado(HH/MM): ')
                dia=input('Digite o dia e o mês desejados para marcar a sua revisão/manutenção veicular (DD/MM): ')
                print(f'Sua revisão/mantenção foi agendada com sucesso para o dia {dia} no horário {hora} na oficina {m1} para o carro {carro}')
                voltar()

            if localizacao ==2:
                m2=' Rua Amaro Antônio Rosa, 52 - Vila Plana SP - MVS Preparações'
                hora=input('Digite o horário desejado(HH/MM): ')
                dia=input('Digite o dia e o mês desejados para marcar a sua revisão/manutenção veicular (DD/MM): ')
                print(f'Sua revisão/mantenção foi agendada com sucesso para o dia {dia} no horário {hora} na oficina {m2} para o carro {carro}')
                voltar()
                
            if localizacao ==3:
                m3='Rua Serra de Bragança, 1638a - Tatuapé SP - TPS Automotive'
                hora=input('Digite o horário desejado(HH/MM): ')
                dia=input('Digite o dia e o mês desejados para marcar a sua revisão/manutenção veicular (DD/MM): ')
                print(f'Sua revisão/mantenção foi agendada com sucesso para o dia {dia} no horário {hora} na oficina {m3} para o carro {carro}')
                voltar() 
            
            if localizacao ==4:
                m4='Rua Clodomiro Amazonas, 1400 - Itaim Bibi SP - Shida Serviços Automotivos'
                hora=input('Digite o horário desejado(HH/MM): ')
                dia=input('Digite o dia e o mês desejados para marcar a sua revisão/manutenção veicular (DD/MM): ')
                print(f'Sua revisão/mantenção foi agendada com sucesso para o dia {dia} no horário {hora} na oficina {m4} para o carro {carro}')
                voltar()
        
        
        if manutencao == 2:
            main()

   #opção guincho
    elif opcao_cliente == 2:
        os.system('cls')
        print('Solicitar um guincho\n')
        print('Escolha uma opção para segprouir\n')
        print('1 - Informe sua localização')
        print('2 - Voltar ao menu principal\n')
        guincho=int(input('Escolha uma opção para prosseguir:'))
        if guincho == 1:
            guinchoLoca=input('Informe sua localização: ')
            num=random.randint(20,40)
            nomes=['Francisnelson Filho','Ambrósio Cardoso','Josinelso Mendes','Cícero Vieira','Altair Neto','Geórgio Oliveira']
            print(f'O motorista parceiro {random.choice(nomes)} chegará a {num} minútos da localização {guinchoLoca}')
            voltar()
        if guincho == 2: 
            main()

   #opção seguros         
    elif opcao_cliente == 3:
        os.system('cls')
        print('Nossos seguros veiculares\n')
        print('Escolha uma opção para prosseguir\n')
        print('1 - Ver planos')
        print('2 - Voltar ao menu principal\n')
        seguros=int(input('Escolha uma opção para prosseguir: '))
        if seguros == 1:
            
            def contratarS():
                email=input('Informe seu email: ')
                input('Digite os números do seu cartão:')
                input('Digite a data de vencimento do seu cartão: ')
                input('Digite o código de segurança do cartão: ')
                print(f'Um e-mail foi enviado para {email} formalizando o contrato e informando sobre as datas de pagamento.\nObrigado pela preferência!')
            
            print('Escolha uma opção de seguro para saber mais')
            print('1 - Porto Starter')
            print('2 - Porto Intermediate ')
            print('3 - Porto Premium')
            sugurus=int(input('Escolha uma opção para prosseguir'))
            if sugurus==1:
                print('Porto Starter\n')
                print(' Preço: R$ 800,00 por ano\nBenefícios:\n Cobertura contra roubo e furto\nAssistência 24 horas para guincho e socorro mecânico\nProteção contra incêndio\nResponsabilidade civil para danos a terceiros\n ')
                print('1 - Contratar seguro')
                print('2 - voltar para o menu principal\n')
                cegu10=int(input('Escolha uma opção para prosseguir: '))
                if cegu10==1:
                    contratarS()
                if cegu10==2:
                    voltar()
            if sugurus==2:
                print('Porto Intermediate\n')
                print('Preço: R$ 1.500,00 por ano Benefícios:\nCorbertura contra roubo e furto\nAssistência 24 horas para guincho e socorro mecânico\nProteção contra incêndio\nResponsabilidade civil para danos a terceiros\nCobertura contra colisões\nCarro reserva por até 7 dias em caso de acidente\nProteção para danos a acessórios do veículo\n')
                print('1 - Contratar seguro')
                print('2 - voltar para o menu principal\n')
                cegu20=int(input('Escolha uma opção para prosseguir: '))
                if cegu20==1:
                    contratarS()
                if cegu20 == 2:
                    voltar()

            if sugurus==3:
                print('Porto Premium\n')
                print('Preço: R$ 3.000,00 por ano\nBenefícios:\nCorbertura contra roubo e furto\nAssistência 24 horas para guincho e socorro mecânico\nProteção contra incêndio\nResponsabilidade civil para danos a terceiros\nCobertura contra colisões\nCarro reserva por até 7 dias em caso de acidente\nProteção para danos a acessórios do veículo\nValor de indenização integral do veículo 100% da tabela FIPE\nAssistência residencial\nCobertura para danos a vidros e retrovisores\n')
                print('1 - Contratar seguro')
                print('2 - voltar para o menu principal\n')
                cegu30=int(input('Escolha uma opção para prosseguir: '))
                if cegu30==1:
                    contratarS()
                if cegu30 == 2:
                    voltar()
        if seguros == 2:
            voltar()

   #opção IA
    elif opcao_cliente == 4:
        os.system('cls')
        print('Identificar problemas usando IA\n')
        print('Nossos especialistas conjutamnete com os estudantes da faculdade de tecnologia FIAP, desenvolveram uma IA capaz de detectar e fazer um diagnóstico de possiveis irregularidades no seu veículo. Criada com a finalidade de informar nossos assegurados e deixa-los apar de todas as possíveis irregularidades que seu veículo pode apresentar, para que no momento da revisão/manutenção do veículo, o assegurado já saiba os possíveis diagnósticos que irá encontrar. Estamos trabalhando arduamente para melhorar a precisão de seus diagnósticos.\n No momento a IA está em fases de teste mas disponível para uso.\n')
        print('Escolha uma opção para prosseguir\n')
        print('1 - Usar a Ia (Está em fase de teste!)')
        print('2 - Voltar ao menu principal\n')
        
        ia=int(input('Escolha uma opção para prosseguir:'))
        if ia == 1:
           print('Seu carro esta fazendo um barrulho estranho ?')
           print('1 - sim \n2 - não\n')
           aa10=int(input('Escolha uma opção:'))
           if aa10 ==1:
               
               print('1 - O som tem um timbre de contato/atrito?\n2 - O som tem um aspecto mais silencioso como um ruido singelo?\n')
               bb20=int(input('Escolha uma opção para prosseguir:'))
               
               if bb20==1:
                   print('Há diversos diagnósticos possíveis para esse som incômodo e listei uma serie deles para o(a) senhor(a), para que no momento da consulta com um profissional possa axiliá-lo na manutenção do seu veículo e/ou evitar gastos desnecessários')
                   print('Abaixo a lista com os possíveis diagnósticos:')
                   print('• pastilha de freio desgastada\n• Uma alta tensão da correia dentada\n• Problemas nos rolamentos')
                   finalizar()

               if bb20==2:
                   print('Há diversos diagnósticos possíveis para esse som incômodo e listei uma serie deles para o(a) senhor(a), para que no momento da consulta com um profissional possa axiliá-lo na manutenção do seu veículo e/ou evitar gastos desnecessários')
                   print('Abaixo a lista com os possíveis diagnósticos:')
                   print('• Falha nos amortecedor\n• Problemas no ar-condicionado\n• Indício de vazamento')
                   finalizar()

           if aa10==2:
               print('No momento não tenho informação o suficiente no meu banco de dados para poder axiliá-lo com outros problemas veiculares:(')
               print('Para ajudar num melhor desenvolvimento da IA, pedimos a você usuário que deixe seu feedback, para assim aprimorarmos nossas ferramentas.')   
               input('Deixe seu feedback: ')    
               finalizar()
        if ia == 2:
            voltar()

   #opção ouvidoria
    elif opcao_cliente == 5:
        os.system('cls')
        faleConosco()

   #opção sair
    elif opcao_cliente == 6:
        finalizar()

   #opção invalida
    else:
        opcaoInvalida()
def main():
    os.system('cls')
    funcaoUsuario()
    menu()
    opcao_do_cliente()

if __name__ == '__main__':
    main()



