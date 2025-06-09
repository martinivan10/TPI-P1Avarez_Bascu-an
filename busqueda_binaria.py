import random

def generar_inventario():
# Crear una lista de 1000 códigos únicos ordenados (simulando el inventario)
    return sorted(random.sample(range(1000, 2000), 1000))

def busqueda_binaria(inventario, codigo):
# Función de búsqueda binaria 
    izquierda, derecha = 0, len(inventario) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if inventario[medio] == codigo:
            return medio  # Código encontrado
        elif inventario[medio] < codigo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1  # Código no encontrado

# Generar inventario de prueba
inventario = generar_inventario()

# Mostrar parte del inventario
print("Inventario generado (primeros 20 códigos):", inventario[:20])
print("Total de códigos en el inventario:", len(inventario))

# Solicitar al usuario el código a buscar
try:
    codigo_buscado = int(input("Ingrese el código de producto a buscar: "))
    
    # Ejecutar búsqueda binaria
    resultado = busqueda_binaria(inventario, codigo_buscado)
    
    # Mostrar resultados
    print("Código buscado:", codigo_buscado)
    if resultado != -1:
        print(f"El código {codigo_buscado} se encuentra en la posición {resultado} del inventario.")
    else:
        print(f"El código {codigo_buscado} no se encuentra en el inventario.")
except ValueError:
    print("Por favor, ingrese un número entero válido.")
