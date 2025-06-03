# tree_sort: Inserta cada elemento en un BST y extrae el recorrido inorden para obtener orden ascendente.
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert_node(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert_node(root.left, key)
    else:
        root.right = insert_node(root.right, key)
    return root

def inorder_traversal(root, result):
    if root:
        inorder_traversal(root.left, result)
        result.append(root.key)
        inorder_traversal(root.right, result)

def tree_sort(arr):
    root = None
    # Construye el BST
    for key in arr:
        root = insert_node(root, key)
    sorted_list = []
    # Recolecta en inorden
    inorder_traversal(root, sorted_list)
    return sorted_list

# Ejemplo de uso
if __name__ == "__main__":
    lista = [5, 3, 7, 2, 4, 6, 8]
    resultado = tree_sort(lista.copy())
    print("TreeSort:", resultado)
