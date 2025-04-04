import random  # Import necessário para gerar valores aleatórios

# Árvore Binária de Busca (ABB)

class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

def inserir_abb(raiz, valor):
    """ Insere um valor na ABB """
    if raiz is None:
        return No(valor)
    
    if valor < raiz.valor:
        raiz.esquerda = inserir_abb(raiz.esquerda, valor)
    else:
        raiz.direita = inserir_abb(raiz.direita, valor)
    
    return raiz

def buscar_abb(raiz, valor):
    """ Busca um valor na ABB """
    if raiz is None:
        return False
    if valor == raiz.valor:
        return True
    elif valor < raiz.valor:
        return buscar_abb(raiz.esquerda, valor)
    else:
        return buscar_abb(raiz.direita, valor)

def remover_abb(raiz, valor):
    """ Remove um valor da ABB """
    if raiz is None:
        return None

    if valor < raiz.valor:
        raiz.esquerda = remover_abb(raiz.esquerda, valor)
    elif valor > raiz.valor:
        raiz.direita = remover_abb(raiz.direita, valor)
    else:
        # Caso 1: Nó sem filhos
        if raiz.esquerda is None and raiz.direita is None:
            return None
        # Caso 2: Nó com um filho
        elif raiz.esquerda is None:
            return raiz.direita
        elif raiz.direita is None:
            return raiz.esquerda
        # Caso 3: Nó com dois filhos
        else:
            sucessor = encontrar_minimo(raiz.direita)
            raiz.valor = sucessor.valor
            raiz.direita = remover_abb(raiz.direita, sucessor.valor)
    return raiz

def encontrar_minimo(no):
    """ Encontra o menor valor em uma subárvore """
    atual = no
    while atual.esquerda is not None:
        atual = atual.esquerda
    return atual

def construir_abb(n):
    """ Constrói uma ABB com N valores aleatórios """
    if n < 1:
        return None, []

    valores = random.sample(range(1, 100), n)  # Evita valores repetidos
    raiz = None
    for v in valores:
        raiz = inserir_abb(raiz, v)

    return raiz, valores

def imprimir_arvore(raiz, nivel=0):
    """ Imprime a árvore de forma hierárquica """
    if raiz is not None:
        imprimir_arvore(raiz.direita, nivel + 1)
        print(' ' * 4 * nivel + '->', raiz.valor)
        imprimir_arvore(raiz.esquerda, nivel + 1)

# Exemplo de uso
N = 15
arvore, valores_inseridos = construir_abb(N)
print("Árvore ABB gerada:")
imprimir_arvore(arvore)
print("Valores inseridos:", valores_inseridos)

# Teste de busca
valor_busca = valores_inseridos[5]
print(f"\nBusca pelo valor {valor_busca}: {buscar_abb(arvore, valor_busca)}")

# Teste de remoção
valor_remover = valores_inseridos[3]
print(f"\nRemovendo o valor {valor_remover}...")
arvore = remover_abb(arvore, valor_remover)
print("Árvore após remoção:")
imprimir_arvore(arvore)
