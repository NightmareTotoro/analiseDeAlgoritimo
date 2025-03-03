# importando bibliotecas
import time
from random import randint 

# funcao de ordenamento bubble sorte
def bubble_sort(arr):
    n = len(arr)
    
    # Passa por todos os elementos da lista
    for i in range(n):
        # Últimos elementos já estão ordenados
        for j in range(0, n-i-1):
            # Troca se o elemento encontrado for maior que o próximo
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]



#funcao que calcula o tempo de execucao
def calcularTempo(lista):
        
    print("iniciando tempo ...")
    tempoInicio = time.time() # inicio do cronometro

    bubble_sort(lista) # chamada de algoritmo 
    
    tempoFinal = time.time() # final do cronometro
    print(f"tempo de corrido: {tempoFinal-tempoInicio:.6f}") # mostra resultado

# declarando arrays a serem ordenados
arr_100 = [randint(1,100) for _ in range(100)]
arr_1000 = [randint(1,1000) for _ in range(1000)]
arr_10_000 = [randint(1,10000) for _ in range(10000)]
arr_100_000 = [randint(1,100000) for _ in range(100000)]

#iniciando os testes
calcularTempo(arr_100)
calcularTempo(arr_1000)
calcularTempo(arr_10_000)
calcularTempo(arr_100_000)