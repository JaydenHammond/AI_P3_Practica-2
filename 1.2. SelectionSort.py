# selection_sort: En cada iteración busca el índice del elemento mínimo (desde i hasta n-1) y lo intercambia con la posición i.
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        # Encuentra el mínimo en arr[i..n-1]
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Intercambia el mínimo encontrado con la posición i
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Ejemplo de uso
if __name__ == "__main__":
    lista = [29, 10, 14, 37, 13]
    resultado = selection_sort(lista.copy())
    print("SelectionSort:", resultado)
