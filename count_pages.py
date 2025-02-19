import os
from multiprocessing import Pool, cpu_count, freeze_support
from PyPDF2 import PdfReader

def count_pages(file_path):
    with open(file_path, 'rb') as file:
        pdf = PdfReader(file)
        return len(pdf.pages)

def count_pages_in_dir(directory):
    num_pages = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.pdf'):
                file_path = os.path.join(root, file)
                num_pages += count_pages(file_path)
    return num_pages

if __name__ == '__main__':
    freeze_support()
    directory = input("Digite o caminho do diretório: ")
    num_processes = cpu_count()
    with Pool(num_processes) as pool:
        result = pool.map(count_pages_in_dir, [directory])
        total_pages = sum(result)
        print(f"Total de páginas em {directory}: {total_pages}")
        