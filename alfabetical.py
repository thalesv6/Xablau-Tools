import os
import shutil

def organizar_pastas_por_letra(diretorio):
    pastas = [pasta for pasta in os.listdir(diretorio) if os.path.isdir(os.path.join(diretorio, pasta))]

    for letra in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        nova_pasta = os.path.join(diretorio, letra)
        os.makedirs(nova_pasta, exist_ok=True)

    for pasta in pastas:
        if pasta[0].upper() in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            letra_inicial = pasta[0].upper()
            destino = os.path.join(diretorio, letra_inicial, pasta)
            origem = os.path.join(diretorio, pasta)
            shutil.move(origem, destino)

if __name__ == "__main__":
    diretorio_a_organizar = "."
    
    organizar_pastas_por_letra(diretorio_a_organizar)
    