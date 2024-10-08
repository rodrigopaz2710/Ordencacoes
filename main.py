from mergesort import mergesort
import time
start_time = time.time()


# Abre o arquivo para leitura
with open("numeros13.txt", "r") as file:
    # Lê todos os números do arquivo e converte para uma lista de inteiros
    numeros = [int(num) for num in file]

# Despreza o primeiro número e salva o restante em uma lista
lista_restante = numeros[1:]

mergesort(lista_restante)

# Exibe a lista resultante
for item in lista_restante:
    print(item)


end_time = time.time()
execution_time = end_time - start_time
print("Tempo de Execucao: ", execution_time)

