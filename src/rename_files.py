import os
import datetime
import re

def rename_files():
    # Solicitar datos del usuario
    project_name = input("¿Cuál es el nombre del proyecto? ")
    sprint_hu = input("¿Cuál es el sprint y HU? ")
    
    # Obtener la fecha actual
    today = datetime.date.today()
    year = today.year
    month = today.month
    day = today.day

    print("========================================")
    print(f"Fecha: {year}-{month:02}-{day:02}")
    print("========================================")

    # Cambiar al directorio padre de src
    os.chdir('..')  # Esto asume que el script se ejecuta desde el directorio src

    # Buscar y procesar todos los archivos U y V en el directorio actual
    for filename in os.listdir('.'):
        if re.match(r'[UV]\d{2}.*\.sql', filename):
            process_file(filename, year, month, day, project_name, sprint_hu)

def process_file(filename, year, month, day, project_name, sprint_hu):
    basename, ext = os.path.splitext(filename)
    if not re.match(r'^[UV]_[0-9]{4}[0-9]{2}[0-9]{2}_[0-9]{2}_.+', basename):
        new_filename = f"{basename[0]}_{year}{month:02}{day:02}_{basename[1:3]}_{project_name}_{sprint_hu}{ext}"
        new_full_path = os.path.join(os.path.dirname(filename), new_filename)
        print("========================================")
        print(f"Renombrando: {filename}")
        print(f"Nuevo nombre: {new_filename}")
        os.rename(os.path.join(os.getcwd(), filename), os.path.join(os.getcwd(), new_filename))
        print("========================================")

if __name__ == "__rename_files__":
    rename_files()