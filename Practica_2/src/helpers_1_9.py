import random

def ejercicio_1_contador(text):
    """
    Esta función recibe un texto y devuelve la cantidad de líneas, la cantidad de palabras y el promedio de palabras por línea.
    """

    cantidad_lineas = text.count(".") + text.count('!')
    

    edited_text = text.replace('\n', ' ')
    edited_text = edited_text.split()
    cantidad_palabras = len(edited_text)
    palabras_por_linea = round(cantidad_palabras/cantidad_lineas,2)

    return cantidad_lineas, cantidad_palabras, palabras_por_linea


def ejercicio_1_encima_promedio(text,palabras_por_linea):
    """ 
    Esta función recibe un texto y una cantidad promedio de palabras por línea y devuelve un detalle con la cantidad de líneas por encima del promedio y las lista.
    """
    lineas = text.split('\n')
    print(f'Líneas por encima del promedio ({palabras_por_linea} palabras):')
    for linea in lineas:
        palabras_en_linea = linea.split(" ")
        palabras = len(palabras_en_linea)
        if len(palabras_en_linea) > palabras_por_linea:
            print("-",linea,f"({palabras} palabras)")


def ejercicio_2(playlist):
    """
    Esta función recibe un diccionario de pares canción-duración, donde la duración esta expresada como un string 'mm:ss'.
    A partir de los datos, la función devuelve la duración total de la playlist en minutos y segundos, y devuelve los datos de la canción más corta y la canción más larga.
    """
    
    duracion_maxima = -9999
    linea_max = -1
    duracion_minima = 9999
    linea_min = -1
    duracion_total_segundos = 0

    for item in range(len(playlist)):
        duracion = playlist[item]["duration"]
        duracion = duracion.split(":")
        duracion_segundos = int(duracion[0])*60 + int(duracion[1])
        if duracion_segundos > duracion_maxima:
            duracion_maxima = duracion_segundos
            linea_max = item
        if duracion_segundos < duracion_minima:
            duracion_minima = duracion_segundos
            linea_min = item
        duracion_total_segundos += duracion_segundos

    duracion_total_minutos = duracion_total_segundos // 60
    duracion_total_segundos_final = duracion_total_segundos % 60

    duracion_total = f'Duración total: {duracion_total_minutos}m {duracion_total_segundos_final}s'

    return duracion_total, linea_max, linea_min


def ejercicio_3(review):
    """
    Esta función recibe como entrada la review de una película. Se le solicita al usuario que ingrese una lista de palabras clave separadas por coma. La función devuelve la review con reemplazando cada letra de cada palabra clave por '*'.
    """
    
    palabras_spoiler = input("Ingrese las palabras spoiler (separadas por coma):")
    palabras_spoiler = palabras_spoiler.replace(',','').split()
    palabras_spoiler = [x.lower() for x in palabras_spoiler]
    
    palabras_review = review.replace('\n', ' ').split(' ')
    
    resultado = []

    for palabra in palabras_review:
        palabra_minusc = palabra.lower()
        if palabra_minusc in palabras_spoiler:
            resultado.append('*' * len(palabra))
        else:
            resultado.append(palabra)
    
    
    separador = ' '
    review_sin_spoilers = separador.join(resultado)

    return review_sin_spoilers


def ejercicio_4():
    """
    La función solicita al usuario que ingrese un mail por teclado y comprueba que cumpla con una serie de condiciones:
    1) El mail continene exactamente un solo '@'.
    2) El mail tiene al menos un caracter antes del '@'.
    3) El mail tiene al menos un '.' después del '@'.
    4) El mail no empieza ni termina con '@' ni con '.'.
    5) La parte después del último '.' tiene al menos dos caracteres (el dominio).
    """

    mail = input('Ingrese un email:')
    cond_1 = False
    cond_2 = False
    cond_3 = False
    cond_4 = False
    cond_5 = False

    if mail[0] in ["@", "."] or mail[-1] in ["@", "."]:
        cond_4 = True
    entrada = mail.split("@")
    if len(entrada) != 2:
        cond_1 = True
    elif len(entrada[0]) == 0:
        cond_2 = True
    elif len(entrada[1].split(".")) == 1:
        cond_3 = True
    elif len(entrada[1].split(".")[-1]) < 2:
        cond_5 = True

    if cond_1 or cond_2 or cond_3 or cond_4 or cond_5:
        return print('El mail no es válido.')
    else:
        return print('El mail es válido.')
    

def ejercicio_5():
    """
    La función solicita al usuario que ingrese un peso en kilos y la zona de destino, y automaticamente calcula e imprime el costo total de realizar el envio solicitado.
    """
    costo = {
        'local' : [500, 1000, 2000],
        'regional' : [1000, 2500, 5000],
        'nacional' : [2000, 4500, 8000]
    }

    peso = float(input('Ingrese el peso del paquete (kg):'))

    if peso <= 1:
        parametro_1 = 0
    elif peso <=5:
        parametro_1 = 1
    else:
        parametro_1 = 2

    parametro_2 = input('Ingrese la zona del destino (local/regional/nacional):').lower()
    while parametro_2 not in list(costo.keys()):
        print('Zona no válida. Las zonas disponibles son: local, regional, nacional.')
        parametro_2 = input('Ingrese la zona:').lower()

    return f'El precio a pagar por el paquete es: ${costo[parametro_2][parametro_1]}'


def ejercicio_6(posts):
    """ 
    La función recibe una lista de posts en redes sociales y extrae la cantidad de hashtags que contiene. Con los datos recopilados genera una ranking en orden descendente por cantidad de apariciones. 
    """
    hashtags = []

    for post in posts:
        entrada = post.split(' ')
        for palabra in entrada:
            if palabra[0] == "#":
                hashtags.append(palabra)

    conteo = {}

    for elemento in hashtags:
        if elemento not in conteo:
            conteo[elemento] = 1
        else:
            conteo[elemento] += 1

    ranking = sorted(conteo.items(), key = lambda x: x[1], reverse = True)
    return ranking


def ejercicio_7_menos_de_tres(lista_de_participantes):
    """
    FUNCIÓN A UTILIZARSE DENTRO DEL CONTEXTO DEL EJERCICIO #7
    ESta función recibe una lista de participantes y verifica si cuenta con tres miembros o más.
    """
    if len(lista_de_participantes) < 3:
        return True
    else:
         return False


def ejercicio_7_se_repite(lista_de_participantes):
    """
    FUNCIÓN A UTILIZARSE DENTRO DEL CONTEXTO DEL EJERCICIO #7
    Esta función recibe una lista de participantes y verifica que no haya al menos un nombre repetido.
    """
    repetido = False
    for nombre in lista_de_participantes:
        if lista_de_participantes.count(nombre) > 1:
            repetido = True
    return repetido


def ejercicio_7_sortea_pares(lista_de_participantes):
    """
    FUNCIÓN A UTILIZARSE DENTRO DEL CONTEXTO DEL EJERCICIO #7
    Esta funcion recibe una lista de participantes con tres miembros o más y sin nombres repetidos, y sortea los pares origen-destino de cada regalo.    
    """
    recibe_regalo = lista_de_participantes.copy()
    for participante in lista_de_participantes:
        participante_1 = participante
        participante_2 = random.choice(recibe_regalo)
        while participante_1 == participante_2:
            participante_2 = random.choice(recibe_regalo)
        recibe_regalo.remove(participante_2) 
        print('    ',participante_1,' → ',participante_2)


def ejercicio_7():
    """
    Esta función solicita que se ingrese una lista de participantes separados por coma, controla que haya tres miembros o más y que no haya nombres repetidos y realiza el sorteo de los pares origen-destino de cada regalo.
    """
    lista = input('Ingrese una lista de participantes separados por coma.').lower()
    participantes = lista.replace(',',' ').split()

    while ejercicio_7_menos_de_tres(participantes) or ejercicio_7_se_repite(participantes):
        print('La cantidad de participantes debe ser como mínimo 3.')
        print('Los nombres no se pueden repetir.')
        lista = input('Ingrese una lista de participantes separados por coma.').lower()
        participantes = lista.split(', ')
        
    print('Sorteo de amigo invisible:')
    ejercicio_7_sortea_pares(participantes)


def ejercicio_8():
    """
    Esta función solicita que se ingrese un mensaje por teclado y una cantidad de caracteres a desplazarse. Con los dos datos imprime el mensaje cifrado (corriendo los caracteres n cantidad de veces) y el mensaje original.
    """
    mensaje = input('Ingrese un mensaje:')
    posiciones = int(input('Ingrese el desplazamiento:'))

    mensaje_cifrado = ''

    for caracter in mensaje:
        if caracter.isalpha():
            inicio = ord('A') if caracter.isupper() else ord('a')
            caracter_nuevo = chr((ord(caracter) - inicio + posiciones) % 26 + inicio)
            mensaje_cifrado += caracter_nuevo
        else:
            mensaje_cifrado += caracter

    print(f'Mensaje cifrado: {mensaje_cifrado}')
    print(f'Mensaje descifrado: {mensaje}')


def ejercicio_9_limpiar_lista(lista_estudiantes):
    """
    FUNCIÓN A UTILIZARSE DENTRO DEL CONTEXTO DEL EJERCICIO #9
    Esta función recibe una lista de estudiantes, definida como una lista de diccionarios compuestos por un nombre, un grado y un status, y la limpia eliminando vacíos, espacios de sobra y valores de nota que no sean numéricos.
    """
    lista_limpia = []
    
    for item in range(len(lista_estudiantes)):
        if (lista_estudiantes[item]['name'] != None and lista_estudiantes[item]['' \
        'name'] != ' ' and not lista_estudiantes[item]['name'].isspace()) and lista_estudiantes[item]['grade'] in ['1','2','3','4','5','6','7','8','9','10']:
            lista_limpia.append(lista_estudiantes[item])

    for item in range(len(lista_limpia)):
        lista_limpia[item]['name'] = lista_limpia[item]['name'].strip().title()
        lista_limpia[item]['status'] = lista_limpia[item]['status'].strip().title()
        
    return lista_limpia


def ejercicio_9_ordenar_lista_por_nombre_nota(lista_estudiantes):
    """
    FUNCIÓN A UTILIZARSE DENTRO DEL CONTEXTO DEL EJERCICIO #9
    Esta función ordena la lista de estudiantes, previamente limpia, en orden descendente por nombre y grado.
    """
    return sorted(lista_estudiantes, key=lambda x: (x['name'], x['grade']), reverse=True)


def ejercicio_9_eliminar_duplicados(lista_estudiantes):
    """
    FUNCIÓN A UTILIZARSE DENTRO DEL CONTEXTO DEL EJERCICIO #9
    Esta función elimina filas con nombres duplicados de una lista previamente ordenada por grado en orden descendente.
    """
    lista_final = []
    nombres = []

    for item in range(len(lista_estudiantes)):
        if lista_estudiantes[item]['name'] not in nombres:
            nombres.append(lista_estudiantes[item]['name'])
            lista_final.append(lista_estudiantes[item])

    return lista_final


def ejercicio_9_ordenar_lista_por_nombre(lista_estudiantes):
    """
    FUNCIÓN A UTILIZARSE DENTRO DEL CONTEXTO DEL EJERCICIO #9
    Esta función ordena una lista sin duplicados en base al nombre, en forma ascendente.
    """
    return sorted(lista_estudiantes, key=lambda x: x['name'])


def ejercicio_9_imprimir_lista(lista_estudiantes):
    """
    FUNCIÓN A UTILIZARSE DENTRO DEL CONTEXTO DEL EJERCICIO #9
    Esta función imprime una lista de alumnos previamente limpia y ordenada en formato tabla.
    """
    print('Registros limpios de alumnos:')
    print(f"{'Nombre':<15} {'Nota':<5} {'Estado':<15}")
    print("-" * 35)
    for item in lista_estudiantes:
        print(f"{item['name']:<15} {item['grade']:<5} {item['status']:<15}")


def ejercicio_9(lista):
    """
    FUNCIÓN A UTILIZARSE DENTRO DEL CONTEXTO DEL EJERCICIO #9
    Esta función recibe una lista de alumnos a ser limpiada, la limpia, elimina duplicados, la ordena de manera ascendente por el nombre y la imprime en formato tabla.
    """
    lista_limpia = ejercicio_9_limpiar_lista(lista)
    lista_ordenada = ejercicio_9_ordenar_lista_por_nombre_nota(lista_limpia)
    lista_sin_duplicados = ejercicio_9_eliminar_duplicados(lista_ordenada)
    lista_sin_duplicados_ordenada = ejercicio_9_ordenar_lista_por_nombre(lista_sin_duplicados)
    ejercicio_9_imprimir_lista(lista_sin_duplicados_ordenada)