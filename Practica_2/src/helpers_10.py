def agregar_participante(tabla_posiciones, participante):
    """ 
     La función recibe un diccionario que representa una tabla de participantes y un nombre de participante.
     Si el nombre de participante no se encuentra en el diccionario, lo agrega como un nuevo diccionario, detallando su puntaje, rondas ganadas, mejor ronda y promedio de puntos.
    """
    if participante not in tabla_posiciones:
        tabla_posiciones[participante] = {
            'Puntaje' : 0,
            'Rondas ganadas' : 0,
            'Mejor ronda' : 0,
            'Promedio' : 0,
        }
    return tabla_posiciones


def obtener_puntaje_individual(puntajes_individuales):
    """ 
    La función recibe un diccionario que representa una serie de puntajes otorgados por los jueces y devuelve la suma de esos puntajes correspondientes a un participante.
    """
    puntaje_total = 0
    for item in puntajes_individuales.keys():
        puntaje_total += puntajes_individuales[item]
    return puntaje_total


def actualizar_ganador(participante,puntaje,ganador_nombre,ganador_puntos):
    """ 
    La función recibe un participante, su puntaje, el nombre del ganador actual y su puntaje. Si el participante tiene mejor puntaje, se actualiza y se devuelve el ganador y sus datos.
    """
    if puntaje > ganador_puntos:
        ganador_puntos = puntaje
        ganador_nombre = participante
    return ganador_nombre,ganador_puntos


def actualizar_puntaje_mejor_ronda_promedio(tabla_posiciones, ronda, ronda_numero):
    """ 
    La función recibe un diccionario que representa una tabla de posiciones, un diccionario que representa una ronda del juego, con su título y los resultados de cada participante, y además, el número de la ronda a jugarse.
    Se recorren los resultados de la ronda de cada jugador y:
    
    -Si el participante no existe en la tabla, lo agrega.
    -Se calcula el puntaje obtenido por el participante en la ronda y se agrega a la tabla de posiciones.
    -Se actualiza quien es el ganador de la ronda.
    -Se actualiza el puntaje de la mejor ronda obtenido por el participante.
    -Se actualiza el puntaje promedio del participante.

    La función devuelve la tabla de posiciones actualizada, el nombre del ganador y los puntos que obtuvo.
    """
    ganador_puntos = -9999
    ganador_nombre = ''   
    for item in ronda['scores']:
        ### Agrega el participante al diccionario, si no existe
        tabla_posiciones = agregar_participante(tabla_posiciones,item)
        
        ### Calcula el puntaje obtenido en la ronda y lo agrega a la tabla
        puntaje_individual = obtener_puntaje_individual(ronda['scores'][item])
        tabla_posiciones[item]['Puntaje'] += puntaje_individual

        ### Actualiza quién es el ganador de la ronda
        ganador_nombre, ganador_puntos = actualizar_ganador(item,puntaje_individual,ganador_nombre,ganador_puntos)
        
        ### Actualiza el puntaje de la mejor ronda        
        if tabla_posiciones[item]['Mejor ronda'] < puntaje_individual:
            tabla_posiciones[item]['Mejor ronda'] = puntaje_individual

        ### Actualiza el puntaje promedio
        tabla_posiciones[item]['Promedio'] = tabla_posiciones[item]['Puntaje'] / ronda_numero
    return tabla_posiciones, ganador_nombre, ganador_puntos


def actualizar_rondas_ganadas(tabla_posiciones,ganador_nombre):
    """ 
    La función recibe un diccionario que representa la tabla de posiciones y el nombre del ganador de la ronda. Con estos datos, incrementa en 1 la cantidad de rondas ganadas para el participante ganador. 
    """
    for item in tabla_posiciones:
        if item == ganador_nombre:
            tabla_posiciones[item]['Rondas ganadas'] += 1


def actualizar_tabla(tabla_posiciones, ronda, ronda_numero):
    """ 
    La función recibe un diccionario que representa la tabla de posiciones, un diccionario que representa la información de la ronda y el número de la misma. Utiliza las funciones de actualizar_puntaje_mejor_ronda_promedio y actualizar_rondas_ganadas para procesar la información, y devuelve la tabla de posiciones actualizada, el nombre del ganador y su puntaje.
    """
    tabla_posiciones, ganador_nombre, ganador_puntos = actualizar_puntaje_mejor_ronda_promedio(tabla_posiciones, ronda, ronda_numero)
    actualizar_rondas_ganadas(tabla_posiciones,ganador_nombre)
    return tabla_posiciones, ganador_nombre, ganador_puntos
        

def imprimir_tabla(tabla_posiciones, ronda_numero):
    """ 
    La función recibe un dicionario que representa la tabla de posiciones y el número de ronda, e imprime la información con formato tabla.
    """
    if ronda_numero == 5:
        print('Tabla de posiciones final:')
    else:
        print('Tabla de posiciones:')
    print(f"{'Cocinero':<10} {'Puntaje':<8} {'Rondas ganadas':<15} {'Mejor ronda':<15} {'Promedio':<10}")
    print("-" * 65)
    for item in sorted(tabla_posiciones, key=lambda x: tabla_posiciones[x]['Puntaje'], reverse=True):
        print(f"{item:<10} {tabla_posiciones[item]['Puntaje']:<8} {tabla_posiciones[item]['Rondas ganadas']:<15} {tabla_posiciones[item]['Mejor ronda']:<15} {tabla_posiciones[item]['Promedio']:<10.2f}")
    print()


def procesar_datos(datos):
    """ 
    La función recibe un diccionario que representa el conjunto de datos de la competencia y lo procesa, imprimiendo las posiciones al cierre de cada ronda y las posiciones finales.
    """
    tabla = {}
    for i, ronda in enumerate(datos):
        ronda_numero = i+1
        tabla,ganador,puntos  = actualizar_tabla(tabla, ronda, ronda_numero)
        print(f'Ronda {ronda_numero} - {ronda['theme']}')
        print(f'  Ganador: {ganador} ({puntos}pts)')
        imprimir_tabla(tabla,ronda_numero)