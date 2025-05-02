from cryptography.fernet import Fernet
import json

# =======================
# GENERACIÓN DE LA CLAVE
# =======================

# Genera una clave nueva para cifrar y descifrar
# Esta clave debe guardarse de forma segura si se quiere reutilizar
key = Fernet.generate_key()

# Crea un objeto Fernet con la clave
cipher = Fernet(key)

# =======================================
# LECTURA Y CIFRADO DEL ARCHIVO JSON
# =======================================

# Lee el contenido del archivo productos.json
with open('productos.json', 'r', encoding='utf-8') as file:
    data = json.load(file)  # Carga el contenido JSON en un diccionario de Python

# Convierte el diccionario a una cadena de texto (JSON serializado)
json_str = json.dumps(data)

# Codifica la cadena a bytes para poder cifrarla
json_bytes = json_str.encode('utf-8')

# Cifra el contenido en bytes usando Fernet
encrypted = cipher.encrypt(json_bytes)

# Guarda el contenido cifrado en un archivo
with open('productos_encriptado.txt', 'wb') as file:
    file.write(encrypted)

print("Archivo cifrado guardado como 'productos_encriptado.txt'")

# ==========================================
# DESCIFRADO DEL ARCHIVO Y MOSTRAR RESULTADO
# ==========================================

# Lee el contenido cifrado del archivo
with open('productos_encriptado.txt', 'rb') as file:
    encrypted_data = file.read()

# Descifra el contenido usando la misma clave
decrypted_bytes = cipher.decrypt(encrypted_data)

# Convierte los bytes descifrados de vuelta a cadena
decrypted_str = decrypted_bytes.decode('utf-8')

# Convierte la cadena JSON de vuelta a diccionario
decrypted_data = json.loads(decrypted_str)

print("Contenido descifrado:")
print(decrypted_data)
