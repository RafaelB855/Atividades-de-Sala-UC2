import psycopg2

# def criarTabelaFuncionario():
#     sql = '''
#     CREATE TABLE "Funcionario" (
#     "ID_Fun" serial,
#     "Nome" varchar(255) NOT NULL,
#     "Salario" money NOT NULL default 0.00,
#     "Cargo" varchar(225) NOT NULL default 'Autônomo',
#     "Id_Dep" int NOT NULL,
#     primary key("ID_Fun")
#     )
#     '''
#     return sql

#Criar Chave estrangeira em uma table existente#
#ALTER TABLE "Funcionario"
# ADD CONSTRAINT fk_departamento
#         FOREIGN KEY("Id_Dep")
#         REFERENCES "Departamento"("ID_Dep")
#         ON DELETE NO ACTION
#         ON UPDATE NO ACTION

# def criarTabelaDepartamento():
#     sql = '''
#     CREATE TABLE "Departamento" (
#     "ID_Dep" serial,
#     "Nome" varchar(255) NOT NULL,
#     primary key("ID_Dep")
#     )
#     '''
#     return sql

# try:
#     conn = psycopg2.connect(dbname="ZXC", host = "localhost", port = "5432", user= "postgres", password = "postgres")
#     cursor = conn.cursor()
#     print("Conectado com sucesso")

#     cursor.execute(criarTabelaFuncionario())
#     conn.commit()

#     cursor.execute(criarTabelaDepartamento())
#     conn.commit()

#     print("Tabelas criadas com sucesso")

#     conn.close()

#     print("Conexão fechada com sucesso")


# except(Exception, psycopg2.Error) as error:
#     print("Ocorreu um erro!", error)

def verFuncionarioEspecifico(id):

    cursor.execute(f'''
    Select * from "Funcionario"
    WHERE "Id" = '{id}'
    ''')

    funcionario = cursor.fetchone()

    if funcionario:
        print(f'''
        ID: {funcionario[0]}
        Nome: {funcionario[1]}
        Salário: {funcionario[2]}
        Cargo: {funcionario[3]}
        Departamento: {funcionario[4]}
        ''')

    else:
        print("Funcionário não encontrado.")

def verDepartamentoEspecifico(id):

    cursor.execute(f'''
    Select * from "Departamento"
    WHERE "Id" = '{id}'
    ''')

    departamento = cursor.fetchone()

    if departamento:
        print(f'''
        ID: {departamento[0]}
        Nome: {departamento[1]}
        ''')

    else:
        print("Departamento não encontrado.")

def verFuncionarios():
    cursor.execute('''
        SELECT * FROM "Funcionario"
        ORDER BY "ID_Fun" ASC
        ''')

    ListadeFuncionios = cursor.fetchall()
    print("ID -- Nome")

    for funcionario in ListadeFuncionios:
        print(f"{funcionario[0]} -- {funcionario[1]}")

    idEscolhido = input("Digite o id de um funcionário que deseja ver mais informações:(0 = Voltar) ")

    if idEscolhido != "0":
        verFuncionarioEspecifico(idEscolhido)
    else:
        print("Voltando para o menu principal.")

def verDepartamento():
    cursor.execute('''
        SELECT * FROM "Departamento"
        ORDER BY "ID_Dep" ASC
        ''')

    ListadeDepartamento = cursor.fetchall()
    print("ID -- Nome")

    for departamento in ListadeDepartamento:
        print(f"{departamento[0]} -- {departamento[1]}")
    print(ListadeDepartamento)

    idEscolhido = input("Digite o id de um departamento que deseja ver mais informações:(0 = Voltar) ")

    if idEscolhido != "0":
        verDepartamentoEspecifico(idEscolhido)
    else:
        print("Voltando para o menu principal.")

def inserirFuncionario():
    print("Você está cadastrando um funcionário.")

    novoFuncionarioNome = input("Digite o nome do novo funcionário: ")
    novoFuncionarioSalario = input("Digite o salário do novo funcionário: ")
    novoFuncionarioCargo = input("Digite o cargo do novo funcionário: ")
    novoFuncionarioIdDepartamento = input("Digite o departamento do novo funcionário: ")

    cursor.execute(f'''
    INSERT INTO "Funcionario"
    Values(default, '{novoFuncionarioNome}', '{novoFuncionarioSalario}', '{novoFuncionarioCargo}', '{novoFuncionarioIdDepartamento}')
    
    ''')

    conn.commit()

    print("Funcionário Inserido!")

def inserirDepartamento():
    print("Você está cadastrando um departamento.")

    novoDepartamentoNome = input("Digite o nome do novo departamento: ")


    cursor.execute(f'''
    INSERT INTO "Departamento"
    Values(default, '{novoDepartamentoNome}')
    
    ''')

    conn.commit()

    print("Departamento Inserido!")


try:
    conn = psycopg2.connect(dbname="ZXC", host = "localhost", port = "5432", user= "postgres", password = "postgres")
    cursor = conn.cursor()
    print("Conectado com sucesso")


except(Exception, psycopg2.Error) as error:
    print("Ocorreu um erro!", error)

while True:
    try:
        print('''
        
        Bem vindo ao gerenciamento SQL Soluções

        Escolha uma opção do menu:

        1 - Ver Funcionários
        2 - Ver Derpatamentos
        3 - Inserir Funcionário
        4 - Inserir Departamento
        0 - Sair do menu
        
        ''')

        op = input("Digite a opção escolhida:")

        match op:
            case "1":
                verFuncionarios()

            case "2":
                verDepartamento()
            
            case "3":
                inserirFuncionario()

            case "4":
                inserirDepartamento()
                
            case "0":
                print("Fechada a conexão com sucesso!")
                cursor.close()
                conn.close()
                break

            case _:
                print("Opção invalida!")

        input("Tecle enter para continuar.")

    except (Exception, psycopg2.Error) as error:

        print("Ocorreu um erro", error)
