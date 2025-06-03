# binary_search: Busca la posición de inserción de key en arr[0..high-1], suponiendo que arr está ordenado
def binary_search(arr, key, low, high):
    while low < high:
        mid = (low + high) // 2
        if arr[mid] <= key:
            low = mid + 1
        else:
            high = mid
    return low

# binary_insertion_sort: En lugar de búsqueda lineal, usa binary_search para ubicar la posición de key
def binary_insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        # Encuentra el índice donde insertar key
        pos = binary_search(arr, key, 0, i)
        # Desplaza elementos para abrir espacio
        j = i
        while j > pos:
            arr[j] = arr[j - 1]
            j -= 1
        arr[pos] = key
    return arr

# Ejemplo de uso
if __name__ == "__main__":
    lista = [37, 23, 0, 17, 12, 72, 31]
    resultado = binary_insertion_sort(lista.copy())
    print("BinaryInsertionSort:", resultado)
