import json
# Crear un diccionario vacío para almacenar los usuarios y contraseñas
DB = {}
archivo_json = "usuarios.json"

def load_data():
    try:
        with open(archivo_json, 'r') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {}

# Guardar datos en el archivo JSON
def save_data(datos):
    with open(archivo_json, 'w') as archivo:
        json.dump(datos, archivo)

DB = load_data()

# Función para obtener todos la data
def get_all_users():
    return load_data()

def register_user():
    name_user = input("Ingrese el nombre de usuario: ")
    password = input("Ingrese la contraseña: ")

    #Verificar si el nombre de usuario ya existe
    if name_user in DB:
        print("El nombre de usuario ya esta en uso. Por favor, elija otro. ")
    else:
        # Almacenar el nombre de usuario y contraseña en el diccionario
        DB[name_user] = password
        save_data(DB)
        print("Usuario registrado exitosamente.")

def login():
    name_user = input("Ingrese el nombre de usuario: ")
    
    # Verificar si el usuario existe
    if name_user in DB:
        password = input("Ingrese la contraseña: ")
        
        # Verificar si la contraseña es correcta
        if DB[name_user] == password:
            print("Inicio de sesión exitoso.")
        else:
            print("Contraseña incorrecta.")
    else:
        print("Nombre de usuario no encontrado.")


def main():
    while True:
        print("\n--- Menú ---")
        print("1. Registrar usuario")
        print("2. Iniciar sesión")
        print("3. Obtener todos los datos")
        print("4. Guardar archivo")
        print("5. Salir")
        
        opcion = input("Seleccione una opción (1/2/3/4/5): ")

        if opcion == '1':
            register_user()
        elif opcion == '2':
            login()
        elif opcion == '3':
            get_all_users = load_data()
            print("Usuarios registrados:")
            for user, password in get_all_users.items():
                print(f"Nombre de usuario: {user} Contraseña: {password}")
        elif opcion == '4':
            save_data(DB)
            print("Datos guardados en el archivo JSON.")
        elif opcion == '5':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()