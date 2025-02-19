import PyPDF2
from pdfminer.high_level import extract_text
from pdfminer.layout import LAParams
import os
import re
from unidecode import unidecode


def ask_company_name():

    company_name = input('Qual o nome da Empresa?\n')
    while not company_name:
        print("Nome da empresa é obrigatório.")
        company_name = input('Qual o nome da Empresa?\n')
    answer = input("O nome da empresa é : " + company_name + " ?  \nResponda com s ou n: \n")
    answer = answer.upper()
    
    while answer not in ("S", "N"): 
        answer = input("Por favor responda S ou N:\n") 
    if answer == "S": 
        print("ok")
        company_name = company_name.upper()
    # regex removidos para poder aceitar números, tratamento feito com unidecode
    #    company_name = re.sub('[^a-zA-Z\s]+', '', company_name)
    #    company_name = re.sub('\s+', ' ', company_name)
        return unidecode(company_name.strip())
    elif answer == "N": 
        return
    else: 
        print("Por favor responda s ou n:\n") 
        

def find_employee_name(text):
    print(text)

    field1 = ("Nome")
    field2 = ("Funcionário")
    name_index = text.find(field1)
    delfield = len(field1)
    if name_index == -1:
        func_index = text.find(field2)
        if func_index != -1:
            name_index = text.find("\n", func_index) + 1
            delfield = 0
    if name_index != -1:
        employee_name = text[name_index+delfield:text.find("\n", name_index)]
        keywords = ["RG", "R G", "Data d", "Sexo", "Cidade","CPF", "Função", "Funcao", "Fantasia", "Feminino", "Numero", "Número", "Bairro", "Masculino", "Idade", "CNPJ", "Departamento", "Setor", "Funcao", "Anos", "Meses", "Segurança"]
        for keyword in keywords:
                if keyword in employee_name:
                    end_index = employee_name.find(keyword)
                    employee_name = employee_name[:end_index].strip()       
    else:
        return
    return unidecode(employee_name.upper())

def try_nextpage(page_index):
    print(f"Não encontrou nome em pág {page_index} : {filename}")
    if page_index < numpages:
        pdf_file = open(filename, 'rb')
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = pdf_reader.pages[page_index].extract_text(space_width=100)
        pdf_file.close()
        employee_name = find_employee_name(text)
        if employee_name:
            print(f'Nome encontrado! :  {employee_name}\n')
            rename(company_name, employee_name,filename)
        else:
            page_index += 1
            employee_name = try_nextpage(page_index)
    else:
        print(f"Todas as páginas de {filename} foram testadas, texto não encontrado.")
        employee_name = "OUTROS"
        rename(company_name, employee_name,filename)
        
        
def rename(company_name, employee_name, filename):
    print("old: " + filename)
    employee_name = re.sub('[^a-zA-Z\s]+', '', employee_name)
    employee_name = re.sub('\s+', ' ', employee_name)
    employee_name = employee_name.strip()
    if employee_name == "DE CONTATO":
        employee_name = "CONTRATO"
    new_filename = "{}--{}--{:03d}.pdf".format(company_name, employee_name, 1)
    print("new: " + new_filename)
    if os.path.exists(new_filename):
        i = 1
        while os.path.exists("{}--{}--{:03d}.pdf".format(company_name, employee_name, i)):
            i += 1
        new_filename = "{}--{}--{:03d}.pdf".format(company_name, employee_name, i)
    os.rename(filename, new_filename)    

def organize_in_folder():
   
    for filename in os.listdir('.'):
        if '--' in filename:
            parts = filename.split('--')
            dir_name = parts[0]
            subdir_name = parts[1]
            if not os.path.exists(dir_name):
                os.mkdir(dir_name)
                print(f'Criando pasta : {dir_name}')
            if not os.path.exists(f'{dir_name}/{subdir_name}'):
                os.mkdir(f'{dir_name}/{subdir_name}')
                print(f'Criando pasta : {dir_name}/{subdir_name}')
            os.rename(filename, f'{dir_name}/{subdir_name}/{filename}')
            
            
company_name = ask_company_name()
if not company_name:
    company_name = ask_company_name()

for filename in os.listdir("."):

    if filename.endswith(".pdf"):
        pdf_file = open(filename, 'rb')
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        numpages = len(pdf_reader.pages)
        pdf_file.close()
        text = extract_text(filename, codec='utf-8', laparams=LAParams(char_margin=80, line_margin=1))
        
        if not company_name:
            company_name = "000"
            
        employee_name = find_employee_name(text)
        
        if not employee_name:


            employee_name = try_nextpage(0)
        
        if employee_name:
            print(f'Nome encontrado! : {employee_name}\n')
            rename(company_name, employee_name, filename)
            
print('Pronto! \nAgora confira os arquivos')
#print('\nConferido?')
#answer = input("Deseja organizar em pastas ?  \nResponda com s ou n: \n")
#
#while answer not in ("s", "n"): 
#    answer = input("Por favor responda s ou n:\n") 
#if answer == "s": 
#    print("ok")
#    organize_in_folder()
#elif answer == "n": 
#    print('ok! caso deseje organizar os arquivos depois, utilize o organizador.py')
#else: 
#    print("Por favor responda s ou n:\n") 
    