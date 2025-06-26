import json
import time
import statistics
import os
from backtracking import coloracao_grafo_backtracking

QTD_TESTES = 1  # Número de rodadas para cada grafo

# --- Funções de Leitura e Escrita de Dados ---
def carregar_grafos_do_json(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as f:
        dados = json.load(f)
    
    grafos_analisados = {}
    for id_grafo, lista_adj_str in dados.items():
        lista_adj_analisada = {}
        for u_str, vizinhos_str in lista_adj_str.items():
            u = int(u_str) # Converte a chave do vértice para int
            lista_adj_analisada[u] = [int(v) for v in vizinhos_str] # Converte os vizinhos para int
        grafos_analisados[id_grafo] = lista_adj_analisada
    return grafos_analisados

def salvar_resultados_em_json(resultados, caminho_arquivo):
    caminho_arquivo = os.path.join("output", caminho_arquivo)
    # Cria o diretório output se não existir
    os.makedirs("output", exist_ok=True)
    with open(caminho_arquivo, 'w', encoding='utf-8') as f:
        json.dump(resultados, f, indent=2, ensure_ascii=False)

def carregar_resultados_existentes(caminho_arquivo):
    """Carrega resultados existentes do arquivo JSON, se existir"""
    caminho_arquivo = os.path.join("output", caminho_arquivo)
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# --- Função Principal de Execução e Medição ---
def executar_testes_e_medir_tempo(caminho_arquivo_grafos, caminho_arquivo_saida):
    grafos = carregar_grafos_do_json(caminho_arquivo_grafos)
    
    # Carrega resultados existentes para não perder dados em caso de erro
    todos_resultados = carregar_resultados_existentes(caminho_arquivo_saida)

    for id_grafo, dados_grafo in grafos.items():
        print(f"Processando grafo: {id_grafo}")
        
        tempos = []
        cores_minimas = None
        coloracao_encontrada = None
        total_coloracoes = 0
        ultimo_total_coloracoes = 0
        
        try:
            # Calcula o número de arestas
            num_arestas = sum(len(adj) for adj in dados_grafo.values()) // 2

            for i in range(QTD_TESTES):
                print(f"  Executando teste {i+1}/{QTD_TESTES}")
                
                try:
                    inicio_tempo = time.perf_counter() # Usa perf_counter para medições de tempo mais precisas
                    k, c, total_coloracoes = coloracao_grafo_backtracking(dados_grafo)
                    fim_tempo = time.perf_counter()
                    
                    tempos.append(fim_tempo - inicio_tempo)
                    ultimo_total_coloracoes = total_coloracoes
                    
                    # A coloração e o número mínimo de cores serão os mesmos em todas as rodadas
                    # Podemos salvá-los na primeira rodada
                    if i == 0:
                        cores_minimas = k
                        coloracao_encontrada = c
                
                except Exception as e:
                    print(f"    Erro no teste {i+1}: {e}")
                    # Se der erro, registra o tempo como erro e interrompe os testes
                    tempos.append(f"ERRO: {e}")
                    if cores_minimas is None:
                        cores_minimas = f"ERRO: {e}"
                        coloracao_encontrada = f"ERRO: {e}"
                    break

            # Calcula tempo médio apenas dos testes que deram certo
            tempos_validos = [t for t in tempos if isinstance(t, (int, float))]
            if tempos_validos:
                tempo_medio = statistics.mean(tempos_validos)
            else:
                tempo_medio = f"ERRO: Nenhum teste completado"
            
            # Se houve erro, marca o total de colorações com asterisco
            if any(isinstance(t, str) for t in tempos):
                total_coloracoes_final = f"{ultimo_total_coloracoes}*"
            else:
                total_coloracoes_final = total_coloracoes
            
            todos_resultados[id_grafo] = {
                "num_vertices": len(dados_grafo),
                "num_arestas": num_arestas,
                "cores_minimas_encontradas": cores_minimas,
                "coloracao_encontrada": coloracao_encontrada,
                "tempos_execucao_segundos": tempos,
                "tempo_medio_segundos": tempo_medio,
                "total_coloracoes_geradas": total_coloracoes_final
            }
            
            print(f"  Resultados para '{id_grafo}': Mínimo de {cores_minimas} cores, Tempo médio: {tempo_medio}")
            
        except Exception as e:
            # Erro geral no processamento do grafo
            print(f"  Erro geral no grafo '{id_grafo}': {e}")
            todos_resultados[id_grafo] = {
                "num_vertices": len(dados_grafo) if 'dados_grafo' in locals() else f"ERRO: {e}",
                "num_arestas": f"ERRO: {e}",
                "cores_minimas_encontradas": f"ERRO: {e}",
                "coloracao_encontrada": f"ERRO: {e}",
                "tempos_execucao_segundos": [f"ERRO: {e}"],
                "tempo_medio_segundos": f"ERRO: {e}",
                "total_coloracoes_geradas": f"{ultimo_total_coloracoes}*"
            }
        
        # Salva após cada grafo para não perder dados
        salvar_resultados_em_json(todos_resultados, caminho_arquivo_saida)
        print(f"  Resultados parciais salvos em '{caminho_arquivo_saida}'")
        
    print(f"\nTodos os resultados salvos em '{caminho_arquivo_saida}'")

# --- Execução Principal ---
if __name__ == "__main__":
    arquivo_json_entrada = "input/k9.json"
    arquivo_json_saida = "resultados_baseline_"+arquivo_json_entrada

    # Cria um arquivo 'grafos.json' de exemplo se ele não existir
    # ou garante que seu 'grafos.json' esteja no formato correto
    try:
        with open(arquivo_json_entrada, 'x', encoding='utf-8') as f:
            grafos_exemplo = {
                "grafo_simples_p3": {
                    "0": [1],
                    "1": [0, 2],
                    "2": [1]
                },
                "grafo_completo_k4": {
                    "0": [1, 2, 3],
                    "1": [0, 2, 3],
                    "2": [0, 1, 3],
                    "3": [0, 1, 2]
                },
                "grafo_triangulo_c3": {
                    "0": [1, 2],
                    "1": [0, 2],
                    "2": [0, 1]
                },
                "grafo_maior_teste": { # Este pode demorar MUITO!
                    "0": [1, 2, 3],
                    "1": [0, 2, 4],
                    "2": [0, 1, 3, 4],
                    "3": [0, 2, 4],
                    "4": [1, 2, 3]
                }
            }
            json.dump(grafos_exemplo, f, indent=2, ensure_ascii=False)
        print(f"Arquivo '{arquivo_json_entrada}' de exemplo criado. Você pode editá-lo com seus grafos.")
    except FileExistsError:
        print(f"Arquivo '{arquivo_json_entrada}' já existe. Usando o existente.")
    
    executar_testes_e_medir_tempo(arquivo_json_entrada, arquivo_json_saida)