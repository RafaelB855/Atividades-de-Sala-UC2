from conexao import Conexao

def criarTabela(con):
    listaSql=['''
    CREATE TABLE "Times"(
    "ID" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "Nome" varchar(255) NOT NULL
    )
    ''',
    
    '''
    CREATE TABLE "Partidas"(
    "ID" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "Time1" int NOT NULL,
    "Gols1" int NOT NULL,
    "Gols2" int NOT NULL,
    "Time2" int NOT NULL,
    CONSTRAINT fk_Time1
        FOREIGN KEY("Time1")
        REFERENCES "Times"("ID"),
    CONSTRAINT fk_Time2
        FOREIGN KEY("Time2")
        REFERENCES "Times"("ID")
    )
    '''

    '''
    CREATE TABLE "Tabela"(
    "ID" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "ID_Time" int NOT NULL,
    "Pontos" int NOT NULL,
    "Vitorias" int NOT NULL,
    "Empates" int NOT NULL,
    "Derrotas" int NOT NULL,
    "GolsPró" int NOT NULL,
    "GolsContra" int NOT NULL,
    "SaldodeGols" int NOT NULL,
    CONSTRAINT fk_Time
        FOREIGN KEY("ID_Time")
        REFERENCES "Times"("ID")
    )
    ''']

    for sql in listaSql:
        if con.manipularBanco(sql):
            print("Tabela criada.")
        else:
            print("Falha ao criar.")


conexaoBanco = Conexao("Campeonato","localhost","5432","postgres","postgres")
#criarTabela(conexaoBanco) 
#----------------------------------------------------------------------------------------------------------------------#
def verMenuClientes():

    while True:
        print('''
        Opções menu Times:
        1. Ver Times
        2. Criar Time
        3. Atualizar Time
        4. Remover Time
        0. Voltar ao menu principal
        ''')
        op = input("Escolha uma das opções:")
        match op:
            case "1":
                verListaDeTimes()
            case "2":
                cadastrarNovoTime()
            case "3":
                atualizarTime()
            case "4":
                removerTime()
            case "0":
                print("Voltando ao menu principal...")
                break
            case _:
                print("Escolha uma opção válida.")

        input("Digite Enter para continuar...")

def verListaDeTimes():

    listaTimes = conexaoBanco.consultarBanco('''
    SELECT * FROM "Times"
    ORDER BY "ID" ASC
    ''')

    if listaTimes:
        print("ID | NOME")
        for Time in listaTimes:
            print(f"{Time[0]} | {Time[1]}")

    else:
        print("Ocorreu um erro na consulta, ou a lista é vazia.")

def cadastrarNovoTime():
    print("Cadastro de Time - Insira as informações pedidas")

    nome = input("Digite o nome do Time:")

    sqlInserir = f'''
    INSERT INTO "Times"
    Values(default, '{nome}')
    '''


    if conexaoBanco.manipularBanco(sqlInserir):

        print(f"O time {nome} foi inserido com sucesso.")
    else:
        print("Falha ao inserir o time!")

def atualizarTime():
    print("Tela de atualização de time:")
    print("Lista de Times")
    
    verListaDeTimes()
    TimeEscolhido = input("Digite o id do time escolhido:")
    verTimeEspecifico(TimeEscolhido)
    novoNome = input("Digite o novo nome (vazio para não alterar):")

    if novoNome:
        conexaoBanco.ManipularBanco(f'''
        UPDATE "Times"
        SET "Nome" = '{novoNome}'
        WHERE "ID" = {TimeEscolhido}
        ''')

    print("Tentativa de alteração executada.")

def verTimeEspecifico(idTime):
    Time = conexaoBanco.ConsultarBanco(f'''SELECT * FROM "Times"
    WHERE "ID" = {idTime}
    ''')[0]

    if Time:
        Time = Time[0]
        print("Time Escolhido: ")
        print(f'''
        ID - {Time[0]}
        Nome - {Time[1]}
        ''')

        listaPartidas = conexaoBanco.ConsultarBanco(f'''
        SELECT * FROM "Partidas"
        WHERE "Time1" = '{Time[0]}' and "Time2" = '{Time[0]}'
        ''')

        if listaPartidas:
            print(" TIME | PLACAR | TIME ")
            for Partida in listaPartidas:
                
                Time1daPartida = conexaoBanco.consultarBanco(f'''
                    SELECT * FROM "Times"
                    WHERE "ID" = '{Partida[1]}'
                    ''')[0]
                
                Time2daPartida = conexaoBanco.consultarBanco(f'''
                    SELECT * FROM "Times"
                    WHERE "ID" = '{Partida[4]}'
                    ''')[0]
                
                print(f"{Time1daPartida[1]} | {Partida[2]} / {Partida[3]} | {Time2daPartida[1]} ")

        else:
            print("O time não possui partidas")

    else:
        print("O time não foi encontrado!")

    if Time:
        Time = Time[0]
        print("Time Escolhido: ")
        print(f'''
        ID - {Time[0]}
        Nome - {Time[1]}
        ''')

        listaTabelas = conexaoBanco.ConsultarBanco(f'''
        SELECT * FROM "Tabela"
        WHERE "ID_Time" = '{Time[0]}'
        ''')

        if listaTabelas:
            print("RANK | TIME | P | V | E | D | GP | GC | SG")
            for Tabela in listaTabelas:
                
                TimedaTabela = conexaoBanco.consultarBanco(f'''
                    SELECT * FROM "Times"
                    WHERE "ID" = '{Tabela[1]}'
                    ''')[0]

                print(f"{Tabela[0]} | {TimedaTabela[1]} | {Tabela[2]} | {Tabela[3]} | {Tabela[4]} | {Tabela[5]} | {Tabela[6]} | {Tabela[7]} | {Tabela[8]}")


        else:
            print("O time não possui cadastrados na tabela")

    else:
        print("O time não foi encontrado!")

def removerTime():
    print("Tela de remoção de time:")
    print("Lista de Times")
    
    verListaDeTimes()
    timeEscolhido = input("Digite o id do time escolhido:")
    verTimeEspecifico(timeEscolhido)
    confirmar = input("Deseja remover este time? (S/N)").upper()

    match confirmar:
        case "S":
           resultadoRemocao = conexaoBanco.ManipularBanco(f'''
           DELETE FROM "Times"
           WHERE "ID" = '{timeEscolhido}'
           ''')
           
           if resultadoRemocao:
               print("Time removido com sucesso.")
           else:
               print("Time não existe ou não foi removido.")
        case "N":
            print("Ok voltando ao menu principal")
        case _:
            print("Você digitou um comando inválido. Voltando ao menu.")

#----------------------------------------------------------------------------------------------------------------------#

def verListaDePartidas():

    listaPartidas = conexaoBanco.consultarBanco('''
    SELECT * FROM "Partidas"
    ORDER BY "ID" ASC
    ''')

    if listaPartidas:
        print(" TIME | PLACAR | TIME ")
        for Partida in listaPartidas:
            
            Time1daPartida = conexaoBanco.consultarBanco(f'''
                SELECT * FROM "Times"
                WHERE "ID" = '{Partida[1]}'
                ''')[0]
            
            Time2daPartida = conexaoBanco.consultarBanco(f'''
                SELECT * FROM "Times"
                WHERE "ID" = '{Partida[4]}'
                ''')[0]
            
            print(f"{Time1daPartida[1]} | {Partida[2]} / {Partida[3]} | {Time2daPartida[1]} ")

    else:
        print("Ocorreu um erro na consulta, ou a lista é vazia.")

#----------------------------------------------------------------------------------------------------------------------#

def verListaDeTabela():

    listaTabelas = conexaoBanco.consultarBanco('''
    SELECT * FROM "Tabela"
    ORDER BY "Pontos" ASC
    ''')

    if listaTabelas:
        print("RANK | TIME | P | V | E | D | GP | GC | SG")
        for Tabela in listaTabelas:
            
            TimedaTabela = conexaoBanco.consultarBanco(f'''
                SELECT * FROM "Times"
                WHERE "ID" = '{Tabela[1]}'
                ''')[0]

            print(f"{Tabela[0]} | {TimedaTabela[1]} | {Tabela[2]} | {Tabela[3]} | {Tabela[4]} | {Tabela[5]} | {Tabela[6]} | {Tabela[7]} | {Tabela[8]}")

    else:
        print("Ocorreu um erro na consulta, ou a lista é vazia.")

#----------------------------------------------------------------------------------------------------------------------#

while True:

    print('''
    Bem vindo ao Campeonato
    1. Menu de Times
    2. Ver Partidas
    3. Ver Tabelas
    0. Sair
    ''')

    op = input("Escolha o menu que deseja acessar:")

    match op:
        case "1":
            verMenuClientes()
        case "2":
            verListaDePartidas()
        case "3":
            verListaDeTabela()
        case "0":
            print("Saindo da programa...")
            break
        case _:
            print("Escolha uma opção válida.")