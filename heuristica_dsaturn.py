
def _calcular_graus_iniciais(grafo):
    return {no: len(grafo[no]) for no in grafo.keys()}

def _obter_grau_saturacao(no, grafo, coloracoes):
    cores_vizinhos = set()
    for vizinho in grafo[no]:
        if vizinho in coloracoes:
            cores_vizinhos.add(coloracoes[vizinho])
    return len(cores_vizinhos)

def _encontrar_proximo_no_a_colorir(nos_nao_coloridos, grafo, coloracoes, grau_original):
    proximo_no = None
    max_saturacao = -1
    max_grau_para_desempate = -1

    for no in nos_nao_coloridos:
        saturacao_atual = _obter_grau_saturacao(no, grafo, coloracoes)
        grau_atual = grau_original[no]

        if saturacao_atual > max_saturacao:
            max_saturacao = saturacao_atual
            max_grau_para_desempate = grau_atual
            proximo_no = no
        elif saturacao_atual == max_saturacao:
            if grau_atual > max_grau_para_desempate:
                max_grau_para_desempate = grau_atual
                proximo_no = no
    return proximo_no

def _encontrar_cor_disponivel(no, grafo, coloracoes):
    cores_vizinhos = set(coloracoes[vizinho] for vizinho in grafo[no] if vizinho in coloracoes)
    cor_disponivel = 0
    while cor_disponivel in cores_vizinhos:
        cor_disponivel += 1
    return cor_disponivel

def dsatur_coloracao(grafo):
    nos = list(grafo.keys())
    num_nos = len(nos)
    coloracoes = {}
    
    grau_original = _calcular_graus_iniciais(grafo)

    k = 0

    while len(coloracoes) < num_nos:
        nos_nao_coloridos = [no for no in nos if no not in coloracoes]

        if not nos_nao_coloridos:
            break

        x_k = _encontrar_proximo_no_a_colorir(nos_nao_coloridos, grafo, coloracoes, grau_original)

        if x_k is None:
            break

        cor_atribuida = _encontrar_cor_disponivel(x_k, grafo, coloracoes)
        coloracoes[x_k] = cor_atribuida

        k = max(k, cor_atribuida + 1)

    return k, coloracoes, num_nos
