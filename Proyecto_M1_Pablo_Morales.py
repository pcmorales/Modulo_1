# PROYECTO 1: Calculadora de Indice de Masa Corporal.

# Pedimos al usuario que ingrese su nombre a través del input, y lo almacenamos en la variable llamada nombre.
while True:
    nombre = input("Ingrese su nombre: ")
    # Verificamos si el campo nombre, está vacío.
    if nombre == "":
        print('El campo no puede estar vacío. Por favor, intente nuevamente.') # Mensaje de alerta al usuario, para que ingrese nuevamente la información solicitada.
    # Verificamos si el campo nombre, contiene números.
    elif nombre.isalpha(): # Utilizamos el método "isalpha()", que retorna True si todos los caracteres en la cadena ingresada, son letras.
        break # Se sale del bucle, si cumple con la condición anterior.
    else: # Si no cumple con la condición anterior, se ejecuta el siguiente print con el mensaje de alerta.
        print('El nombre no puede contener números. Por favor, intente nuevamente.') # Mensaje de alerta al usuario, para que ingrese nuevamente la información solicitada.

# Pedimos al usuario que ingrese su apellido paterno a través del input, y lo almacenamos en la variable llamada apell_paterno.
while True:
    apell_paterno = input("Ingrese su apellido paterno: ")
    # Verificamos si el campo apell_paterno, está vacío.
    if apell_paterno == "":
        print('El campo no puede estar vacío. Por favor, intente nuevamente.') # Mensaje de alerta al usuario, para que ingrese nuevamente la información solicitada.
    # Verificamos si el campo apell_paterno, contiene números.
    elif apell_paterno.isalpha(): # Utilizamos el método "isalpha()", que retorna True si todos los caracteres en la cadena ingresada, son letras.
        break # Sale del bucle, si cumple con la condición anterior.
    else: # Si no cumple con la condición anterior, se ejecuta el siguiente print con el mensaje de alerta.
        print('El apellido paterno no puede contener números. Por favor, intente nuevamente.') # Mensaje de alerta al usuario, para que ingrese nuevamente la información solicitada.

# Pedimos al usuario que ingrese su apellido materno a través del input, y lo almacenamos en la variable llamada apell_materno.
while True:
    apell_materno = input("Ingrese su apellido materno: ")
    # Verificamos si el campo apell_materno, está vacío.
    if apell_materno == "":
        print('El campo no puede estar vacío. Por favor, intente nuevamente.') # Mensaje de alerta al usuario, para que ingrese nuevamente la información solicitada.
    # Verificamos si el campo apell_materno, contiene números.
    elif apell_materno.isalpha(): # Utilizamos el método "isalpha()", que retorna True si todos los caracteres en la cadena ingresada, son letras.
        break # Sale del bucle, si cumple con la condición anterior.
    else: # Si no cumple con la condición anterior, se ejecuta el siguiente print con el mensaje de alerta.
        print('El apellido materno no puede contener números. Por favor, intente nuevamente.') # Mensaje de alerta al usuario, para que ingrese nuevamente la información solicitada.

# Pedimos al usuario que ingrese su edad a través del input, y lo almacenamos en la variable llamada edad.
while True:
    try:
        edad = int(input("Ingrese su edad: "))
        if edad > 0: # La edad debe ser mayor a 0.
            break  # Sale del bucle, si la edad es válida.
        else: # Si no cumple con la condición anterior, se ejecuta el siguiente print con el mensaje de alerta.
            print('La edad debe ser un número positivo y mayor que cero. Por favor, intente nuevamente.') # Mensaje de alerta al usuario, para que ingrese nuevamente la información solicitada.
    except ValueError: # Tratamiento de errores.
        print('Debe ingresar un número entero válido. Por favor, intente nuevamente.') # Se evita que aparezca el error tipo ValueError, y se solicita ingresar nuevamente la información solicitada.

# Pedimos al usuario que ingrese su peso a través del input, y lo almacenamos en la variable llamada peso.
while True:
    try:
        peso = int(input("Ingrese su peso: "))
        if peso > 0: # El peso debe ser mayor a 0.
            break  # Sale del bucle, si el peso es válida.
        else: # Si no cumple con la condición anterior, se ejecuta el siguiente print con el mensaje de alerta.
            print('El peso debe ser un número entero y mayor que cero. Por favor, intente nuevamente.') # Mensaje de alerta al usuario, para que ingrese nuevamente la información solicitada.
    except ValueError: # Tratamiento de errores.
        print('Debe ingresar un número entero válido. Por favor, intente nuevamente.') # Se evita que aparezca el error tipo ValueError, y se solicita ingresar nuevamente la información solicitada.

# Pedimos al usuario que ingrese su estatura a través del input, y lo almacenamos en la variable llamada estatura.
while True:
    try:
        estatura = float(input("Ingrese su estatura (ejemplo 1.65): "))
        if estatura > 0:  # La estatura debe ser mayor a 0.
            break  # Sale del bucle si la estatura es válida.
        else: # Si no cumple con la condición anterior, se ejecuta el siguiente print con el mensaje de alerta.
            print('La estatura debe ser un número positivo y mayor que cero. Por favor, intente nuevamente.') # Se evita que aparezca el error tipo ValueError, y se solicita ingresar nuevamente la información solicitada.
    except ValueError:  # Tratamiento de errores.
        print('Debe ingresar un número válido. Por favor, intente nuevamente.') # Se evita que aparezca el error tipo ValueError, y se solicita ingresar nuevamente la información solicitada.

print('') # Salto de línea.

# Se imprime la información del usuario.
print(f"Su nombre es: {nombre}") # Se imprime el nombre del usuario.
print(f"Su apellido paterno es: {apell_paterno}") # Se imprime el apellido paterno del usuario.
print(f"Su apellido materno es: {apell_materno}") # Se imprime el apellido materno del usuario.
print(f"Su edad es: {edad}") # Se imprime la edad del usuario.
print(f"Su peso es: {peso}") # Se imprime el peso del usuario.
print(f"Su estatura es: {estatura}") # Se imprime la estatura del usuario.

print('') # Salto de línea.

# Se efectúa el cálculo del Indice de Masa Corporal (IMC) al usuario.
# Se crea una variable que se llama imc, donde almacenaremos el resultado del cálculo del IMC que es el peso (kg) dividido por la estatura al cuadrado.
imc = round(peso / (estatura ** 2),2)
print(f"Su indice de masa corporal es: {imc}") # Se imprime el IMC del usuario.