from thefuzz import fuzz
from os import listdir
import os
import re



def find_similar_filenames(threshold):

    similar_filenames = []
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            similarity = fuzz.token_set_ratio(names[i], names[j])
            if similarity >= threshold:
                similar_filenames.append((names[i], names[j]))
    return similar_filenames

def rename(employee_name, filename):
    company_name = parts[0]
    print("old: " + filename)
    employee_name = re.sub('[^a-zA-Z\s]+', '', employee_name)
    new_filename = "{}--{}--{:03d}.pdf".format(company_name, employee_name, 1)
    print("new: " + new_filename)
    if os.path.exists(new_filename):
        i = 1
        while os.path.exists("{}--{}--{:03d}.pdf".format(company_name, employee_name, i)):
            i += 1
        new_filename = "{}--{}--{:03d}.pdf".format(company_name, employee_name, i)
    os.rename(filename, new_filename) 


# Cria um dicionário para armazenar os nomes de arquivo
file_dict = {}

for filename in os.listdir('.'):
    if filename.endswith(".pdf"):
        parts = filename.split("--")
        name2 = parts[1]
        file_dict[parts[1]] = [filename]
        

names = list(file_dict.keys())
print(names)
print('\n Nomes parecidos \n')
threshold = 80

lista_nomes = find_similar_filenames( threshold)

for index, nomes in enumerate(lista_nomes):
    print(f"1.{nomes[0]}")
    print(f"2.{nomes[1]}")
    opcao = int(input("Escolha uma opção para renomear o arquivo: "))
    novo_nome = lista_nomes[index][opcao - 1]
    velho_nome = lista_nomes[index][opcao - 2]
    old_filename = str(file_dict[velho_nome])[2:-2]
    new_employee_name = str(novo_nome)
    print(old_filename)
    print(new_employee_name)
    rename(new_employee_name,old_filename)
    print(f"Arquivo renomeado para: {novo_nome}")
    