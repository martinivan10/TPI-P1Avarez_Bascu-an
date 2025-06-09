def insercion(lista):
    lista = lista.copy()  # Copia para no modificar la original
    for i in range(1, len(lista)):
        insertar = lista[i]
        anterior = i - 1
        while anterior >= 0 and lista[anterior] > insertar:
            lista[anterior + 1] = lista[anterior]
            anterior -= 1
        lista[anterior + 1] = insertar
    return lista

# Este código implementa el algoritmo de ordenamiento por inserción.
if __name__ == "__main__":
    lista = [5, 2, 9, 1, 7, 6]
    print("Lista original:", lista)
    lista_ordenada = insercion(lista)
    print("Lista ordenada:", lista_ordenada)
