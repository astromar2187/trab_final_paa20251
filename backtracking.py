
def gerar_coloracoes(n, k, atual=[], todas=[]):
    print(f"Gerando coloracoes: {len(todas)} até agora, atual: {atual}")

    if len(atual) == n:
        todas.append(atual[:])
        return
    for cor in range(k):
        atual.append(cor)
        gerar_coloracoes(n, k, atual, todas)
        atual.pop()

def coloracao_valida(grafo, coloracao):
    for u in grafo:
        for v in grafo[u]:
            if coloracao[u] == coloracao[v]:
                return False 
    return True

def coloracao_grafo_backtracking(grafo):
    n = len(grafo)

    for k in range(1, n+1):
        todas = []
        gerar_coloracoes(n, k, [], todas)

        for coloracao in todas:
            if coloracao_valida(grafo, coloracao):
                return k, coloracao, len(todas)
    return None, None, None