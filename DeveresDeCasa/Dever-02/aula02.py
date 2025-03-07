import time # import necessario da lib time para calcular o tempo
import sys # lib necesarria para aumentar limite de recursoes 
sys.setrecursionlimit(4000) # usado para aumentar o limite de recursoes possiveis

# funcao fatorial obtida nos slides
def fatorial(n):

    if(n == 0):   # caso n = 0 retornara 0! = 1
        return 1
    else:
        return n * fatorial(n-1) # do contrario entrara num processo recurssivo

def mensuraTempo(valor):
    tempoInicio = time.time() # capturando o tempo atual que sera usado posteriormente 
    resultado = fatorial(valor) # chama a funcao fatorial e mensurar o tempo decorrido
    tempoFinal = time.time() # capturando o tempo final do processo para ser feito a diferenca

    return tempoFinal-tempoInicio , resultado

# nao tera tratamento dos caracteres recebidos
numero = int(input("calcular fatorial do lumero: ")) # adquirindo o valor fornecido no console
tempo, resultado = mensuraTempo(numero)
print(f"O fatorial de {numero} é {resultado}") # exibe resultado
# abaixo exibe o tempo decorrido
print(f'O tempo necessario para calcular o fatorial de {numero} foi de: {tempo:.10f} segundos')

lista_de_numero = [10, 100, 500, 1000] # numeros selecionado do slide para testes

# loop que ira fazer todos os testes necessarios
for i in lista_de_numero:
    print("\n \n _____________________")
    tempo, resultado = mensuraTempo(i)
    print(f"O fatorial de {i} é {resultado}") # exibe resultado
    # abaixo exibe o tempo decorrido
    print(f'O tempo necessario para calcular o fatorial de {i} foi de: {tempo:.10f} segundos')

""""
a funcao fatorial tem uma complexidade linear, observa-se é uma execucao simples
onde a complexidade, ou o tempo de processamento aumenta com a quantidade de
recursoes feitas

a complexidade de uma funcao fatorial é de O(n)

Tn = Tn-1   + 1

nos teste em minha maquina nao houve diferenças significativas 
de tempo de valor entre 10 e 500

foi visto apenas um valor de tempo em 1000 execucoes, onde
o resultado foi de 0.0010008812 segundos
ou 1 milesimo
"""


