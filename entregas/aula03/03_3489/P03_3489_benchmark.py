import AulasPraticas.AP_03_ordenacao as ap3
import random
import time
import sys
sys.setrecursionlimit(10**6)
#aumenta o limite de recursão

def avg_case(N):
    original = [x for x in range(N)]
    #cria uma lista de N elementos distintos
    lista = []
    while len(original):
        random_index = random.randint(0,len(original)-1)
        lista.append(original[random_index])
        original[random_index], original[-1] = original[-1], original[random_index]
        original.pop(-1)
        #enquanto a lista original ainda houver elementos, pegaremos um termo aleatorio dessa lista, adcionaresmos na lista lista e removeremos da original
    return lista

def w_case(N):
    #retornamos uma lista com ordem estritamente descrescente
    #pois no caso quick_sort, uma lista estritamente decrescente faz com que o algoritmo faça operações em O(n²)
    # e, portanto, maximiza o tempo
    return [x for x in range(N)][::-1]

#o divide_and_conquer_sort e o selection_sort fazem o mesmo número de operaçõs respectivas ao algoritmo
#no primeiro, ficará com complexidade O(nlogn) e no segundo, O(n²)
#independente da ordenação da lista de entrada, portanto não há melhor caso

def perf_algo(sort_algo,N,k,worst_case_fun = None):
    times = []
    #criamos uma lista com os tempos
    for _ in range(k):
        lista = worst_case_fun(N) if worst_case_fun else avg_case(N)
        #aescolhemos se a lista está no pior caso ou no caso aleatorio
        start_t =  time.perf_counter()
        sort_algo(lista)
        end_t = time.perf_counter()
        #cronometramos quanto tempo leva para para ordenar a lista com o método sort_algo
        times.append(end_t - start_t)
        #adicionamos esse intervalo de tempo na lista times e retornamos a média dos tempos
    return sum(times)/k

Ns = [100, 500, 1000, 5000]
k = 50

algoritmos = [
    ("Quick Sort", ap3.quick_sort),
    ("Divide and Conquer", ap3.divide_and_conquer_sort),
    ("Selection Sort", ap3.selection_sort)
]

#agora basta iniciarmos a printar a tabela

print(f"{'Algoritmo':<22} | {'N':<6} | {'k':<4} | {'Cenário':<10} | {'Tempo Médio (s)':<15}")
print("-" * 76)

for nome_algo, funcao_algo in algoritmos:
    for n in Ns:
        tempo_medio = perf_algo(funcao_algo, n, k)
        print(f"{nome_algo:<22} | {n:<6} | {k:<4} | {'Médio':<10} | {tempo_medio:.20f}")    
        tempo_pior = perf_algo(funcao_algo, n, k, w_case)
        print(f"{nome_algo:<22} | {n:<6} | {k:<4} | {'Pior':<10} | {tempo_pior:.20f}")
        