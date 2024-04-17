import os

def clean_directory():
    os.chdir('..')
    current_directory = os.getcwd()
    allowed_extensions = ['.bat', '.7z', '.txt', '.git', '.md', '.py']
    
    # Listar todos los archivos en el directorio, asegurando no incluir directorios en el proceso
    for filename in os.listdir(current_directory):
        # Construir la ruta completa del archivo
        file_path = os.path.join(current_directory, filename)
        # Verificar si es un archivo y si no tiene una extensión permitida
        if os.path.isfile(file_path) and not any(filename.endswith(ext) for ext in allowed_extensions):
            # Eliminar el archivo
            os.remove(file_path)
            print(f"Eliminado: {filename}")

    print(f"Se han eliminado todos los archivos (excepto los permitidos) en {current_directory}.")

if __name__ == "__clean_directory__":
    clean_directory()
