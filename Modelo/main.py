import psycopg2

class Conexao:

    def __init__(self, banco, host, port, user, senha):

        self._banco = banco
        self._host = host
        self._port = port
        self._user = user
        self._senha = senha
    
    def consultarBanco(self,sql):

        conn = psycopg2.connect(dbname=self._banco, host=self._host, port=self._port, user=self._user,password=self._senha )
        cursor = conn.cursor()

        cursor.execute(sql)

        resultado = cursor.fetchall()

        cursor.close()
        conn.close()

        return resultado


    def manipularBanco(self,sql):

        conn = psycopg2.connect(dbname=self._banco, host=self._host, port=self._port, user=self._user,password=self._senha )
        cursor = conn.cursor()

        cursor.execute(sql)

        conn.commit()

        cursor.close()
        conn.close()

conexaoBanco = Conexao("Mercado","localhost","5432","postgres","postgres")

# conexaoBanco.manipularBanco('''
#         CREATE TABLE "Cliente"(
#         "ID" serial,
#         "Nome" varchar(255) NOT NULL,
#         "Cpf" int not null,
#         PRIMARY KEY("ID")
#         )
        
#         ''')

# conexaoBanco.manipularBanco('''
#         CREATE TABLE "Produto"(
#         "Id" serial,
#         "Nome" varchar(255) NOT NULL,
#         "Preço" int not null,
#         "Estoque" int not null default 0,
#         PRIMARY KEY("Id")
#         )
        
#         ''')

while True:

    try:

        # print("Cadastro de Cliente")
        # nomeC = input("Digite o nome do Cliente: ")
        # CpfC = input("Digite o Cpf do Cliente: ")

        # conexaoBanco.manipularBanco(f'''
        # INSERT INTO "Cliente"
        # VALUES(default, '{nomeC}', '{CpfC}')
        
        # ''')

        print("Cadastro de Produto(Digite 0 para sair)")
        nomeP = input("Digite o nome do Produto: ")
        if nomeP == "0":
            break
        preçoC = input("Digite o preço do Produto: ")
        estoqueC = input("Digite a quantidade de estoque do Produto: ")

        conexaoBanco.manipularBanco(f'''
        INSERT INTO "Produto"
        VALUES(default, '{nomeP}', '{preçoC}', '{estoqueC}')
        
        ''')

    except(Exception, psycopg2.Error) as error:
        print("Ocorreu um erro", error)