# heapify: Asegura que el subárbol con raíz en i (y tamaño heap_size) cumpla la propiedad de max-heap
def heapify(arr, heap_size, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    # Compara con hijo izquierdo
    if left < heap_size and arr[left] > arr[largest]:
        largest = left
    # Compara con hijo derecho
    if right < heap_size and arr[right] > arr[largest]:
        largest = right
    # Si no es el nodo mayor, intercambia y continúa heapificando
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, heap_size, largest)

# heap_sort: Crea un max-heap y luego extrae el máximo repetidamente
def heap_sort(arr):
    n = len(arr)
    # Construye max-heap invirtiendo desde el último nodo interno hasta la raíz
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    # Extrae elementos uno a uno
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Mueve raíz al final
        heapify(arr, i, 0)              # Reconstruye heap con tamaño reducido
    return arr

# Ejemplo de uso
if __name__ == "__main__":
    lista = [12, 11, 13, 5, 6, 7]
    resultado = heap_sort(lista.copy())
    print("HeapSort:", resultado)
