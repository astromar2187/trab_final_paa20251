
def gerar_coloracoes(n, k, atual=[], todas=[]):
    #print(f"Gerando coloracoes: {len(todas)} até agora, atual: {atual}")

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
    total_tentativas_acumuladas = 0  # Acumula tentativas de todos os k's

    for k in range(1, n+1):
        print(f"Tentando com k={k} cores...")
        todas = []
        gerar_coloracoes(n, k, [], todas)

        for coloracao in todas:
            if coloracao_valida(grafo, coloracao):
                # Adiciona as tentativas deste k ao total acumulado
                total_tentativas_acumuladas += len(todas)
                print(f"Coloração encontrada com {k} cores em {len(todas)} tentativas")
                print(f"Total de tentativas acumuladas: {total_tentativas_acumuladas}")
                return k, coloracao, total_tentativas_acumuladas
            
        # Se não encontrou com este k, acumula as tentativas e continua
        total_tentativas_acumuladas += len(todas)
        print(f"Não foi possível colorir com {k} cores (tentativas: {len(todas)})")
    
    return None, None, total_tentativas_acumuladas