Primero, asegúrate de instalar la librería necesaria:

pip install cryptography

🔐 Notas importantes:
La clave key se genera cada vez que corres el script. Si quieres descifrar el archivo más adelante, deberías guardar esa clave en un archivo y reutilizarla.

Puedes guardar la clave así:

# Guardar la clave
with open('clave.key', 'wb') as key_file:
    key_file.write(key)

# Leer la clave después
with open('clave.key', 'rb') as key_file:
    key = key_file.read()
cipher = Fernet(key)