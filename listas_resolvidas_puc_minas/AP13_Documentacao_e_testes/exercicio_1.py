def contar_pares(lista_numeros):
    """Função que conta a quantidade de números pares
    
    Parâmetros: 
    Uma lista (list ) com x números do tipo INT, negativos ou positivos, incluindo o zero

    Retorno:
    Número inteiro que representa a quantidade de números pares dentro da lista, 

    Para lista (*lista*) vazias, será retornado 0
    Para apenas um número na lista e este for o zero será retornado 1
    Para números negativos dentro da lista, será retornando a quantidade de números negativos que forem múltiplos de 2
    
    """
    quantidade = 0
    for numero in lista_numeros:
        if numero %2 ==0:
            quantidade +=1
      
    return quantidade
