import random

words = {
        "Programación" : ["python","programa","variable","funcion","bucle","cadena","entero","lista"],
        "Comida" : ["banana", "manzana", "hamburguesa", "milanesa", "pure", "helado", "chocolate", "medialuna"],
        "Deportes" : ["futbol", "pelota", "offside", "rugby", "basket", "referi", "jugador", "reglamento"],
        "Entretenimiento" : ["netflix", "friends", "seinfeld", "pelicula", "miniserie", "comedia", "streaming", "videojuego"]
    }

sigue_jugando = "y"
while sigue_jugando == "y":
    
    guessed = []

    attempts = 6
    score = 0

    print("¡Bienvenido al Ahorcado!")
    print()
    print("Seleccione una de las siguientes categorías")
    print("Programación")
    print("Comida")
    print("Deportes")
    print("Entretenimiento")
    categoria = input("Su elección:")

    while categoria not in words.keys():
        print('Categoría incorrecta. Ingrese de nuevo.')
        categoria = input("Su elección:")

    word = random.sample(words[categoria],1)[0]
    words[categoria].remove(word)

    while attempts > 0:
        # Mostrar progreso: letras adivinadas y guiones para las que faltan
        progress = ""
        for letter in word:
            if letter in guessed:
                progress += letter + " "
            else:
                progress += "_ "
        print(progress)

        # Verificar si el jugador ya adivinó la palabra completa
        if "_" not in progress:
            print("¡Ganaste!")
            score += 6
            break

        print(f"Intentos restantes: {attempts}")
        print(f"Letras usadas: {', '.join(guessed)}")

        letter = input("Ingresá una letra: ")

        if letter in guessed:
            print("Ya usaste esa letra.")
        elif letter.lower() < 'a' or letter.lower() > 'z' or len(letter) > 1:
            print('Entrada no válida')
        elif letter in word:
            guessed.append(letter)
            print("¡Bien! Esa letra está en la palabra.")
        else:
            guessed.append(letter)
            attempts -= 1
            score -= 1
            print("Esa letra no está en la palabra.")

        print()

    else:
        print(f"¡Perdiste! La palabra era: {word}")
        score = 0

    print(f"Score final: {score}")
    
    sigue_jugando = input('Desea seguir jugando? (y/n)').lower()
    print()
