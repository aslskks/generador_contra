import random
import string

def generate_password(length):
    # Define los caracteres posibles que se pueden usar en la contraseña
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Genera la contraseña aleatoria
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

# Pide al usuario que ingrese la longitud de la contraseña deseada
while True:
    length = int(input("Ingresa la longitud de la contraseña que deseas generar: "))
    password = generate_password(length)
    print("Tu nueva contraseña es:", password)
    
    # Pregunta al usuario si desea generar otra contraseña
    choice = input("¿Deseas generar otra contraseña? (s/n): ")
    if choice.lower() == 'n':
        break
