# bubble_sort: Recorre repetidamente el arreglo, intercambiando elementos adyacentes si están fuera de orden.
def bubble_sort(arr):
    n = len(arr)
    # Repetir hasta que no haya intercambios
    for i in range(n):
        swapped = False
        for j in range(0, n - 1 - i):
            if arr[j] > arr[j + 1]:
                # Intercambia arr[j] y arr[j+1]
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            # Si en una pasada no hubo intercambios, ya está ordenado
            break
    return arr

# Ejemplo de uso
if __name__ == "__main__":
    lista = [64, 34, 25, 12, 22, 11, 90]
    resultado = bubble_sort(lista.copy())
    print("BubbleSort:", resultado)
