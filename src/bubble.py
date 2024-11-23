import time
import platform
import psutil

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

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

    # Bubble Sort
    start_time = time.time()
    bubble_sort(numeros)
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
