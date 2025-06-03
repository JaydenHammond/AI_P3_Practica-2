# merge_sort y función auxiliar merge: divide recursivamente y luego combina subarreglos ordenados
def merge(left, right):
    merged = []
    i = j = 0
    # Combina comparando el frente de cada subarreglo
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    # Agrega los elementos restantes
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

# Ejemplo de uso
if __name__ == "__main__":
    lista = [38, 27, 43, 3, 9, 82, 10]
    resultado = merge_sort(lista.copy())
    print("MergeSort:", resultado)
