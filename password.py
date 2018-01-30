#!/usr/bin/python3
fichero = open('/etc/passwd', 'r')
lineas = fichero.readlines()
diccionario = {}

interesantes = ['root', 'imaginario', 'sys', 'var']

for linea in lineas:
    datos = linea[:-1].split(':')
    usuario, shell = datos[0], datos[-1]
    diccionario[usuario] = shell

for username in interesantes:
    try:
        print(username, '--->', diccionario[username])
    except KeyError:
        print(username, "no existe")

fichero.close()
