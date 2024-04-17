import os
import shutil

def add_names_to_files():
    # Establecer el directorio actual al directorio padre del script
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    os.chdir('..')

    # Procesar cada archivo .sql en el directorio
    for filename in os.listdir('.'):
        if filename.endswith('.sql'):
            process_file(filename)

    print("Proceso completado.")

def process_file(filename):
    # Obtener el nombre del archivo sin extensión
    base_name = os.path.splitext(filename)[0]

    # Crear un archivo temporal y escribir el nombre en él
    temp_filename = f"{base_name}_temp.sql"
    with open(temp_filename, 'w') as temp_file, open(filename, 'r') as original_file:
        temp_file.write(f"--* {filename}\n--\n")
        shutil.copyfileobj(original_file, temp_file)

    # Reemplazar el archivo original con el archivo temporal
    shutil.move(temp_filename, filename)

if __name__ == "__add_names_to_files__":
    add_names_to_files()