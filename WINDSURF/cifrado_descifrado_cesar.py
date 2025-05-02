# Importamos las bibliotecas necesarias
import json
from cryptography.fernet import Fernet
import base64

class JsonCrypto:
    def __init__(self):
        # Generamos una clave de cifrado
        self.key = Fernet.generate_key()
        self.cipher_suite = Fernet(self.key)

    def encrypt_json(self, json_data):
        """
        Cifra los datos JSON
        :param json_data: Diccionario con los datos a cifrar
        :return: Datos cifrados en formato base64
        """
        # Convertimos el diccionario a string JSON
        json_str = json.dumps(json_data)
        # Convertimos a bytes
        json_bytes = json_str.encode('utf-8')
        # Ciframos los datos
        encrypted = self.cipher_suite.encrypt(json_bytes)
        # Codificamos en base64 para facilitar el almacenamiento
        return base64.b64encode(encrypted).decode('utf-8')

    def decrypt_json(self, encrypted_data):
        """
        Descifra los datos JSON
        :param encrypted_data: Datos cifrados en base64
        :return: Diccionario con los datos descifrados
        """
        # Decodificamos de base64
        encrypted = base64.b64decode(encrypted_data)
        # Desciframos los datos
        decrypted = self.cipher_suite.decrypt(encrypted)
        # Convertimos de bytes a string
        json_str = decrypted.decode('utf-8')
        # Convertimos el string JSON a diccionario
        return json.loads(json_str)

# Ejemplo de uso
if __name__ == "__main__":
    # Creamos una instancia de la clase
    crypto = JsonCrypto()
    
    # Datos JSON de ejemplo
    productos = [
        { "id": 1, "name": "Zapatillas", "price": 45000 },
        { "id": 2, "name": "Remera", "price": 18000 },
        { "id": 3, "name": "Campera", "price": 75000 }
    ]
    
    # Ciframos los datos
    encrypted = crypto.encrypt_json(productos)
    print("Datos cifrados:", encrypted)
    
    # Desciframos los datos
    decrypted = crypto.decrypt_json(encrypted)
    print("\nDatos descifrados:")
    print(json.dumps(decrypted, indent=4))