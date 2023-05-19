# Lista de digimons, para "simular um banco de dados
digimons = [(1, 'Beelzemon X', 'Virus Attribute', 'Pitch Black'),(2, 'Gaioumon', 'Virus Attribute', 'Steel'),(3, 'Magnamon X', 'Vaccine Attribute', 'Light'),(4, 'Sleipmon X', 'Vaccine Attribute', 'Ice'),(5, 'Dynasmon X', 'Data Attribute', 'Wind') ]

# link com os comandos do ".format" https://www.w3schools.com/python/ref_string_format.asp
print("")
print("{:^60}".format("Meus Filhos, kkk"))
print("")

# Print da primeira linha com o nome das colunas
# No caso usei :^ que alinha o resultado no centro (dentro do espaço que eu especifiquei, 5, 15, 20...) 
print("{:^5} | {:^15} | {:^20} | {:^20}".format("Id", "Nome", "Attribute", "Elemental"))

# Print dos dados dos Digimons
# Aqui já usei :< que alinha o resultado à esquerda (dentro do espaço que eu especifiquei, 5, 15, 20...) 
for digimon in digimons:
    print("{:^5} | {:<15} | {:<20} | {:<20}".format(digimon[0],digimon[1],digimon[2],digimon[3]) )