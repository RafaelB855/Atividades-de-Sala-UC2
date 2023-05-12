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
    "Derrotas" int NOT NULL,
    "Empates" int NOT NULL,
    "GolsFeitos" int NOT NULL,
    "GolsTomados" int NOT NULL,
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
#########################################################################
#----------------------------------------------------------------------------------------------------------------------#

def verListaDePartidas():

    listaLivros = conexaoBanco.consultarBanco('''
    SELECT * FROM "Livros"
    ORDER BY "ID" ASC
    ''')

    if listaLivros:
        print("ID | NOME | Autor")
        for livro in listaLivros:
            print(f"{livro[0]} | {livro[1]} | {livro[2]}")

    else:
        print("Ocorreu um erro na consulta, ou a lista é vazia.")

#----------------------------------------------------------------------------------------------------------------------#

def verListaDeTabela():

    listaAlugueis = conexaoBanco.consultarBanco('''
    SELECT * FROM "Alugueis"
    ORDER BY "ID" ASC
    ''')

    if listaAlugueis:
        print("ID | CLIENTE | LIVRO | DATA DA RETIRADA")
        for Aluguel in listaAlugueis:

            clientedoaluguel = conexaoBanco.consultarBanco(f'''
                SELECT * FROM "Clientes"
                WHERE "ID" = '{Aluguel[1]}'
                ''')[0]
            
            livrodoaluguel = conexaoBanco.consultarBanco(f'''
                SELECT * FROM "Livros"
                WHERE "ID" = '{Aluguel[2]}'
                ''')[0]


            print(f"{Aluguel[0]} | {clientedoaluguel[1]} | {livrodoaluguel[1]} | {Aluguel[3]}")

    else:
        print("Ocorreu um erro na consulta, ou a lista é vazia.")

#----------------------------------------------------------------------------------------------------------------------#

while True:

    print('''
    Bem vindo ao Campeonato
    1. Ver Times
    2. Ver Tabelas
    3. Ver Tabelas
    0. Sair
    ''')

    op = input("Escolha o menu que deseja acessar:")

    match op:
        case "1":
            verListaDeTimes()
        case "2":
            cadastrarNovoTime()
        case "3":
            verListaDePartidas()
        case "4":
            verListaDeTabela()
        case "0":
            print("Saindo da programa...")
            break
        case _:
            print("Escolha uma opção válida.")