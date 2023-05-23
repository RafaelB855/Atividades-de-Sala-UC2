from conexao import Conexao

def criarTabela(con):
    listaSql=['''
    CREATE TABLE "Clientes"(
    "ID" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "Nome" varchar(255) NOT NULL,
    "CPF" char(11) NOT NULL UNIQUE
    )
    ''',
    
    '''
    CREATE TABLE "Livros"(
    "ID" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "Nome" varchar(255) NOT NULL,
    "Autor" varchar(255) NOT NULL
    )
    ''',

    '''
    CREATE TABLE "Alugueis"(
    "ID" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "ID_Cliente" int NOT NULL,
    "ID_Livro" int NOT NULL,
    "Data do Aluguel" timestamp default CURRENT_TIMESTAMP(2),
    CONSTRAINT fk_cliente
        FOREIGN KEY("ID_Cliente")
        REFERENCES "Clientes"("ID"),
    CONSTRAINT fk_livro
        FOREIGN KEY("ID_Livro")
        REFERENCES "Livros"("ID")
    )
    ''']

    for sql in listaSql:
        if con.manipularBanco(sql):
            print("Tabela criada.")
        else:
            print("Falha ao criar.")

conexaoBanco = Conexao("Biblioteca","localhost","5432","postgres","postgres")

def verMenuClientes():

    while True:
        print('''
        Opções menu cliente:
        1. Ver lista de Clientes
        2. Cadastrar Novo Cliente
        3. Atualizar Cliente
        4. Remover Cliente
        0. Voltar ao menu principal
        ''')
        op = input("Escolha uma das opções:")
        match op:
            case "1":
                verListaDeClientes()
            case "2":
                cadastrarNovoCliente()
            case "3":
                atualizarCliente()
            case "4":
                removerCliente()
            case "0":
                print("Voltando ao menu principal...")
                break
            case _:
                print("Escolha uma opção válida.")

        input("Digite Enter para continuar...")

def verListaDeClientes():

    listaClientes = conexaoBanco.consultarBanco('''
    SELECT * FROM "Clientes"
    ORDER BY "ID" ASC
    ''')

    if listaClientes:
        print("ID | NOME | CPF")
        for cliente in listaClientes:
            print(f"{cliente[0]} | {cliente[1]} | {cliente[2]}")

    else:
        print("Ocorreu um erro na consulta, ou a lista é vazia.")

def cadastrarNovoCliente():
    print("Cadastro de Cliente - Insira as informações pedidas")

    nome = input("Digite o nome do Cliente:")
    cpfValido = False

    while cpfValido == False:
        cpf = input("Digite o cpf do Cliente (somente os números):")

        try:
            if len(cpf) == 11 and cpf.isnumeric():
                cpfValido = True
            else:
                print("CPF Inválido, digite novamente. O CPF deve conter 11 digitos e ser somente números.")
                cpfValido = False

        except:

            print("Ocorreu um erro, digite novamente")
            cpfValido = False

    sqlInserir = f'''
    INSERT INTO "Clientes"
    Values(default, '{nome}', '{cpf}')
    '''


    if conexaoBanco.manipularBanco(sqlInserir):

        print(f"O Cliente {nome} foi inserido com sucesso.")
    else:
        print("Falha ao inserir o cliente!")

def atualizarCliente():
    print("Tela de atualização de cliente:")
    print("Lista de Clientes")
    
    verListaDeClientes()
    clienteEscolhido = input("Digite o id do cliente escolhido:")
    verClienteEspecifico(clienteEscolhido)
    novoNome = input("Digite o novo nome (vazio para não alterar):")
    novoCPF = input("Digite o novo cpf (vazio para não alterar):")

    if novoNome:
        conexaoBanco.manipularBanco(f'''
        UPDATE "Clientes"
        SET "Nome" = '{novoNome}'
        WHERE "ID" = {clienteEscolhido}
        ''')

    if novoCPF:
        conexaoBanco.manipularBanco(f'''
        UPDATE "Clientes"
        SET "CPF" = '{novoCPF}'
        WHERE "ID" = {clienteEscolhido}
        ''')

    print("Tentativa de alteração executada.")

def verClienteEspecifico(idCliente):
    cliente = conexaoBanco.consultarBanco(f'''SELECT * FROM "Clientes"
    WHERE "ID" = {idCliente}
    ''')[0]

    if cliente:
        cliente = cliente[0]
        print("Cliente Escolhido: ")
        print(f'''
        ID - {cliente[0]}
        Nome - {cliente[1]}
        CPF - {cliente[2]}
        ''')

        listaAlugueis = conexaoBanco.consultarBanco(f'''
        SELECT * FROM "Alugueis"
        WHERE "ID_Cliente" = '{cliente[0]}'
        ''')

        if listaAlugueis:
            print("Lista de alugueis: ")
            print("ID | Cliente | Livro | Data de Aluguel")
            for aluguel in listaAlugueis:
                
                clienteDoAluguel = conexaoBanco.consultarBanco(f'''
                SELECT * FROM "Clientes"
                WHERE "ID" = {aluguel[1]}
                ''')[0]

                livroDoAluguel = conexaoBanco.consultarBanco(f'''
                SELECT * FROM "Livros"
                WHERE "ID" = {aluguel[2]}
                ''')[0]

                print(f"{aluguel[0]} | {clienteDoAluguel[1]} | {livroDoAluguel[1]} | {aluguel[3]}")

        else:
            print("O cliente não possui aluguéis cadastrados")

    else:
        print("O cliente não foi encontrado!")

def removerCliente():
    print("Tela de remoção de cliente:")
    print("Lista de Clientes")
    
    verListaDeClientes()
    clienteEscolhido = input("Digite o id do cliente escolhido:")
    verClienteEspecifico(clienteEscolhido)
    confirmar = input("Deseja remover este cliente? (S/N)").upper()

    match confirmar:
        case "S":
           resultadoRemocao = conexaoBanco.manipularBanco(f'''
           DELETE FROM "Clientes"
           WHERE "ID" = '{clienteEscolhido}'
           ''')
           
           if resultadoRemocao:
               print("Cliente removido com sucesso.")
           else:
               print("Cliente não existe ou não foi removido.")
        case "N":
            print("Ok voltando ao menu principal")
        case _:
            print("Você digitou um comando inválido. Voltando ao menu.")

#----------------------------------------------------------------------------------------------------------------------#

def verMenuLivros():

    while True:
        print('''
        Opções menu livros:
        1. Ver lista de Livros
        2. Cadastrar Novo Livro
        3. Atualizar Livro
        4. Remover Livro
        0. Voltar ao menu principal
        ''')
        op = input("Escolha uma das opções:")
        match op:
            case "1":
                verListaDeLivros()
            case "2":
                cadastrarNovoLivro()
            case "3":
                atualizarLivro()
            case "4":
                removerLivro()
            case "0":
                print("Voltando ao menu principal...")
                break
            case _:
                print("Escolha uma opção válida.")

        input("Digite Enter para continuar...")

def verListaDeLivros():

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

def cadastrarNovoLivro():

    print("Cadastro de Livro - Insira as informações pedidas")

    nome = input("Digite o nome do Livro:")
    autor = input("Digite o nome do Autor:")

    sqlInserir = f'''
    INSERT INTO "Livros"
    Values(default, '{nome}', '{autor}')
    '''

    if conexaoBanco.manipularBanco(sqlInserir):

        print(f"O Livro {nome} foi inserido com sucesso.")
    else:
        print("Falha ao inserir o livro!")

def atualizarLivro():
    print("Tela de atualização de Livro:")
    print("Lista de Livros")
    
    verListaDeLivros()
    LivroEscolhido = input("Digite o id do Livro escolhido:")
    verLivroEspecifico(LivroEscolhido)
    novoNome = input("Digite o novo Nome (vazio para não alterar):")
    novoAutor = input("Digite o novo Autor (vazio para não alterar):")

    if novoNome:
        conexaoBanco.manipularBanco(f'''
        UPDATE "Livros"
        SET "Nome" = '{novoNome}'
        WHERE "ID" = {LivroEscolhido}
        ''')

    if novoAutor:
        conexaoBanco.manipularBanco(f'''
        UPDATE "Livros"
        SET "Autor" = '{novoAutor}'
        WHERE "ID" = {LivroEscolhido}
        ''')

    print("Tentativa de alteração executada.")

def verLivroEspecifico(idLivro):
    Livro = conexaoBanco.consultarBanco(f'''SELECT * FROM "Livros"
    WHERE "ID" = {idLivro}
    ''')

    if Livro:
        Livro = Livro[0]
        print("Livro Escolhido: ")
        print(f'''
        ID - {Livro[0]}
        Nome - {Livro[1]}
        Autor - {Livro[2]}
        ''')

        listaAlugueis = conexaoBanco.consultarBanco(f'''
        SELECT * FROM "Alugueis"
        WHERE "ID_Livro" = '{Livro[0]}'
        ''')

        if listaAlugueis:
            print("Lista de alugueis: ")
            print("ID | Cliente | Livro | Data de Aluguel")
            for aluguel in listaAlugueis:
                
                ClienteDoAluguel = conexaoBanco.consultarBanco(f'''
                SELECT * FROM "Cliente"
                WHERE "ID" = {aluguel[1]}
                ''')[0]

                livroDoAluguel = conexaoBanco.consultarBanco(f'''
                SELECT * FROM "Livros"
                WHERE "ID" = {aluguel[2]}
                ''')[0]

                print(f"{aluguel[0]} | {ClienteDoAluguel[1]} | {livroDoAluguel[1]} | {aluguel[3]}")

        else:
            print("O Livro não possui aluguéis cadastrados")

    else:
        print("O Livro não foi encontrado!")

def removerLivro():
    print("Tela de remoção de Livro:")
    print("Lista de Livros")
    
    verListaDeLivros()
    LivroEscolhido = input("Digite o id do Livro escolhido:")
    verLivroEspecifico(LivroEscolhido)
    confirmar = input("Deseja remover este Livro? (S/N)").upper()

    match confirmar:
        case "S":
           resultadoRemocao = conexaoBanco.manipularBanco(f'''
           DELETE FROM "Livros"
           WHERE "ID" = '{LivroEscolhido}'
           ''')
           
           if resultadoRemocao:
               print("Livro removido com sucesso.")
           else:
               print("Livro não existe ou não foi removido.")
        case "N":
            print("Ok voltando ao menu principal")
        case _:
            print("Você digitou um comando inválido. Voltando ao menu.")

#----------------------------------------------------------------------------------------------------------------------#

def verMenuAlugueis():

    while True:
        print('''
        Opções menu Alugueis:
        1. Ver lista de Alugueis
        2. Cadastrar Novo Aluguel
        3. Atualizar Aluguel
        4. Remover Aluguel
        0. Voltar ao menu principal
        ''')
        op = input("Escolha uma das opções:")
        match op:
            case "1":
                verListaDeAlugueis()
            case "2":
                cadastrarNovoAluguel()
            case "3":
                atualizarAluguel()
            case "4":
                removerAluguel()
            case "0":
                print("Voltando ao menu principal...")
                break
            case _:
                print("Escolha uma opção válida.")

        input("Digite Enter para continuar...")

def verListaDeAlugueis():

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

def cadastrarNovoAluguel():

    print("Cadastro de Aluguel - Insira as informações pedidas")

    verListaDeClientes()
    idCliente = input("Digite o ID do Cliente:")

    verListaDeLivros()
    idlivro = input("Digite o ID do Livro:")

    sqlInserir = f'''
    INSERT INTO "Alugueis"
    Values(default, '{idCliente}', '{idlivro}', default)
    '''

    if conexaoBanco.manipularBanco(sqlInserir):

        print(f"O Aluguel foi inserido com sucesso.")
    else:
        print("Falha ao cadastrar o Aluguel!")

def atualizarAluguel():
    print("Tela de atualização de Aluguel:")
    print("Lista de Alugueis")
    
    verListaDeAlugueis()
    AluguelEscolhido = input("Digite o id do Aluguel escolhido:")
    verAluguelEspecifico(AluguelEscolhido)
    novoIDCliente = input("Digite o novo ID do Cliente (vazio para não alterar):")
    novoIDLivro = input("Digite o novo ID do Livro (vazio para não alterar):")

    if novoIDCliente:
        conexaoBanco.manipularBanco(f'''
        UPDATE "Alugueis"
        SET "ID_Cliente" = '{novoIDCliente}',
        "Data do Aluguel" = default
        WHERE "ID" = {AluguelEscolhido}
        ''')

    if novoIDLivro:
        conexaoBanco.manipularBanco(f'''
        UPDATE "Alugueis"
        SET "ID_Livro" = '{novoIDLivro}',
        "Data do Aluguel" = default
        WHERE "ID" = {AluguelEscolhido}
        ''')

    print("Tentativa de alteração executada.")

def verAluguelEspecifico(idAluguel):
    Aluguel = conexaoBanco.consultarBanco(f'''SELECT * FROM "Alugueis"
    WHERE "ID" = {idAluguel}
    ''')

    if Aluguel:
        Aluguel = Aluguel[0]
        print("Aluguel Escolhido: ")
        print(f'''
        ID - {Aluguel[0]}
        ID_Cliente - {Aluguel[1]}
        ID_Livro - {Aluguel[2]}
        Data do Aluguel - {Aluguel[3]}
        ''')

        listaAlugueis = conexaoBanco.consultarBanco(f'''
        SELECT * FROM "Alugueis"
        WHERE "ID_Aluguel" = '{Aluguel[0]}'
        ''')

        if listaAlugueis:
            print("Lista de alugueis: ")
            print("ID | Cliente | Aluguel | Data de Aluguel")
            for aluguel in listaAlugueis:
                
                ClienteDoAluguel = conexaoBanco.consultarBanco(f'''
                SELECT * FROM "Cliente"
                WHERE "ID" = {aluguel[1]}
                ''')[0]

                LivroDoAluguel = conexaoBanco.consultarBanco(f'''
                SELECT * FROM "Livros"
                WHERE "ID" = {aluguel[2]}
                ''')[0]

                print(f"{aluguel[0]} | {ClienteDoAluguel[1]} | {LivroDoAluguel[1]} | {aluguel[3]}")

        else:
            print("O Aluguel não possui aluguéis cadastrados")

    else:
        print("O Aluguel não foi encontrado!")

def removerAluguel():
    print("Tela de remoção de Aluguel:")
    print("Lista de Alugueis")
    
    verListaDeAlugueis()
    AluguelEscolhido = input("Digite o id do Aluguel escolhido:")
    verAluguelEspecifico(AluguelEscolhido)
    confirmar = input("Deseja remover este Aluguel? (S/N)").upper()

    match confirmar:
        case "S":
           resultadoRemocao = conexaoBanco.manipularBanco(f'''
           DELETE FROM "Alugueis"
           WHERE "ID" = '{AluguelEscolhido}'
           ''')
           
           if resultadoRemocao:
               print("Aluguel removido com sucesso.")
           else:
               print("Aluguel não existe ou não foi removido.")
        case "N":
            print("Ok voltando ao menu principal")
        case _:
            print("Você digitou um comando inválido. Voltando ao menu.")

#----------------------------------------------------------------------------------------------------------------------#

while True:

    print('''
    Bem vindo a Biblioteca ZXC
    1. Menu Clientes
    2. Menu Livros
    3. Menu Aluguéis
    0. Sair
    ''')

    op = input("Escolha o menu que deseja acessar:")

    match op:
        case "1":
            verMenuClientes()
        case "2":
            verMenuLivros()
        case "3":
            verMenuAlugueis()
        case "0":
            print("Saindo da aplicação...")
            break
        case _:
            print("Escolha uma opção válida.")