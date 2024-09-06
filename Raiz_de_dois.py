
Valor_1 = 1
Valor_2 = 2
contador = 0

while ( contador < 50 ):

    media = (Valor_1 + Valor_2)/2

    if min(media*media, Valor_1*Valor_1) < 2 < max(media*media, Valor_1*Valor_1):

        Valor_1 = Valor_1
        Valor_2 = media

    else:

        Valor_2 = Valor_2
        Valor_1 = media

    contador = contador + 1
    print(media)

# Só para brincar um pouco mais eu quero gerar um tabela para colocar os valores de (Valor_1 e Valor_2 e Media)