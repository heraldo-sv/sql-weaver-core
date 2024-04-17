import os
import subprocess
from pathlib import Path

def compress_files():
    # Ruta a 7-Zip (ajustar según la instalación)
    ruta_compresor = r"C:\Program Files\7-Zip"
    
    # Cambiar al directorio padre desde el directorio del script
    os.chdir(Path(__file__).parent.parent)
    ubicacion_actual = os.getcwd()

    # Obtener el nombre del primer archivo .sql encontrado
    sql_files = list(Path(ubicacion_actual).glob('*.sql'))
    if sql_files:
        filename = sql_files[0].stem
        short_name = filename[-12:]  # Tomar los últimos 12 caracteres del nombre

        # Cambiar al directorio del compresor
        os.chdir(ruta_compresor)

        # Comprimir los archivos .sql en un archivo 7z
        output_zip = f"{ubicacion_actual}\\{short_name}.7z"
        subprocess.run([f"{ruta_compresor}\\7z.exe", 'a', '-t7z', output_zip, f"{ubicacion_actual}\\*.sql"], check=True)

        # Eliminar los archivos .sql de la ubicación original (descomentar para activar)
        # for sql_file in sql_files:
        #     sql_file.unlink()

        print(f"¡Archivos .sql comprimidos exitosamente en {short_name}.7z!")
        
        # Regresar al directorio original del script
        os.chdir(Path(__file__).parent)

if __name__ == "__compress_files__":
    compress_files()
