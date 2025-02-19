import os
from PyPDF2 import PdfReader
    
def count_pdf_pages(directory):
    total_pages = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".pdf"):
                file_path = os.path.join(root, file)
                with open(file_path, "rb") as pdf_file:
                    pdf_reader = PdfReader(pdf_file)
                    total_pages += len(pdf_reader.pages)
    return total_pages

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

print('Este programa organiza os arquivos em pastas.\nEle separa arquivos com nome Diretório--Subdiretório--Contador')


directory = '.'
total_pages = count_pdf_pages(directory)
print("O número total de páginas é:", total_pages)

print('\nNomes dos arquvios conferidos?')
answer = str.upper(input("Deseja organizar em pastas ?  \nResponda com s ou n: \n"))

while answer not in ("S", "N"): 
    answer = input("Por favor responda s ou n:\n") 
if answer == "S": 
    print("ok")
    organize_in_folder()
elif answer == "N": 
    print('ok! caso deseje organizar os arquivos depois, utilize o organizador.py')
else: 
    print("Por favor responda s ou n:\n") 
    