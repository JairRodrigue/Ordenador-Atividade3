import time
import platform
import psutil

# Função de ordenação Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    meio = len(arr) // 2
    esquerda = merge_sort(arr[:meio])
    direita = merge_sort(arr[meio:])

    return merge(esquerda, direita)

def merge(esquerda, direita):
    resultado = []
    i = j = 0

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    return resultado

def main():
    # Informações da linguagem e sistema
    print(f"Linguagem: Python")
    print(f"Versão: {platform.python_version()}")
    print(f"Sistema Operacional: {platform.system()} {platform.release()}")
    print(f"CPU: {platform.processor()}")
    print(f"Memória RAM: {round(psutil.virtual_memory().total / (1024**3), 2)} GB\n")

    # Lendo o arquivo
    with open('rsc/arq.txt', 'r') as file:
        numeros = [int(line.strip()) for line in file]

    # Merge Sort
    start_time = time.time()
    numeros = merge_sort(numeros)
    end_time = time.time()

    # Salvando em arquivo de saída
    with open('arq-saida.txt', 'w') as file:
        file.write('\n'.join(map(str, numeros)))

    # Informações de tempo e memória
    tempo_ms = (end_time - start_time) * 1000
    memoria_kb = psutil.Process().memory_info().rss / 1024
    print(f"Tempo de execução: {tempo_ms:.2f} ms")
    print(f"Memória utilizada: {memoria_kb:.2f} KB")

if __name__ == "__main__":
    main()
