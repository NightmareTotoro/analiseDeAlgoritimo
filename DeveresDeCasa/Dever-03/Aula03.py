
# Funcao de recursao de verificacao de palindromo  
def palindromo_recursivo(arr, esquerda=0, direita=None):
    if direita is None:
        direita = len(arr) - 1
    
    if esquerda >= direita:
        return True
    
    if arr[esquerda] != arr[direita]:
        return False
    
    return palindromo_recursivo(arr, esquerda + 1, direita - 1)

# Exemplo de uso fornecido no slide
array1 = [0, 1, 2, 3, 2, 1, 0] 

array2 = ["a", "b", "b", "a"] 

array3 = ["a", "b", "c", "b", "a"] 

array4 = ["a", "b", "c", "f", "b", "a"]

print(palindromo_recursivo(array1))  # Saída: True
print(palindromo_recursivo(array2))  # Saída: True
print(palindromo_recursivo(array3))  # Saída: True
print(palindromo_recursivo(array4))  # Saída: False
