import os
from unidecode import unidecode


def rename(company_name, filename):
    print("old: " + filename)
    employee_name = parts[1]
    new_filename = "{}--{}--{:03d}.pdf".format(company_name, employee_name, 1)
    print("new: " + new_filename)
    if os.path.exists(new_filename):
        i = 1
        while os.path.exists("{}--{}--{:03d}.pdf".format(company_name, employee_name, i)):
            i += 1
        new_filename = "{}--{}--{:03d}.pdf".format(company_name, employee_name, i)
    os.rename(filename, new_filename) 
	
company_name = unidecode(str.upper(input("Corrija o nome da empresa:\n")))	
company_name = company_name.strip()
	
for filename in os.listdir('.'):
    if filename.endswith(".pdf"):
        parts = filename.split("--")
        rename(company_name, filename)
