import PyPDF2
from pdfminer.high_level import extract_text
from pdfminer.layout import LAParams
import os
import re
from unidecode import unidecode



def find_employee_name(text):

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
        pdf_file = open(filepath, 'rb')
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = pdf_reader.pages[page_index].extract_text(space_width=100)
        pdf_file.close()
        employee_name = find_employee_name(text)
        if employee_name:
            print(f'Nome encontrado! :  {employee_name}\n')
            rename(company_name, employee_name,filepath)
        else:
            page_index += 1
            employee_name = try_nextpage(page_index)
    else:
        print(f"Todas as páginas de {filename} foram testadas, texto não encontrado.")
        employee_name = "OUTROS"
        rename(company_name, employee_name,filepath)


def rename(company_name, employee_name, filepath):
    print("old: " + filepath)
    employee_name = re.sub('[^a-zA-Z\s]+', '', employee_name)
    employee_name = re.sub('\s+', ' ', employee_name)
    employee_name = employee_name.strip()
    if employee_name == "DE CONTATO":
        employee_name = "CONTRATO"
    new_filename = "{}--{}--{:03d}.pdf".format(company_name, employee_name, 1)
    print("new: " + new_filename)
    new_filepath = os.path.join(root, new_filename)
    if os.path.exists(new_filepath):
        i = 1
        while os.path.exists(new_filepath):
            new_filename = "{}--{}--{:03d}.pdf".format(company_name, employee_name, i)
            new_filepath = os.path.join(root, new_filename)
            i += 1
    os.rename(filepath, new_filepath)



for root, dirs, files in os.walk("."):
        for filename in files:
            if filename.endswith(".pdf"):
                company_name = os.path.basename(root)
                print(company_name)
                filepath = os.path.join(root, filename)
                print(filepath)
                pdf_file = open(filepath, 'rb')
                pdf_reader = PyPDF2.PdfReader(pdf_file)
                numpages = len(pdf_reader.pages)
                pdf_file.close()
                text = extract_text(filepath, codec='utf-8', laparams=LAParams(char_margin=80, line_margin=1))

                if not company_name:
                    company_name = "000"

                employee_name = find_employee_name(text)

                if not employee_name:


                    employee_name = try_nextpage(0)

                if employee_name:
                    print(f'Nome encontrado! : {employee_name}\n')
                    rename(company_name, employee_name, filepath)

print('Pronto! \nAgora confira os arquivos')


