# Projeto de Coloração de Grafos - PAA

Este projeto implementa e testa algoritmos para o problema de coloração de grafos, utilizando técnicas de backtracking e heurística para encontrar o número cromático mínimo e os tempos de execução. 

## Como Executar

### Pré-requisitos
- Python 3.x instalado
- Bibliotecas padrão do Python (json, time, statistics, os)

### Execução

1. **Prepare o arquivo de entrada**: 
   - O programa irá procurar por um arquivo JSON com os grafos a serem analisados
   - Por padrão, ele procura por `k4.json`, mas você pode modificar a variável `arquivo_json_entrada` no código
   - Se o arquivo não existir, o programa criará um arquivo de exemplo automaticamente

2. **Execute o programa**:
   ```bash
   python main.py
   ```

3. **Resultados**:
   - Os resultados serão salvos na pasta `output/` com o nome `resultados_baseline_{nome_do_arquivo_entrada}.json` para execuções do algorítimo baseline.
   - Troque o nome para 'resultados_heuristica_' quando necessário.
   - O programa salva os resultados incrementalmente após processar cada grafo.
   - Em caso de erro (ex: memory error), os dados já processados são preservados.

### Formato do Arquivo de Entrada

O arquivo JSON deve seguir este formato:
```json
{
  "nome_do_grafo": {
    "0": [1, 2],
    "1": [0, 2], 
    "2": [0, 1]
  }
}
```

Onde:
- As chaves são os vértices (como strings)
- Os valores são listas dos vértices adjacentes

### Configurações

- `QTD_TESTES`: Número de execuções para cada grafo (padrão: 3)
- Modifique as variáveis `arquivo_json_entrada` e `arquivo_json_saida` conforme necessário

### Exemplo de Uso

```bash
# Para testar com k4.json
python main.py

# Para outros arquivos, modifique a variável arquivo_json_entrada no código
```

O programa processará cada grafo do arquivo de entrada e gerará estatísticas de tempo de execução, número cromático encontrado e coloração resultante. 