def busca_inteligente(lista, alvo):
    if esta_ordenada(lista):
        return busca_binaria_recursiva(lista, alvo, 0, len(lista) - 1)
    else:
        return contem(lista, alvo)