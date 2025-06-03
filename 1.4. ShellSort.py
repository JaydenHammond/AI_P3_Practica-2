# shell_sort: Utiliza una secuencia de brechas (gaps) para realizar inserciones parciales y luego reduce el gap hasta 1
def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    # Mientras gap > 0, aplicar inserción con paso "gap"
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            # Inserta arr[i] en la subsecuencia arr[i-gap, i-2*gap, ...]
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr

# Ejemplo de uso
if __name__ == "__main__":
    lista = [12, 34, 54, 2, 3]
    resultado = shell_sort(lista.copy())
    print("ShellSort:", resultado)
