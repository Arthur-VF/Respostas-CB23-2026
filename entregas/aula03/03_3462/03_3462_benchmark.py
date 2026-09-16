import AulasPraticas.AP_03_ordenacao as ord
import random
import time
import sys


sys.setrecursionlimit(10000)

def lista_media(n):
    return [random.randint(1, 100000) for _ in range(n)]

def pior_caso(n):
    return list(range(n, 0, -1))

tamanhos_n = [100, 500, 1000, 5000]
k = 50


print(f"{'Algoritmo':<18} | {'N':<5} | {'Caso Médio (s)':<15} | {'Pior Caso (s)':<15}")
print("-" * 62)


for Q in tamanhos_n:

    lista = lista_media(Q)
    lista_ruim = pior_caso(Q)

    total_s = 0
    total_ruim_s = 0
    for i in range(k):
        lista_teste1 = lista.copy()
        inicio1 = time.perf_counter()
        ord.selection_sort(lista_teste1)
        total_s += (time.perf_counter() - inicio1)

        lista_ruim_teste1 = lista_ruim.copy()
        inicio_ruim1 = time.perf_counter()
        ord.selection_sort(lista_ruim_teste1)
        total_ruim_s += (time.perf_counter() - inicio_ruim1)

    total_d = 0
    total_ruim_d = 0
    for q in range(k):
        lista_teste2 = lista.copy()
        inicio2 = time.perf_counter() 
        ord.divide_and_conquer_sort(lista_teste2)
        total_d += (time.perf_counter() - inicio2)

        lista_ruim_teste2 = lista_ruim.copy()
        inicio_ruim2 = time.perf_counter()
        ord.divide_and_conquer_sort(lista_ruim_teste2)
        total_ruim_d += (time.perf_counter() - inicio_ruim2)

    total_q = 0
    total_ruim_q = 0
    for j in range(k):
        lista_teste3 = lista.copy()
        inicio3 = time.perf_counter()
        ord.quick_sort(lista_teste3)
        total_q += (time.perf_counter() - inicio3) 

        lista_ruim_teste3 = lista_ruim.copy()
        inicio_ruim3 = time.perf_counter()
        ord.quick_sort(lista_ruim_teste3)
        total_ruim_q += (time.perf_counter() - inicio_ruim3)
   
    media_s = total_s / k
    media_ruim_s = total_ruim_s / k
    
    media_d = total_d / k
    media_ruim_d = total_ruim_d / k
    
    media_q = total_q / k
    media_ruim_q = total_ruim_q / k

    print(f"{'Selection Sort':<18} | {Q:<5} | {media_s:<15.6f} | {media_ruim_s:<15.6f}")
    print(f"{'Divide & Conquer':<18} | {Q:<5} | {media_d:<15.6f} | {media_ruim_d:<15.6f}")
    print(f"{'Quick Sort':<18} | {Q:<5} | {media_q:<15.6f} | {media_ruim_q:<15.6f}")
    print("-" * 62)