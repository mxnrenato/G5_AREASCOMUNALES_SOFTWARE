import hashlib

# Crea un diccionario para almacenar los usuarios y sus contraseñas encriptadas
users = {'email1@example.com': '8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918',
         'email2@example.com': '8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918'}

def authenticate(email, password):
    # Encriptar la contraseña ingresada
    password = hashlib.sha256(password.encode()).hexdigest()
    # Verificar si el email y la contraseña encriptada están en el diccionario de usuarios
    if email in users and users[email] == password:
        return True
    else:
        return False

email = input("Email: ")
password = input("Password: ")

if authenticate(email, password):
    #Ingresa al sistema
    pass
else:
    print("Please enter the correct email and password for a staff account. Note that both fields may be case-sensitive.")