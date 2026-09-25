def busca_binaria_recursiva(lista, alvo, baixo, alto):
    if baixo > alto:
        return -1
    meio = (baixo + alto) // 2
    if lista[meio] == alvo:
        return meio
    elif lista[meio] < alvo:
        return busca_binaria_recursiva(lista, alvo, meio + 1, alto)
    else:
        return busca_binaria_recursiva(lista, alvo, baixo, meio - 1)