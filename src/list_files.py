import os
import subprocess

def list_files():
    # Configurar la consola para UTF-8
    subprocess.run('chcp 65001', shell=True)

    # Directorio actual
    current_dir = os.getcwd()

    # Crear una lista de todos los archivos .sql en el directorio actual y subdirectorios
    with open('print-withing-path.txt', 'w', encoding='utf-8') as file:
        for root, dirs, files in os.walk(current_dir):
            for filename in files:
                if filename.endswith('.sql'):
                    file.write(os.path.join(root, filename) + '\n')

    # Crear una lista de todos los archivos .sql solo en el directorio actual
    with open('print-without-path.txt', 'w', encoding='utf-8') as file:
        for filename in os.listdir(current_dir):
            if filename.endswith('.sql'):
                file.write(filename + '\n')

    print("Lista de archivos creada...")

if __name__ == "__list_files__":
    list_files()
