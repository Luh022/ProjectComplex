import heapq
def heuristic(node, goal):
    """Função heurística que estima o custo do nó ao objetivo (distância Euclidiana)"""
    return ((node[0] - goal[0]) ** 2 + (node[1] - goal[1]) ** 2) ** 0.5

def astar(mapa, inicio, objetivo):
    # Verifica se o início e o objetivo estão dentro dos limites do mapa
    if not (0 <= inicio[0] < len(mapa)) or not (0 <= inicio[1] < len(mapa[0])):
        raise ValueError("O ponto de início está fora dos limites do mapa.")
    if not (0 <= objetivo[0] < len(mapa)) or not (0 <= objetivo[1] < len(mapa[0])):
        raise ValueError("O ponto de objetivo está fora dos limites do mapa.")

    # Define os movimentos possíveis (8 direções: cima, baixo, esquerda, direita e diagonais)
    movimentos = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    # Inicializa as estruturas de dados
    fronteira = []
    heapq.heappush(fronteira, (0, inicio))  # Prioridade e posição atual
    custo_acumulado = {inicio: 0}  # Custo acumulado para chegar ao nó atual
    pais = {}  # Dicionário para rastrear o nó pai de cada nó visitado

    while fronteira:
        _, atual = heapq.heappop(fronteira)

        if atual == objetivo:
            # Constrói o caminho a partir do objetivo até o início
            caminho = [atual]
            while atual in pais:
                atual = pais[atual]
                caminho.append(atual)
            caminho.reverse()
            return caminho

        for movimento in movimentos:
            proximo = atual[0] + movimento[0], atual[1] + movimento[1]
            novo_custo = custo_acumulado[atual] + mapa[proximo[0]][proximo[1]]

            if proximo not in custo_acumulado or novo_custo < custo_acumulado[proximo]:
                custo_acumulado[proximo] = novo_custo
                prioridade = novo_custo + heuristic(proximo, objetivo)
                heapq.heappush(fronteira, (prioridade, proximo))
                pais[proximo] = atual

    raise ValueError("Não foi possível encontrar um caminho válido.")

# Exemplo de uso
mapa = [
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 1, -1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1]
]

inicio = (0, 0)
objetivo = (4, 4)

caminho = astar(mapa, inicio, objetivo)
print(caminho)