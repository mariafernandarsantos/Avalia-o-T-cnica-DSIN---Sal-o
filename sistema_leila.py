import mysql.connector
from datetime import datetime, timedelta


# INÍCIO DA CONEXAO COM O BANCO DE DADOS
conexao = mysql.connector.connect(
    host='xxxxx',                  # INSIRA SEU HOST
    user='xxxxx',                  # INSIRA SEU USER
    password='xxxxxxx',            # INSIRA SUA SENHA
    database='xxxxxxx',            # INSIRA O NOME DO BANCO DE DADOS
)
cursor = conexao.cursor()

# FUNÇÃO PARA COMEÇAR O AGENDAMENTO
def agendamento():
    funcao_agendamento = int(input('Digite (1) para criar um novo agendamento, digite (2) para alterar um agendamento já feito ou digite (3) para visualizar seu histórico: '))
    if funcao_agendamento != 1 and funcao_agendamento != 2 and funcao_agendamento != 3:
        print('\nOpção inválida, por favor digite (1) para criar um novo agendamento, (2) para alterar um agendamento já feito ou digite (3) para visualizar seu histórico. \nVocê está sendo redirecionado ao início.')
        return
    elif funcao_agendamento == 1:
        novo_agendamento(inserido)

        while True:
            repetir = input('\nDeseja realizar outro agendamento? (S/N): ').upper()
            if repetir not in 'SN':
                print('Resposta inválida, por favor digite (S) para SIM ou (N) para NÃO')

            elif repetir == 'S':
                novo_agendamento(inserido)
            else:
                break

    elif funcao_agendamento == 2:
        altera_agendamento(inserido)
    elif funcao_agendamento == 3:
        historico()


# FUNÇÃO PARA COMEÇAR UM NOVO AGENDAMENTO
def novo_agendamento(inserido):
    servico = escolhe_servico()
    horario = input('Escolha a data e hora do atendimento (formato AAAA-MM-DD HH:MM): ')

    # SELECIONA OS HORARIOS ESCOLHIDOS PELO CLIENTE
    if valida_horario(horario):
        verifica_semana = f'SELECT horarioescolhido FROM agenda WHERE idcadastro = {inserido} AND YEARWEEK(horarioescolhido) = YEARWEEK("{horario}")'
        cursor.execute(verifica_semana)
        agendamentos_semana = cursor.fetchall()

        # NOTIFICA SOBRE MAIS DE UM AGENDAMENTO NA SEMANA
        if agendamentos_semana:
            reagenda = input('Aparentemente você já fez agendamentos para essa semana, gostaria de encaixar todos no mesmo dia?'
                             '\nDigite "S" para Sim e "N" para Não: ').upper()

            if reagenda not in 'SN':
                print('Entrada inválida, digite S para Sim e N para não')
                return novo_agendamento(inserido)

            elif reagenda == 'S':
                comando_mostra = f'SELECT horario FROM servicos, agenda WHERE idcadastro = {inserido} AND YEARWEEK(horarioescolhido) = YEARWEEK("{horario}")'
                cursor.execute(comando_mostra)
                resultado = cursor.fetchall()
                foreign_key_off = 'SET foreign_key_checks = 0'          # DESLIGA A CHECAGEM DA FOREIGN KEY PARA QUE SEU VALOR SEJA ALTERADO
                cursor.execute(foreign_key_off)
                conexao.commit()

                # VERIFICA O MELHOR HORÁRIO PARA O AGENDAMENTO DO CLIENTE (PRIMEIRO HORÁRIO DESPONÍVEL)
                melhor_data = min(resultado, key=lambda x: x[0])

                # ATUALIZA O AGENDAMENTO
                update_data = f'UPDATE servicos, agenda SET servicos.horario = %s WHERE agenda.idcadastro = %s AND servicos.horario = agenda.horarioescolhido AND YEARWEEK(agenda.horarioescolhido) = YEARWEEK("{horario}")'
                cursor.execute(update_data, (melhor_data[0], inserido))
                conexao.commit()
                foreign_key_on = 'SET foreign_key_checks = 1'          # LIGA NOVAMENTE A CHECAGEM DA FOREIGN KEY
                cursor.execute(foreign_key_on)
                conexao.commit()
                print('Reagendamento realizado com sucesso!')
    add_horario(horario, servico, inserido,novo)


#FUNÇÃO PARA CRIAR CADASTRO
def cadastro():
    nome = input('Por favor, digite seu nome completo: ')
    cursor.execute(f'SELECT LAST_INSERT_ID()')      #SELECIONA O ULTIMO ID INSERIDO
    inserido = cursor.fetchone()[0]
    add_nome(nome,inserido)   #CHAMA A FUNÇÃO add_nome PARA ADICIONAR O NOME
    print(f'Obrigada {nome}! Seu número de cadastro é {inserido}')


# FUNÇÃO PARA ADICONAR O NOME
def add_nome(nome):
        cursor.execute('INSERT INTO clientes (nome) VALUES (%s)', (nome,))
        conexao.commit()
        return cursor.lastrowid


# FUNÇÃO PARA MOSTRAR O HISTÓRICO DE AGENDAMENTOS
def historico():
    # SELECIONA OS AGENDAMENTOS EXISTENTES DESSE CLIENTE
    comando = f'SELECT agenda.idagendamento, servico, horarioescolhido FROM servicos, agenda WHERE idcadastro = {inserido} AND servicos.horario = agenda.horarioescolhido'
    cursor.execute(comando)
    resultados = cursor.fetchall()

    if not resultados:
        print('Nenhum agendamento encontrado para este cliente.')
        return

    # MOSTRA OS AGENDAMENTOS EXISTENTES
    print('Agendamentos existentes:')
    for idagendamento, servico, horario in resultados:
        print(f'ID: {idagendamento}, Serviço: {servico}, Horário: {horario}')


# FUNÇÃO PARA ESCOLHER O SERVIÇO
def escolhe_servico():
    # MOSTRA A LISTA DE SERVIÇOS
    print('Lista de serviços disponíveis:')
    for codigo, servico in lista_servico:
        print(f'({codigo}) {servico}')

    servico = int(input('\nDigite o código do serviço escolhido: '))

    # PROCURA O SERVIÇO CORRESPONDENTE AO CODIGO INSERIDO
    if servico not in [codigo for codigo, _ in lista_servico]:
        print('Código inválido! Tente novamente com um número de 1 a 7.')
        return escolhe_servico()

    return servico


# FUNÇÃO PARA VALIDAR O HORARIO ESCOLHIDO
def valida_horario(hora):
    try:
        formato = '%Y-%m-%d %H:%M'
        horario_dt = datetime.strptime(hora, formato)

        # VERIFICA SE O HORÁRIO ESTÁ NO FUTURO
        if horario_dt <= datetime.now():
            print('Por favor insira um horário no futuro! Ainda não temos uma máquina do tempo para ir ao passado...')
            return False

        return True
    except ValueError:
        print('Formato de data inválido. Por favor siga o formato AAAA-MM-DD HH:MM.')
        return False


# FUNÇÃO PARA ADICIONAR O HORARIO
def add_horario(hora, servico, inserido, novo):
    if valida_horario(hora):
        servico_escolhido = next((s for c, s in lista_servico if c == servico), None)
        if servico_escolhido:
            novo += 1
            foreign_key_off = 'SET foreign_key_checks = 0'      # DESLIGA A CHECAGEM DA FOREIGN KEY PARA QUE SEU VALOR SEJA ALTERADO
            cursor.execute(foreign_key_off)
            conexao.commit()

            comando = 'INSERT INTO servicos (horario, servico) VALUES (%s, %s)'   #I NSERE OS DADOS NA COLUNA 'SERVICOS' NO BANCO DE DADOS
            cursor.execute(comando, (hora, servico_escolhido))
            conexao.commit()

            comando_agenda = 'INSERT INTO agenda (horarioescolhido, idcadastro, idservico) VALUES (%s, %s, %s)'    # INSERE OS DADOS NA COLUNA 'AGENDA' NO BANCO DE DADOS
            cursor.execute(comando_agenda, (hora, inserido, novo))
            conexao.commit()

            foreign_key_on = 'SET foreign_key_checks = 1'        # LIGA NOVAMENTE A CHECAGEM DA FOREIGN KEY
            cursor.execute(foreign_key_on)
            conexao.commit()

            print('Agendamento realizado com sucesso!')

        else:
            print('Erro ao obter nome do serviço.')
    else:
        print('Formato de data inválido. Siga o formato AAAA-MM-DD HH:MM')


# FUNÇÃO PARA VALIDAR SE É POSSÍVEL ALTERAR O AGENDAMENTO
def pode_alterar(horario_agendamento):
    # OBTÉM A DATA DE HOJE
    agora = datetime.now()

    # CALCULA A DIFERENÇA DE TEMPO ENTRE O AGENDAMENTO E A DATA ATUAL
    diferenca = horario_agendamento - agora

    # VERIFICA SE A DIFERENÇA É MENOR QUE DE 2 DIAS
    if diferenca.total_seconds() < 172.800:
        return False
    else:
        return True


# FUNÇÃO PARA ALTERAR AGENDAMENTO
def altera_agendamento(inserido):
    # MOSTRA OS AGENDAMENTOS DO CLIENTE
    comando = f'SELECT agenda.idagendamento, servico, horarioescolhido FROM servicos, agenda WHERE idcadastro = {inserido} AND servicos.horario = agenda.horarioescolhido'
    cursor.execute(comando)
    resultados = cursor.fetchall()

    if not resultados:
        print('Nenhum agendamento encontrado para este cliente.')
        return

    print('Agendamentos existentes:')
    for idagendamento, servico, horario in resultados:
        print(f'ID: {idagendamento}, Serviço: {servico}, Horário: {horario}')

    # SOLICITA O ID DO AGENDAMENTO QUE O CLIENTE DESEJA ALTERAR
    id_agendamento_alterar = input('Digite o ID do agendamento que deseja alterar: ')
    if not id_agendamento_alterar.isdigit():
        print('ID inválido. Tente novamente.')
        return

    id_agendamento_alterar = int(id_agendamento_alterar)

    # OBTÉM O horario_agendamento DO AGENDAMENTO ESPECÍFICO
    horario_agendamento = next((horario for id_agendamento, _, horario in resultados if id_agendamento == id_agendamento_alterar), None)

    if not horario_agendamento:
        print('ID de agendamento não encontrado. Tente novamente.')
        return

    # VERIFICA SE É POSSÍVEL ALTERAR
    if not pode_alterar(horario_agendamento):
        print('Não é possível alterar o agendamento.\n A alteração só é permitida até 2 dias antes do agendamento.'
              'Por favor entre em contato com Leila pelo telefone.')
        return

        # ESCOLHE O QUE ALTERAR
    quer_alterar = input('Deseja alterar o horário ou o serviço? (Digite 1 para horário ou 2 para serviço: ')

    if quer_alterar != '1' and quer_alterar != '2':
        print('Resposta inválida, por favor insira 1 para horário e 2 para serviço')
        return
    else:
        # ALTERA O HORÁRIO
        if quer_alterar == '1':
            novo_horario = input('Digite a nova data e hora do agendamento (formato AAAA-MM-DD HH:MM): ')

            # VALIDA O NOVO HORÁRIO
            if not valida_horario(novo_horario):
                print('Formato de data inválido. Siga o formato AAAA-MM-DD HH:MM')
                return

            # ATUALIZA O HORÁRIO NA TABELA SERVICOS
            foreign_key_off = 'SET foreign_key_checks = 0'
            cursor.execute(foreign_key_off)
            conexao.commit()
            update_agenda_hora = 'UPDATE servicos SET horario = %s WHERE horario = %s'
            cursor.execute(update_agenda_hora, (novo_horario, horario))
            conexao.commit()

            # ATUALIZA O HORÁRIO NA TABELA AGENDA
            update_servicos_hora = 'UPDATE agenda SET horarioescolhido = %s WHERE idagendamento = %s'
            cursor.execute(update_servicos_hora, (novo_horario, id_agendamento_alterar))
            conexao.commit()
            foreign_key_on = 'SET foreign_key_checks = 1 '
            cursor.execute(foreign_key_on)
            conexao.commit()

        # ALTERA O SERVIÇO
        else:
            print('Lista de serviços disponíveis:')
            for codigo, servico in lista_servico:
                print(f'({codigo}) {servico}')

            # ESCOLHA DO NOVO SERVIÇO
            novo_servico = int(input('\nDigite o código do novo serviço escolhido: '))
            novo_servico_escolhido = next((s for c, s in lista_servico if c == novo_servico), None)

            if novo_servico not in [codigo for codigo, _ in lista_servico]:
                print('Código inválido! Tente novamente com um número de 1 a 7.')
                return
            # ATUALIZA TABELA SERVICO
            update_servicos = 'UPDATE servicos SET servico = %s WHERE horario = %s'
            cursor.execute(update_servicos, (novo_servico_escolhido, horario))
            conexao.commit()
    print('Agendamento alterado com sucesso!')

def altera_leila():
    comando = f'SELECT agenda.idagendamento, servico, horarioescolhido FROM servicos, agenda'
    cursor.execute(comando)
    resultados = cursor.fetchall()

    print('Agendamentos existentes:')
    for idagendamento, servico, horario in resultados:
        print(f'ID: {idagendamento}, Serviço: {servico}, Horário: {horario}')

    # SOLICITA O ID DO AGENDAMENTO QUE LEILA DESEJA ALTERAR
    id_agendamento_alterar = input('Digite o ID do agendamento que deseja alterar: ')
    if not id_agendamento_alterar.isdigit():
        print('ID inválido. Tente novamente.')
    else:
        # ESCOLHE O QUE ALTERAR
        quer_alterar = input('Deseja alterar o horário ou o serviço? (Digite 1 para horário ou 2 para serviço): ')

        if quer_alterar != '1' and quer_alterar != '2':
            print('Resposta inválida, por favor insira 1 para horário e 2 para serviço')
        else:
            # ALTERA O HORÁRIO
            if quer_alterar == '1':
                novo_horario = input('Digite a nova data e hora do agendamento (formato AAAA-MM-DD HH:MM): ')

                # VALIDA O NOVO HORÁRIO
                if not valida_horario(novo_horario):
                    print('Formato de data inválido. Siga o formato AAAA-MM-DD HH:MM')
                else:
                    # ATUALIZA O HORÁRIO NA TABELA SERVICOS
                    foreign_key_off = 'SET foreign_key_checks = 0'
                    cursor.execute(foreign_key_off)
                    conexao.commit()
                    update_agenda_hora = 'UPDATE servicos SET horario = %s WHERE horario = %s'
                    cursor.execute(update_agenda_hora, (novo_horario, horario))
                    conexao.commit()

                    # ATUALIZA O HORÁRIO NA TABELA AGENDA
                    update_servicos_hora = 'UPDATE agenda SET horarioescolhido = %s WHERE idagendamento = %s'
                    cursor.execute(update_servicos_hora, (novo_horario, id_agendamento_alterar))
                    conexao.commit()
                    foreign_key_on = 'SET foreign_key_checks = 1 '
                    cursor.execute(foreign_key_on)
                    conexao.commit()

                    print('Agendamento alterado com sucesso!')

            # ALTERA O SERVIÇO
            elif quer_alterar == '2':
                print('Lista de serviços disponíveis:')
                for codigo, servico in lista_servico:
                    print(f'({codigo}) {servico}')

                # ESCOLHA DO NOVO SERVIÇO
                novo_servico = int(input('\nDigite o código do novo serviço escolhido: '))
                novo_servico_escolhido = next((s for c, s in lista_servico if c == novo_servico), None)

                if novo_servico not in [codigo for codigo, _ in lista_servico]:
                    print('Código inválido! Tente novamente com um número de 1 a 7.')
                else:
                    # ATUALIZA TABELA SERVICO
                    update_servicos = 'UPDATE servicos SET servico = %s WHERE horario = %s'
                    cursor.execute(update_servicos, (novo_servico_escolhido, horario))
                    conexao.commit()

                    print('Agendamento alterado com sucesso!')

    id_agendamento_alterar = int(id_agendamento_alterar)

    # OBTÉM O HORÁRIO DO AGENDAMENTO ESPECÍFICO
    horario_agendado = next((horario for id_agendamento, _, horario in resultados if id_agendamento == id_agendamento_alterar), None)

    if not horario_agendado:
        print('ID de agendamento não encontrado. Tente novamente.')
        return


# LISTA DE SERVIÇOS
lista_servico = [
    (1, 'Cortar cabelo'),
    (2, 'Pintar cabelo'),
    (3, 'Escovar cabelo'),
    (4, 'Penteado'),
    (5, 'Hidratar cabelo'),
    (6, 'Fazer sobrancelhas'),
    (7, 'Rena Sobrancelhas')
]
inserido = None  # NÍCIO DA VÁRIAVEL INSERIDO (id do cadastro do cliente)
novo = 0  # VARIÁVEL QUE IRÁ AUMENTAR +1 A CADA NOVO SERVIÇO CADASTRADO


#INÍCIO DO SISTEMA
while True:
    funcao_inicio = int(input('Bem vindo ao sistema da Cabeleleila Leila! Digite (1) se você já possui cadastro, ou digite (2) se você deseja se cadastrar: '))
    if funcao_inicio != 1 and funcao_inicio != 2:
        print('Opção inválida, por favor digite (1) caso o cadastro já exista, ou (2) se você deseja se cadastrar. \nVocê está sendo redirecionado ao início.')

    # CLIENTE JÁ POSSUI CADASTRO
    elif funcao_inicio == 1:
        while True:
            try:
                insere_cadastro = int(input('Bem-vindo de volta! Por favor, insira o número do seu cadastro: '))
                # LEILA QUER ALTERAR AGENDAMENTO
                if insere_cadastro == 0:
                    print('Bem vinda Leila! Veja e altere seus agendamentos!')
                    altera_leila()

                elif not insere_cadastro:
                    print('Número de cadastro inválido. Verifique se seu número está correto.')
                    continue
            except ValueError:
                print('Entrada inválida. Insira um número inteiro para o cadastro.')
                continue

            # CONFERE O NÚMERO DE CADASTRO DO CLIENTE
            comando = 'SELECT cadastro FROM clientes WHERE cadastro = %s'
            cursor.execute(comando, (insere_cadastro,))
            inserido_tupla = cursor.fetchone()

            if inserido_tupla:
                inserido = inserido_tupla[0]
                print(f'Cadastro inserido = {inserido}')
                agendamento()
                break
            else:
                print('Número de cadastro não encontrado. Tente novamente.')

    # CLIENTE NÃO POSSUI CADASTRO
    elif funcao_inicio == 2:
        nome = input('Por favor, digite seu nome completo: ')
        inserido = add_nome(nome)
        print(f'Obrigado(a), {nome}! Seu número de cadastro é {inserido}')
        agendamento()
        break
    break

print('Obrigada por usar os serviços da Cabeleleila Leila!! Volte sempre :)')
cursor.close()
conexao.close()
