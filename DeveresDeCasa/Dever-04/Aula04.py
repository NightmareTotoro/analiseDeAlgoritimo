

def funcaoRecursiva(n):
    if(n == 1):
        return 2

    return 2 * funcaoRecursiva(n - 1) + n**2

# pede para o usuario o valor de n
n = int(input("Digite um valor para n: "))

# mostra o resultado da rercussividade 
print(f"F({n}) = {funcaoRecursiva(n)}")
