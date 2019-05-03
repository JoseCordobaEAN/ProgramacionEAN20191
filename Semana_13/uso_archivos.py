import json

# este es el diccionario que vamos a guardar
diccionario_de_pruebas = {
    'hola': 'mundo',
    'jose': 'cordoba',
    'programacion': 'ean'
}


def guardar(nombre_archivo, diccionario_a_guardar):
    """
    (str, dict) -> Boolean

    Guarda en el archivo mencionado el diccionario


    :param nombre_archivo: str el nombre del archivo a guardar
    :param diccionario_a_guardar: el diccionario a guardar
    :return: True si se logró guardar el diccionario false de lo contrario
    """
    try:
        #Abrimos nuestro archivo
        archivo = open(nombre_archivo, "w")

        # Convertimos nuestro diccionario en un json
        convertido = json.dumps(diccionario_a_guardar)

        # Guardamos el archivo
        archivo.write(convertido)

        # Cerramos el archivo
        archivo.close()

        # Retornamos exito en la operacion
        return True
    except:

        # Si ocurrió un error retornamos falso
        return False


def leer(nombre_archivo):
    """
    (str) -> dict

    Lee un diccionario dado un archivo

    :param nombre_archivo: str el nombre del archivo
    :return: dict contenido en el archivo o un diccionario vacío si no existe nada
    """

    try:
        # Abrimos nuestro archivo en modo lectura
        archivo = open(nombre_archivo, 'r')

        # Convertimos el json a diccionario
        diccionario_leido = json.load(archivo)

        # Cerramos nuestro archivo
        archivo.close()

        # Retornamos el archivo
        return diccionario_leido
    except:
        return {}


if __name__ == '__main__':
    nombre_archivo = 'prueba.json'
    leido = leer(nombre_archivo)

    print(leido)

    print(guardar(nombre_archivo, diccionario_de_pruebas))

