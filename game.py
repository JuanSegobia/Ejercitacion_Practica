import random

# Lista de palabras posibles
words = ["python", "programación", "computadora", "código", "desarrollo", "inteligencia"]

# Elegir una palabra al azar
secret_word = random.choice(words)

# Número máximo de intentos permitidos
max_attempts = 10

# Intento actual
attempt = 0

# Lista para almacenar las letras adivinadas
guessed_letters = []

# Lista de vocales
vowels = ['a', 'e', 'i', 'o', 'u']

print("¡Bienvenido al juego de adivinanzas!")
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")

# Seleccion de dificultad
print("Selecciona el nivel de dificultad: ")
print("1 - Fácil")
print("2 - Medio")
print("3 - Difícil")
level = int (input("Ingrese el número correspondiente al nivel: "))

# Seleccion de nivel 1 (Si elijo este nivel, me muevo por la secret word, y de ser vocal la muestra. Sino "_"

if level == 1:
    word_displayed = ""
    for letter in secret_word:
        if letter in vowels:
            guessed_letters.append(letter)
            word_displayed += letter
        else:
            word_displayed += "_"

# Mostrar la palabra parcialmente adivinada
    print(f"Palabra: {word_displayed}")

while attempt < max_attempts:
    # Pedir al jugador que ingrese una letra
    letter = input("Ingresa una letra: ").lower()

    # Verificar si el caracter ingresado es vacio
    if letter == "":
        print("Error. No has ingresado nada")
        continue

    # Verificar si la letra ya ha sido adivinada
    if letter in guessed_letters:
        print("Ya has intentado con esa letra. Intenta con otra.")
        continue

    # Incrementar el attempt
    attempt += 1

    # Agregar la letra a la lista de letras adivinadas
    guessed_letters.append(letter)

    # Verificar si la letra está en la palabra secreta
    if letter in secret_word:
        print("¡Bien hecho! La letra está en la palabra.")
    else:
        print("Lo siento, la letra no está en la palabra.")

    # Mostrar la palabra parcialmente adivinada
    letters = []
    for letter in secret_word:
        if letter in guessed_letters:
            letters.append(letter)
        else:
            letters.append("_")
    word_displayed = "".join(letters)
    print(f"Palabra: {word_displayed}")

    # Verificar si se ha adivinado la palabra completa
    if word_displayed == secret_word:
        print(f"¡Felicidades! Has adivinado la palabra secreta: {secret_word}")
        break
else:
    print(f"¡Oh no! Has agotado tus {max_attempts} intentos.")
    print(f"La palabra secreta era: {secret_word}")
