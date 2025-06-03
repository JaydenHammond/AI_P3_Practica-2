# insertion_sort (se reutiliza) para ordenar cada cubeta
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# bucket_sort: Crea k cubetas y reparte los elementos según su valor/dominio
def bucket_sort(arr, k=10):
    if not arr:
        return arr
    n = len(arr)
    # Encuentra mínimo y máximo para mapear rango [min, max] a cubetas
    min_val, max_val = min(arr), max(arr)
    diferencia = max_val - min_val + 1
    buckets = [[] for _ in range(k)]
    # Distribuye cada elemento en la cubeta correspondiente
    for num in arr:
        index = ( (num - min_val) * k ) // diferencia
        buckets[index].append(num)
    # Ordena cada cubeta y concatena resultados
    sorted_arr = []
    for bucket in buckets:
        sorted_bucket = insertion_sort(bucket)
        sorted_arr.extend(sorted_bucket)
    return sorted_arr

# Ejemplo de uso
if __name__ == "__main__":
    lista = [29, 25, 3, 49, 9, 37, 21, 43]
    resultado = bucket_sort(lista.copy(), k=5)
    print("BucketSort (Hashing):", resultado)
