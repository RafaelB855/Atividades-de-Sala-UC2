import psycopg2

try:
    conn = psycopg2.connect(dbname="Escola2", host = "localhost", port = "5432", user= "postgres", password = "postgres")
    cursor = conn.cursor()
    print("Conectado com sucesso")

    cursor.execute('''
    Create table "Alunos"
    (
    "ID_Matricula" serial,
    "Nome" varchar(255) not null,
    "CPF" char(11) not null,
    "Endereço" varchar(255) default('Não Informado'),
    "AnoNascimento" integer,
    Primary Key("NroMatricula")
    )
    ''',

    '''
    Create table "Disciplina"
    (
    "ID_Disciplina" serial,
    "Nome" varchar(255) not null,
    "Codigo_Curso" integer,
    Primary Key("ID_Disciplina")
    )
    ''',

    '''
    Create table "Matricula"
    (
    "ID" serial,
    "ID_Matricula" int not null,
    "ID_Disciplina" int not null,
    "Semestre" varchar(255) not null,
    "Ano" integer not null default('2023'),
    "Nota" integer not null default('0'),
    "Faltas" integer not null default('0'),
    Primary Key("NroMatricula"),
        CONSTRAINT fk_ID_Matricula
        FOREIGN KEY("ID_Matricula")
        REFERENCES "Alunos"("ID_Matricula"),
    CONSTRAINT fk_ID_Disciplina
        FOREIGN KEY("ID_Disciplina")
        REFERENCES "Disciplina"("ID_Disciplina")
    )
    '''    
    )

    conn.commit()

    cursor.execute('''
    insert into "Alunos"
    Values(default, 'Jõa', '12345678910', default, 2002)
    
    ''')

    conn.commit()

    conn.close()
    print("Fechado com sucesso")

except(Exception, psycopg2.Error) as error:
    print("Ocorreu um erro!", error)