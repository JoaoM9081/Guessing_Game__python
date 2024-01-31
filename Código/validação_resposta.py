from interface import linha
TAM = 8

def verificar_resposta(resposta, correta):
    # Verificando se a resposta tem o tamanho correto
    if len(resposta) != TAM:
        print('\033[1;31mErro na entrada. A resposta deve conter 8 digitos.\033[m')
        return False, False

    # Verificando se a resposta é um número
    try:
        int(resposta)
    except ValueError:
        print('\033[1;31mErro na entrada. A resposta deve ser uma data.\033[m')
        return False, False

    # Verificando cada caractere da resposta
    check = []
    pontuation = 0
    for i in range(TAM):
        if resposta[i] == correta[i]:
            check.append('✅')
            pontuation += 1
        else:
            check.append('❌')

    # Imprimindo o resultado da verificação
    print('Resposta: \n')
    print('|'.join(check))
    print('|'.join(resposta))
    print(linha())

    return pontuation == TAM, True