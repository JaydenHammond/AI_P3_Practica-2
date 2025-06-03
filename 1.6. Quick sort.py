# quick_sort y función auxiliar partition: divide el arreglo y ordena recursivamente subarreglos de menor y mayor que el pivote.
def partition(arr, low, high):
    pivot = arr[high]     # Elegimos el último elemento como pivote
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    # Coloca al pivote en su posición final
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort_rec(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort_rec(arr, low, pi - 1)
        quick_sort_rec(arr, pi + 1, high)

def quick_sort(arr):
    quick_sort_rec(arr, 0, len(arr) - 1)
    return arr

# Ejemplo de uso
if __name__ == "__main__":
    lista = [10, 7, 8, 9, 1, 5]
    resultado = quick_sort(lista.copy())
    print("QuickSort:", resultado)
