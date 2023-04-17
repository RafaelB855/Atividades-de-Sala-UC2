import psycopg2

try:
    conn = psycopg2.connect(dbname="Escola2", host = "localhost", port = "5432", user= "postgres", password = "postgres")
    cursor = conn.cursor()
    print("Conectado com sucesso")

    # cursor.execute('''
    # Drop table if exists "Alunos";

    # Create table "Alunos"
    # (
    # "NroMatricula" serial,
    # "Nome" varchar(255) not null,
    # "CPF" char(11) not null,
    # "Endereço" varchar(255) default('Não Informado'),
    # "AnoNascimento" integer,
    # Primary Key("NroMatricula")
    # )
    # ''')

    # conn.commit()

    cursor.execute('''
    insert into "Alunos"
    Values(default, 'Jõa', '12345678910', default, 2002)
    
    ''')

    conn.commit()

    conn.close()
    print("Fechado com sucesso")

except(Exception, psycopg2.Error) as error:
    print("Ocorreu um erro!", error)