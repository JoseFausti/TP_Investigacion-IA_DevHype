from cryptography.fernet import Fernet
import json

# Genera una clave de cifrado (esto debe guardarse en un lugar seguro para poder descifrar después)
clave = Fernet.generate_key()
cipher_suite = Fernet(clave)

# Guarda la clave en un archivo para su uso posterior
with open("clave.key", "wb") as clave_archivo:
    clave_archivo.write(clave)

# Función para cifrar el contenido de un archivo JSON
def cifrar_json(nombre_archivo):
    # Abre el archivo JSON y lo lee
    with open(nombre_archivo, "r") as archivo:
        datos = archivo.read()  # Lee el contenido del JSON como texto

    # Cifra el contenido utilizando la clave generada
    datos_cifrados = cipher_suite.encrypt(datos.encode())

    # Guarda el contenido cifrado en un nuevo archivo
    with open("productos_cifrados.json", "wb") as archivo_cifrado:
        archivo_cifrado.write(datos_cifrados)

    print("Archivo JSON cifrado correctamente.")

# Función para descifrar el contenido de un archivo JSON cifrado
def descifrar_json(nombre_archivo_cifrado):
    # Lee la clave almacenada
    with open("clave.key", "rb") as clave_archivo:
        clave_leida = clave_archivo.read()

    # Crea una nueva instancia de Fernet con la clave recuperada
    cipher_suite = Fernet(clave_leida)

    # Abre el archivo cifrado y lo lee
    with open(nombre_archivo_cifrado, "rb") as archivo_cifrado:
        datos_cifrados = archivo_cifrado.read()  # Lee los datos cifrados

    # Descifra los datos utilizando la clave
    datos_descifrados = cipher_suite.decrypt(datos_cifrados).decode()

    # Convierte el texto JSON descifrado en un diccionario
    datos_json = json.loads(datos_descifrados)

    print("Archivo JSON descifrado correctamente.")
    print("Contenido:", datos_json)

# Ejecutar el cifrado y descifrado
cifrar_json("productos.json")
descifrar_json("productos_cifrados.json")