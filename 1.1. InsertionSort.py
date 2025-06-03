# insertion_sort: Recorre el arreglo y para cada posición i inserta el
# elemento actuales en la subsecuencia anterior (ya ordenada).
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]               # Elemento a insertar
        j = i - 1
        # Desplaza los mayores a la derecha para hacer espacio
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key           # Inserta en la posición correcta
    return arr

# Ejemplo de uso
if __name__ == "__main__":
    lista = [5, 2, 9, 1, 5, 6]
    resultado = insertion_sort(lista.copy())
    print("InsertionSort:", resultado)
