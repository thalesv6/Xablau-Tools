# Xablau Tools

## 🇬🇧 English
I started a job scanning and indexing documents, so I wrote these simple scripts to automate and make my work easier. If you're dealing with tons of files, this might save you some headaches too!

### 🔧 Tools & Usage

#### 1. Split Files Scripts
Splits a PDF into individual pages whenever it finds the word **XABLAU**. Handy for scanning multiple documents together.
```sh
python xablau.py input.pdf
```

#### 2. Rename Scripts 🏷️
These help keep your files properly named.
- **rename_automatic.py** – Extracts employee names from PDFs and renames them.
- **rename_manual.py** – Asks for company and employee names to rename PDFs manually.
- **reset_names.py** – Resets all filenames to `001.pdf`, `002.pdf`, etc.
- **company_corrector.py** – Fixes company names in filenames.
- **employee_corrector.py** – Fixes employee names in filenames.
- **simillar_names.py** – Finds and suggests corrections for similar filenames.

#### 3. Organizer Scripts 📂
Sorts and organizes your files.
- **remove_empty.py** – Deletes empty folders and `desktop.ini` files.
- **organizer.py** – Counts PDF pages and organizes them into folders.
- **organizer_subfolders.py** – Does the same but also processes subfolders.
- **alfabetical.py** – Moves files into A-Z folders based on the first letter.

#### 4. Page Management 📄
- **count_pages.py** – Counts total pages in all PDFs within a folder.

### 💻 Running the Scripts
Just open a terminal in the folder where the script is located and run:
```sh
python script_name.py 
```

---

## 🇧🇷 Português
Comecei a trabalhar com digitalização e indexação de documentos, então escrevi esses scripts para automatizar e facilitar o trabalho. Se você também lida com muitos arquivos, espero que isso te ajude!

### 🔧 Ferramentas e Uso

#### 1. Scripts de Divisão de Arquivos 
Divide um PDF em páginas individuais sempre que encontra a palavra **XABLAU**. Uso para escanear uma grande quantidade de documentos de uma vez separado por paginas padronizadas.
```sh
python xablau.py arquivo.pdf
```

#### 2. Scripts de Renomeação 🏷️
Facilitam a organização dos nomes dos arquivos.
- **rename_automatic.py** – Extrai nomes dos funcionários e renomeia os PDFs automaticamente.
- **rename_manual.py** – Pede o nome da empresa e do funcionário para renomear os PDFs manualmente.
- **reset_names.py** – Renomeia todos os PDFs como `001.pdf`, `002.pdf`, etc.
- **company_corrector.py** – Corrige nomes de empresas nos arquivos.
- **employee_corrector.py** – Corrige nomes de funcionários nos arquivos.
- **simillar_names.py** – Encontra e sugere correções para nomes de arquivos parecidos.

#### 3. Scripts de Organização 📂
Organizam seus arquivos de forma prática.
- **remove_empty.py** – Remove pastas vazias e arquivos `desktop.ini`.
- **organizer.py** – Conta páginas dos PDFs e os organiza em pastas.
- **organizer_subfolders.py** – Faz o mesmo, mas também trabalha com subpastas.
- **alfabetical.py** – Move arquivos para pastas A-Z com base na primeira letra.

#### 4. Gerenciamento de Páginas 📄
- **count_pages.py** – Conta o número total de páginas de todos os PDFs em uma pasta.

### 💻 Executando os Scripts
Abra um terminal na pasta onde o script está localizado e rode:
```sh
python nome_do_script.py 
```

---

