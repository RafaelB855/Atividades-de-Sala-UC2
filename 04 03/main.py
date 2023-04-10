import json 

caminho = "pessoa.csv"

class Pessoa():
    def __init__(self,nome,idade):
        self._nome = nome
        self._idade = idade

caminho = "Atividade1/pessoa.json"

def salvarPessoaJson(novaPessoa):

    with open(caminho,"r") as pessoaJson:

        listaPessoa = json.load(pessoaJson)
   
    listaPessoa.append({'nome':novaPessoa._nome,'idade':novaPessoa._idade})

    with open(caminho,"w") as pessoaJson:
        json.dump(listaPessoa,pessoaJson, indent=2)

def recuperarPessoaJson():

    with open(caminho,"r") as pessoaJson:
        listaPessoa = json.load(pessoaJson)

    listaObjetos = []

    for pessoa in listaPessoa:
        listaObjetos.append(Pessoa(pessoa['nome'],pessoa['idade']))
        return listaObjetos

pessoa1 = Pessoa("Marcos",30)

salvarPessoaJson(pessoa1)

print(listaObjetos)
