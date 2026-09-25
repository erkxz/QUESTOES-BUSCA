def contar_ocorrencias(lista, alvo):
    contador = 0
    for item in lista:
        if item == alvo:
            contador += 1
    return contador