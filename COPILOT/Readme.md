Asegúrate de instalar cryptography con pip install cryptography antes de ejecutar el código.

Explicación del código:
- Se genera una clave de cifrado y se almacena en un archivo clave.key para su uso posterior.
- La función cifrar_json lee el archivo productos.json, cifra su contenido y lo guarda en productos_cifrados.json.
- La función descifrar_json recupera la clave almacenada, descifra el archivo productos_cifrados.json y muestra su contenido en formato JSON.

De esta manera, puedes proteger los datos del JSON y recuperarlos cuando lo necesites. ¿Te gustaría hacer alguna mejora o agregar más funciones? 