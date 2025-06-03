# counting_sort_por_digito: Ordena arr en base al exponente (1: unidades, 10: decenas, etc.)
def counting_sort_por_digito(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    # Cuenta ocurrencias del dígito (arr[i] // exp) % 10
    for num in arr:
        index = (num // exp) % 10
        count[index] += 1
    # Convierte en posiciones acumuladas
    for i in range(1, 10):
        count[i] += count[i - 1]
    # Construye el arreglo ordenado parcial (recorriendo de derecha a izquierda para conservar estabilidad)
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
    return output

# radix_sort: Repite counting sort para cada posición de dígito
def radix_sort(arr):
    if not arr:
        return arr
    max_num = max(arr)
    exp = 1
    result = arr.copy()
    # Procesa cada dígito hasta alcanzar el dígito más significativo
    while max_num // exp > 0:
        result = counting_sort_por_digito(result, exp)
        exp *= 10
    return result

# Ejemplo de uso
if __name__ == "__main__":
    lista = [170, 45, 75, 90, 802, 24, 2, 66]
    resultado = radix_sort(lista.copy())
    print("RadixSort:", resultado)
