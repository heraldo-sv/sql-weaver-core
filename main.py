import os

from src.rename_files import rename_files
from src.add_names_to_files import add_names_to_files
from src.list_files import list_files
from src.compress_files import compress_files
from src.clean_directory import clean_directory

def main():
    # Define the path to the 'src' directory where Python modules are stored
    src_dir = os.path.join(os.path.dirname(__file__), 'src')
    if not os.path.exists(src_dir):
        print("Directorio src no encontrado. Asegúrese que existe en la misma ubicación que este script.")
        return

    # Change to the directory where the SQL files are expected to be located
    os.chdir(src_dir)

    print("1. Renombrando archivos .sql...")
    rename_files()

    print("2. Agregando nombre en archivos .sql...")
    add_names_to_files()

    print("3. Creando listado...")
    list_files()

    print("4. Comprimiendo...")
    compress_files()

    print("5. Limpiando...")
    clean_directory()

    print("Proceso completado.")

if __name__ == "__main__":
    main()
