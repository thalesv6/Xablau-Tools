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

def organize_in_folder(directory='.'):
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if '--' in filename:
                parts = filename.split('--')
                if len(parts) == 3:
                    dir_name, subdir_name, _ = parts
                    dir_path = os.path.join(directory, dir_name, subdir_name)
                    if not os.path.exists(dir_path):
                        os.makedirs(dir_path)
                        print(f'Creating folder: {dir_path}')
                    
                    file_path = os.path.join(root, filename)
                    new_file_path = os.path.join(dir_path, filename)
                    
                    # Check if the file already exists in the target directory
                    if os.path.exists(new_file_path):
                        base, ext = os.path.splitext(new_file_path)
                        counter = 1
                        while os.path.exists(new_file_path):
                            new_file_path = f"{base}_{counter}{ext}"
                            counter += 1
                    
                    os.rename(file_path, new_file_path)
                    print(f'Moving file to: {new_file_path}')
                    
def remove_desktop_ini_and_empty_folders(directory='.'):
    # Walk through the directory tree
    for root, dirs, files in os.walk(directory, topdown=False):
        # Remove desktop.ini files
        for filename in files:
            if filename.lower() == 'desktop.ini':
                file_path = os.path.join(root, filename)
                try:
                    os.remove(file_path)
                    print(f'Removed file: {file_path}')
                except Exception as e:
                    print(f'Error removing file {file_path}: {e}')
        
        # Remove empty directories
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            try:
                if not os.listdir(dir_path):  # Check if the directory is empty
                    os.rmdir(dir_path)
                    print(f'Removed empty folder: {dir_path}')
            except Exception as e:
                print(f'Error removing folder {dir_path}: {e}')

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
    remove_desktop_ini_and_empty_folders()
elif answer == "N": 
    print('ok! caso deseje organizar os arquivos depois, utilize o organizador.py')
else: 
    print("Por favor responda s ou n:\n") 
    