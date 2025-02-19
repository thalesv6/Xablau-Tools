import os
import PyPDF2

def split_pdf(input_file_path, output_dir_path):

    with open(input_file_path, 'rb') as input_file:
        pdf_reader = PyPDF2.PdfReader(input_file)

        output_file_number = 1

        output_file = PyPDF2.PdfWriter()


        for pag_number in range(len(pdf_reader.pages)):
            pag = pdf_reader.pages[pag_number]
            print(f'\n \n \n PAGINA {pag_number} \n \n \n')
            print(pag.extract_text())
            if pag.extract_text() == "XABLAU":
                
                if len(output_file.pages) > 0:
                    output_file_path = f'{output_dir_path}/output{output_file_number}.pdf'
                    with open(output_file_path, 'wb') as output_file_stream:
                        output_file.write(output_file_stream)

                    output_file = PyPDF2.PdfWriter()
                    output_file_number += 1
            else:

                output_file.add_page(pag)


        if len(output_file.pages) > 0:
            output_file_path = f'{output_dir_path}/output{output_file_number}.pdf'
            with open(output_file_path, 'wb') as output_file_stream:
                output_file.write(output_file_stream)

for filename in os.listdir("."):

    if filename.endswith(".pdf"):                
        split_pdf(filename, '.')
        
        