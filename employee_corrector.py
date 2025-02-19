import os


def rename(employee_name, filename):
    print("old: " + filename)
    company_name = parts[0]
    new_filename = "{}--{}--{:03d}.pdf".format(company_name, employee_name, 1)
    print("new: " + new_filename)
    if os.path.exists(new_filename):
        i = 1
        while os.path.exists("{}--{}--{:03d}.pdf".format(company_name, employee_name, i)):
            i += 1
        new_filename = "{}--{}--{:03d}.pdf".format(company_name, employee_name, i)
    os.rename(filename, new_filename) 
	
	
for filename in os.listdir('.'):
    if filename.endswith(".pdf"):
        os.startfile(filename)
        employee_name = unidecode(str.upper(input("Corrija o nome do funcionário:\n")))
        employee_name = employee_name.strip()
        parts = filename.split("--")
        rename(employee_name, filename)
        