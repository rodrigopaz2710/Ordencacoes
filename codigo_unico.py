import time

# Função Quicksort
def quicksort(lista):
    if len(lista) <= 1:
        return lista
    pivo = lista[len(lista) // 2]
    esquerda = [x for x in lista if x < pivo]
    meio = [x for x in lista if x == pivo]
    direita = [x for x in lista if x > pivo]
    return quicksort(esquerda) + meio + quicksort(direita)

# Função MergeSort
def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    meio = len(lista) // 2
    esquerda = merge_sort(lista[:meio])
    direita = merge_sort(lista[meio:])
    return merge(esquerda, direita)

# Função de mesclagem 
def merge(esquerda, direita):
    resultado = []
    i = j = 0
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    return resultado

# Função para carregar dados de teste
def carregar_dados_teste(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r') as arquivo:
            dados = [int(linha.strip()) for linha in arquivo]
        return dados
    except FileNotFoundError:
        print(f"Erro: Arquivo {caminho_arquivo} não encontrado.")
        return []
    except ValueError:
        print("Erro: O arquivo contém valores que não são números inteiros.")
        return []

# Caminho do arquivo de teste, ai aqui eh so mudar o nome do arquivo que quer ler
caminho_arquivo = "numeros13.txt"
dados = carregar_dados_teste(caminho_arquivo)

if dados:
    # Medindo o tempo do Quicksort
    tempo_inicio = time.time()
    resultado_quicksort = quicksort(dados)
    tempo_fim = time.time()
    print(f"Tempo de execução do Quicksort: {tempo_fim - tempo_inicio} segundos")

    # Medindo o tempo do MergeSort
    tempo_inicio = time.time()
    resultado_mergesort = merge_sort(dados)
    tempo_fim = time.time()
    print(f"Tempo de execução do MergeSort: {tempo_fim - tempo_inicio} segundos")
