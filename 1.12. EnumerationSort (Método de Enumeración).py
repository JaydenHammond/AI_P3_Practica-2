# enumeration_sort: Para cada elemento arr[i], cuenta cuántos son menores y sitúa arr[i] en su posición final
def enumeration_sort(arr):
    n = len(arr)
    sorted_arr = [None] * n
    # Para cada elemento, cuenta cuántos elementos son menores
    for i in range(n):
        count = 0
        for j in range(n):
            if arr[j] < arr[i] or (arr[j] == arr[i] and j < i):
                count += 1
        sorted_arr[count] = arr[i]
    return sorted_arr

# Ejemplo de uso
if __name__ == "__main__":
    lista = [4, 2, 3, 1, 2]
    resultado = enumeration_sort(lista.copy())
    print("EnumerationSort:", resultado)
