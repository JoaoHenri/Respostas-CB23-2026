#Observação: apenas o quicksort tem pior caso, pois utiliza pivô para determinar a divisão da lista em sua estrutura para aplicar recursão enquanto o mergesort e o selectionsort têm seus casos de recursão pré-determinados (dividir em listas de tamanho 2 no caso do merge ou aplicar recursão em uma sublista de tamanho n-1 no caso do selection)


import AP_03_ordenacao as arquivo
import sys
import random
import time
sys.setrecursionlimit(10**6)

def gerador_de_lista(N):
    return [random.randint(0,N) for i in range(N)]

def pior_quick(N):
    return [x for x in range(N) [::-1]]

def avg_case(N):
    original = [x for x in range(N)]
    my_list = []
    while len(original):
        random_index = random.randint(0,len(original)-1)
        my_list.append(original[random_index])
        original[random_index], original[-1] = original[-1], original[random_index]
        original.pop(-1)
    return my_list




def perf_algo(sort_algo, N ,k,Worst_case = False):
    times = []
    for _ in range(k):
        my_list = avg_case(N) if not Worst_case else pior_quick(N)
        start_t = time.perf_counter()
        sort_algo(my_list)
        end_t = time.perf_counter()
        times.append(end_t - start_t)
    return sum(times)/k



resultados = []

# Valores de N que serão testados
valores_N = [100, 500, 1000, 5000, 10000]

# Número de repetições de cada teste
k = 10




for N in valores_N:

    tempo = perf_algo(
        arquivo.quick_sort,
        N,
        k,
        False
    )

    resultados.append([
        "Médio",
        k,
        "Quicksort",
        N,
        tempo
    ])



for N in valores_N:

    tempo = perf_algo(
        arquivo.quick_sort,
        N,
        k,
        True
    )

    resultados.append([
        "Pior",
        k,
        "Quicksort",
        N,
        tempo
    ])




for N in valores_N:

    tempo = perf_algo(
        arquivo.divide_and_conquer_sort,
        N,
        k,
        False
    )

    resultados.append([
        "Médio",
        k,
        "Mergesort",
        N,
        tempo
    ])




for N in valores_N:

    tempo = perf_algo(
        arquivo.selection_sort,
        N,
        k,
        False
    )

    resultados.append([
        "Médio",
        k,
        "Selection Sort",
        N,
        tempo
    ])





def mostrar_resultados(resultados):

    print()
    print(
        f"{'Caso':<15}"
        f"{'Testes':<10}"
        f"{'Método':<20}"
        f"{'N':<10}"
        f"{'Tempo médio (s)':<20}"
    )

    print("-" * 75)

    for resultado in resultados:

        caso, testes, metodo, N, tempo = resultado

        print(
            f"{caso:<15}"
            f"{testes:<10}"
            f"{metodo:<20}"
            f"{N:<10}"
            f"{tempo:<20.6f}"
        )
mostrar_resultados(resultados)
#minha_lista = [1,99,1023,4,9,100,9999999,4,666]
#print(arquivo.selection_sort(minha_lista))

