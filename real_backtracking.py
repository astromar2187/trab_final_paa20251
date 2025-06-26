def cor_valida_para_vertice(grafo, coloracao, vertice, cor):
    """Verifica se uma cor é válida para um vértice específico"""
    vertices = list(grafo.keys())
    vertice_atual = vertices[vertice]
    
    # Verifica se a cor conflita com algum vizinho já colorido
    for vizinho in grafo[vertice_atual]:
        # Encontra o índice do vizinho na lista de vértices
        if vizinho in vertices:
            indice_vizinho = vertices.index(vizinho)
            # Se o vizinho já foi colorido e tem a mesma cor, há conflito
            if indice_vizinho < vertice and coloracao[indice_vizinho] == cor:
                return False
    return True

def backtrack_coloracao(grafo, coloracao, vertice, k, contador):
    """Backtracking real para coloração de grafos"""
    contador[0] += 1  # Conta tentativas
    
    if vertice == len(grafo):
        return True  # Encontrou uma coloração válida
    
    for cor in range(k):
        if cor_valida_para_vertice(grafo, coloracao, vertice, cor):
            coloracao[vertice] = cor
            if backtrack_coloracao(grafo, coloracao, vertice + 1, k, contador):
                return True
            # Backtrack automático (coloracao[vertice] será sobrescrito)
    
    return False

def coloracao_grafo_real_backtracking(grafo):
    n = len(grafo)
    vertices = list(grafo.keys())
    total_tentativas_acumuladas = 0  # Acumula tentativas de todos os k's
    
    for k in range(1, n + 1):
        coloracao = [-1] * n  # -1 indica não colorido
        contador = [0]  # Usa lista para passar por referência
        
        print(f"Tentando com k={k} cores...")
        
        if backtrack_coloracao(grafo, coloracao, 0, k, contador):
            # Adiciona as tentativas deste k ao total acumulado
            total_tentativas_acumuladas += contador[0]
            
            # Converte a coloração para o formato original (dicionário)
            coloracao_dict = {}
            for i, vertice in enumerate(vertices):
                coloracao_dict[vertice] = coloracao[i]
            
            print(f"Coloração encontrada com {k} cores em {contador[0]} tentativas")
            print(f"Total de tentativas acumuladas: {total_tentativas_acumuladas}")
            return k, coloracao_dict, total_tentativas_acumuladas
        
        # Se não encontrou com este k, acumula as tentativas e continua
        total_tentativas_acumuladas += contador[0]
        print(f"Não foi possível colorir com {k} cores (tentativas: {contador[0]})")
    
    return None, None, total_tentativas_acumuladas