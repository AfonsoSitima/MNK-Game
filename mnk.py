#Função Auxiliar
def eh_jog(jog: int) -> bool:
    '''Recebe um argumento e retorna True se for um inteiro identificando um jogador e False caso contrário.'''

    return type(jog) == int and (jog == -1 or jog == 1)

#Função Auxiliar
def eh_k(k: int) -> bool:
    '''Recebe argumento e retorna True se for um inteiro positivo e False caso contrário.'''

    return type(k) == int and k > 0


#Função Auxiliar
def eh_lvl(lvl: str) -> bool:
    '''Recebe argumento e retorna True se for uma string identificando uma dificuldade e False caso contrário.'''

    return type(lvl) == str and (lvl == 'facil' or lvl == 'normal' or lvl == 'dificil')


#Função Auxiliar
def obtem_tamanho_tab(tab: tuple) -> int:
    '''Recebe um tabuleiro e devolve o seu tamanho (nº de posições).'''

    n_linha, n_coluna = obtem_dimensao(tab)
    return n_linha * n_coluna


#Função Auxiliar
def obter_index(tab: tuple, pos: int) -> tuple:
    '''Recebe um tabuleiro e uma posição e devolve o index da linha em que essa posição se encontra
         no tabuleiro e o index dessa posição nessa linha (coordenadas da posição na tabela).'''

    tamanho_linha = obtem_dimensao(tab)[1]  # numero de elementos de uma linha
    linha = 0
    while pos > tamanho_linha:  # Caso a posição seja superior ao nº de elementos de uma linha, passa-se para a próxima linha
        linha += 1
        pos -= tamanho_linha
    return (linha, pos - 1)  # Retorna o index da linha da posição | index dessa posição na linha (index coluna)

#Função Auxiliar
def posicoes_tab(tab: tuple) -> tuple:
    '''Recebe um tabuleiro e devolve um tuplo.'''

    n_linha, n_coluna = obtem_dimensao(tab)  # nº de linhas e colunas
    tab_posicoes = []
    posicoes = 1
    for i in range(n_linha):  # Conta o nº de linhas
        linha = ()
        for e in range(n_coluna):  # Conta o nº de colunas
            linha += (posicoes,)  # Adiciona posição
            posicoes += 1
        tab_posicoes.append(linha)  # Adiciona as linhas com as posicoes numa lista
    return tuple(tab_posicoes)  # Devolve posicoes do tabuleiro em tuplo


# 2.1.1
def eh_tabuleiro(arg):
    '''Recebe um argumento e devolve True se for um tabuleiro valido e False caso contrário.'''

    if not (type(arg) == tuple and 2 <= len(arg) <= 100 and type(arg[0]) == tuple):
        return False
    tamanho_linha = len(arg[0])  # Ver o tamanho da primeira linha para depois comparar com as outras
    for linha in range(len(arg)):  # linha é o index dos tuplos que fazem referencia às linhas detro do tabuleiro
        if not (type(arg[linha]) == tuple and 2 <= len(arg[linha]) <= 100 and len(arg[linha]) == tamanho_linha):
            return False
        for valor in arg[linha]:  # valor são os inteiros (-1 , 0, 1) que cada um dos espaços de uma linha pode tomar valor
            if not (type(valor) == int and (valor == 0 or valor == -1 or valor == 1)):
                return False
    return True  # Mudei o type(valor)


# 2.1.2
def eh_posicao(arg):
    '''Recebe um argumento e devolve True se for uma posição e False caso contrário.'''

    if not (type(arg) == int and 1 <= arg <= 10000):
        return False
    return True


# 2.1.3
def obtem_dimensao(tab: tuple):
    '''Recebe um tabuleiro e devolve tuplo com o nº de linhas e o nº de colunas desse tabuleiro.'''

    linha = len(tab)
    coluna = len(tab[0])
    return (linha, coluna)  # Retorna o nº de linhas | Retorna o nº de colunas


# 2.1.4
def obtem_valor(tab: tuple, pos: int) -> int:
    '''Recebe um tabuleiro e uma posição e devolve o valor dessa posição.'''

    index_linha, index_coluna = obter_index(tab, pos)
    return tab[index_linha][index_coluna]


# 2.1.5
def obtem_coluna(tab: tuple, pos: int) -> tuple:
    '''Recebe um tabuleiro e uma posição e devolve um tuplo que contem as posições da coluna onde essa posição está inserida.'''

    index_coluna = obter_index(tab, pos)[1]  # Vai buscar o index da pos na linha
    tuplo_coluna = ()
    for linha in posicoes_tab(tab):
        tuplo_coluna += (linha[index_coluna],)
    return tuplo_coluna  # Retorna as posicoes de uma coluna


# 2.1.6
def obtem_linha(tab: tuple, pos: int) -> tuple:
    '''Recebe um tabuleiro e uma posição e devolve um tuplo que contem as posições da linhs onde essa posição está inserida.'''

    index_linha = obter_index(tab, pos)[0]  # Obtem o index da linha que contem a posicao escolhida
    return posicoes_tab(tab)[index_linha]  # Retorna as posicoes linha


# 2.1.7
def obtem_diagonais(tab: tuple, pos: int) -> tuple:
    '''Recebe um tabuleiro e uma posição e devolve um tuplo que contem dois tuplos: um que contém as posições da
        diagonal onde essa posição está inserida e outro que contém as posições da antidiagonal onde essa posição está inserida.'''

    index_linha, index_coluna = obter_index(tab, pos)
    n_linha, n_coluna = obtem_dimensao(tab)
    diagonal = [pos]
    antidiagonal = [pos]
    i = 1
    while index_linha + i != n_linha and index_coluna + i != n_coluna:
        diagonal.append(posicoes_tab(tab)[index_linha + i][index_coluna + i])
        i += 1
    i = 1
    while index_linha - i >= 0 and index_coluna - i >= 0:
        diagonal.insert(0, posicoes_tab(tab)[index_linha - i][index_coluna - i])
        i += 1
    i = 1
    while index_linha - i >= 0 and index_coluna + i != n_coluna:
        antidiagonal.append(posicoes_tab(tab)[index_linha - i][index_coluna + i])
        i += 1
    i = 1
    while index_linha + i != n_linha and index_coluna - i >= 0:
        antidiagonal.insert(0, posicoes_tab(tab)[index_linha + i][index_coluna - i])
        i += 1

    return (tuple(diagonal), tuple(antidiagonal))


# 2.1.8
def tabuleiro_para_str(tab: tuple) -> str:
    '''Recebe uma tabuleiro e devolve uma string que o representa.'''

    tab_dic = {-1: 'O', 0: '+', 1: 'X'}
    tabuleiro = ''
    for i_linha in range(len(tab)):
        for pos in tab[i_linha]:
            tabuleiro += f'{tab_dic[pos]}'
            tabuleiro += '---'
        tabuleiro = tabuleiro[:-3]
        if i_linha != len(tab) - 1:
            tabuleiro += '\n'
            for i in range(len(tab[i_linha])):
                tabuleiro += '|   '
            tabuleiro = tabuleiro[:-3]
            tabuleiro += '\n'
    return tabuleiro


# 2.2.1
def eh_posicao_valida(tab: tuple, pos: int) -> bool:
    '''Recebe um tabuleiro e uma posição e devolve True caso essa posição válida e False caso contrário.'''

    if not (eh_posicao(pos) and eh_tabuleiro(tab)):
        raise ValueError('eh_posicao_valida: argumentos invalidos')
    return 1 <= pos <= obtem_tamanho_tab(tab)


# 2.2.2
def eh_posicao_livre(tab: tuple, pos: int) -> bool:
    '''Recebe um tabuleiro e uma posição e devolve True caso essa posições esteja livre e False caso contrário.'''

    if not (eh_tabuleiro(tab) and eh_posicao(pos) and eh_posicao_valida(tab, pos)):
        raise ValueError('eh_posicao_livre: argumentos invalidos')
    return obtem_valor(tab, pos) == 0


#Função Auxiliar
def valor_posicoes(tab: tuple) -> tuple:
    '''Recebe uma tabuleiro e devolve um tuplo formado por três outro tuplos: um que contém as posições livres do tabuleiro,
        outro que contém as posições ocupadas pelo jogador 1, e por último um que contém as posições ocupadas pelo jogador -1.'''

    livres = ()
    jog_menos_1 = ()
    jog_1 = ()
    pos = 1
    while eh_posicao_valida(tab, pos):
        i_linha, i_coluna = obter_index(tab, pos)
        if eh_posicao_livre(tab, pos):
            livres += (posicoes_tab(tab)[i_linha][i_coluna],)
        elif obtem_valor(tab, pos) == -1:
            jog_menos_1 += (posicoes_tab(tab)[i_linha][i_coluna],)
        else:
            jog_1 += (posicoes_tab(tab)[i_linha][i_coluna],)
        pos += 1
    return (livres, jog_1, jog_menos_1)


# 2.2.3
def obtem_posicoes_livres(tab: tuple) -> tuple:
    '''Recebe um tabuleiro e devolve um tuplo com todas as posições livres do tabuleiro.'''

    if not (eh_tabuleiro(tab)):
        raise ValueError('obtem_posicoes_livres: argumento invalido')
    return valor_posicoes(tab)[0]


# 2.2.4
def obtem_posicoes_jogador(tab: tuple, jog: int) -> tuple:
    '''Recebe um tabuleiro e um jogaodor e devolve um tuplo com todas as posições ocupadas pelo jogador no tabuleiro.'''

    if not (eh_tabuleiro(tab) and eh_jog(jog)):
        raise ValueError('obtem_posicoes_jogador: argumentos invalidos')
    return valor_posicoes(tab)[jog]


#Função Auxiliar
def distancia(tab: tuple, pos1: int, pos2: int) -> int:
    '''Recebe um tabuleiro e duas posições e devolve a distância entre elas segundo Chebyshev distance.'''

    i_l1, i_c1 = obter_index(tab, pos1)
    i_l2, i_c2 = obter_index(tab, pos2)
    d_cheb = (abs(i_l1 - i_l2), abs(i_c1 - i_c2))
    return max(d_cheb)


# 2.2.5
def obtem_posicoes_adjacentes(tab: tuple, pos: int) -> tuple:
    '''Recebe um tabuleiro e uma posição e devolve um tuplo que contém as posições adjacentes à posição'''

    if not (eh_tabuleiro(tab) and eh_posicao(pos) and eh_posicao_valida(tab, pos)):
        raise ValueError('obtem_posicoes_adjacentes: argumentos invalidos')
    adj = ()
    for linha in posicoes_tab(tab):
        for pos_in_linha in linha:
            if distancia(tab, pos, pos_in_linha) == 1:
                adj += (pos_in_linha,)
    return adj


#Função Auxiliar
def obtem_centro(tab: tuple) -> int:
    '''Recebe um tabuleiro e devolve a posição central do tabuleiro.'''

    n_linha, n_coluna = obtem_dimensao(tab)
    return (n_linha // 2) * n_coluna + n_coluna // 2 + 1


# 2.2.6
def ordena_posicoes_tabuleiro(tab: tuple, tup: tuple) -> tuple:
    '''Recebe um tabuleiro e um tuplo de posições do tabuleiro e devolve o tuplo com as posições em
    ordem ascendente de distância ao centro do tabuleiro.'''

    if not (eh_tabuleiro(tab) and type(tup) == tuple and 0 <= len(tup) <= obtem_tamanho_tab(tab)):
        raise ValueError('ordena_posicoes_tabuleiro: argumentos invalidos')
    tup = tuple(sorted(list(tup)))
    c = obtem_centro(tab)
    pos_i = 0
    dist = 0
    t_distancia = ()
    while len(tup) != 0:
        if not (type(tup[pos_i]) == int and 0<=tup[pos_i]<= obtem_tamanho_tab(tab)):   #Caso de erro outra vez confirmar que não há pos repetidas
            raise ValueError('ordena_posicoes_tabuleiro: argumentos invalidos')
        if distancia(tab, c, tup[pos_i]) == dist:  # Caso a distancia da pos ao cetro seja igual a dist/
            t_distancia += (tup[pos_i],)  # Adiciona ao tuplo t_distancia, organizando assim o tuplo
            tup = tup[:pos_i] + tup[pos_i + 1:]
        else:
            pos_i += 1
        if pos_i == len(tup):  # Como modifica o comprimento do tuplo, tem que começar do idx 0 para rever as pos que faltam
            pos_i = 0
            dist += 1
    return t_distancia


'''tab = ((1,0,0,0),
       (1,0,0,0),
       (1,0,0,0),
       (1,0,0,0))
print(ordena_posicoes_tabuleiro(tab, (14,15,11,12,13,1,2)) )'''


# 2.2.7
def marca_posicao(tab: tuple, pos: int, jog: int) -> tuple:
    '''Recebe uma tabela, uma posição e um jogador e devolve um novo tabuleiro com uma nova pedra do jogador
    indicado na posição indicada.'''

    if not (eh_tabuleiro(tab) and eh_posicao(pos) and eh_posicao_valida(tab, pos) and eh_posicao_livre(tab,pos) and eh_jog(jog)):
        raise ValueError('marca_posicao: argumentos invalidos')
    i_linha, i_coluna = obter_index(tab, pos)
    nova_tab = list(tab)
    nova_tab[i_linha] = tab[i_linha][:i_coluna] + (jog,) + tab[i_linha][i_coluna + 1:]
    return tuple(nova_tab)


#Função Auxiliar
def obtem_comum(tab: tuple, pos1: int, pos2: int) -> tuple:
    '''Recebe um tabuleiro e duas posições e devolve a linha/coluna/diagonal/antidiagonal (tuplo) comum às duas posições.'''

    dig, anti = obtem_diagonais(tab, pos1)
    linha = obtem_linha(tab, pos1)
    coluna = obtem_coluna(tab, pos1)
    if pos2 in linha:
        return obtem_linha(tab, pos1)
    elif pos2 in coluna:
        return obtem_coluna(tab, pos1)
    elif pos2 in dig:
        return obtem_diagonais(tab, pos1)[0]
    elif pos2 in anti:
        return obtem_diagonais(tab, pos1)[1]


#Função Auxiliar
def ver_sequencia(tab: tuple, pos: int, valor_adj: int, comum: tuple) -> int:
    '''Recebe um tabuleiro, uma posição, o valor de uma posição adjacente a essa posição e a
    linha/coluna/diagonal/antidiagonal (tuplo) comum a essas posições e devolve o tamanho da sequência
    que é possível formar com posições do (tuplo) comum com o mesmo valor da adjacente da posição.'''

    seq = 1
    idx_pos_na_linha = comum.index(pos)
    while idx_pos_na_linha > 0:  # Vai calcular a sequencia
        idx_pos_na_linha -= 1
        if valor_adj == obtem_valor(tab, comum[idx_pos_na_linha]):
            seq += 1
        else:
            break
    idx_pos_na_linha = comum.index(pos)
    while idx_pos_na_linha < len(comum) - 1:
        idx_pos_na_linha += 1
        if valor_adj == obtem_valor(tab, comum[idx_pos_na_linha]):
            seq += 1
        else:
            break
    return seq


# 2.2.8
def verifica_k_linhas(tab: tuple, pos: int, jog: int, k: int) -> bool:
    '''Recebe um tabuleiro, uma posição, um jogador e um k e devolve True caso haja uma pelo menos uma linha /coluna
       / diagonal / antidiagonal que contenha a posição com k ou mais pedras do jogador indicado e False caso contrário'''

    if not (eh_tabuleiro(tab) and eh_posicao(pos) and eh_posicao_valida(tab, pos) and eh_jog(jog) and eh_k(k)):
        raise ValueError('verifica_k_linhas: argumentos invalidos')
    if jog != obtem_valor(tab, pos):
        return False
    if k==1 and obtem_posicoes_jogador(tab,jog) != 0:
        return True
    for adj in obtem_posicoes_adjacentes(tab, pos):
        if obtem_valor(tab,adj) == jog:           # Caso pos tenha o mesmo valor que uma pos adj, entra no ciclo para verificar se há uma sequencia de k
            comum = obtem_comum(tab, pos, adj)    # Vai dar o tuplo da linha/coluna/diagonal comum às duas pos
            if ver_sequencia(tab, pos, jog, comum) >= k:
                return True
    return False


# 2.3.1
def eh_fim_jogo(tab: tuple, k: int) -> bool:
    '''Recebe um tabuleiro e um k e devolve True caso o jogo tenha terminado e False caso contrário'''

    if not (eh_tabuleiro(tab) and eh_k(k)):
        raise ValueError('eh_fim_jogo: argumentos invalidos')
    if len(obtem_posicoes_livres(tab)) == 0:
        return True
    jogs = (-1, 1)
    for jog in jogs:
        for pos in obtem_posicoes_jogador(tab, jog):
            if verifica_k_linhas(tab, pos, jog, k):
                return True
    return False


# 2.3.2
def escolhe_posicao_manual(tab: tuple) -> int:
    '''Recebe um tabuleiro e devolve a posição introduzida pelo utilizador'''

    if not (eh_tabuleiro(tab)):
        raise ValueError('escolhe_posicao_manual: argumento invalido')
    pedido = input('Turno do jogador. Escolha uma posicao livre: ')
    t = ()
    for e in obtem_posicoes_livres(tab):
        t += (str(e),)
    while pedido not in t:
        pedido = input('Turno do jogador. Escolha uma posicao livre: ')
    return int(pedido)


#Função Auxiliar
def ver_adjacente_jog(tab: tuple, pos: int, jog: int) -> bool:
    '''Recebe um tabuleiro, uma posição e um jogador e devolve True caso pelo menos uma posição adjacente à posição
    seja ocupada por uma pedra do mesmo valor das pedra jogadas pelo jogador.'''

    for adj in obtem_posicoes_adjacentes(tab, pos):
        if jog == obtem_valor(tab, adj):
            return True
    return False


#Função Auxiliar
def facil(tab: tuple, jog: int) -> int:
    '''Recebe um tabuleiro e um jogador e devolve a posição escolhida automaticamente de acordo com a estratégia facil.'''

    pos_possiveis = ()
    for pos in obtem_posicoes_livres(tab):
        if ver_adjacente_jog(tab, pos, jog):
            pos_possiveis += (pos,)
    if len(pos_possiveis) != 0:
        return ordena_posicoes_tabuleiro(tab, pos_possiveis)[0]
    return ordena_posicoes_tabuleiro(tab, obtem_posicoes_livres(tab))[0]


#Função Auxiliar
def obtem_sequencia(tab: tuple, jog: int, k: int) -> tuple:
    '''Recebe um tabuleiro, um jogador e um k e devolve um tuplo que contém: o maior valor de L pedras consecutivas que o próprio pode
    conseguir colocar na próxima jogada, o maior valor de L pedras consecutivas que o adversário pode conseguir colocar na próxima jogada,
    um tuplo com as posições que permitem que o próprio coloque uma pedra para obter L pedras próprias consecutivas e um tuplo
    com as posições que permitem que o adversário coloque uma pedra para obter L pedras adversárias consecutivas.'''

    pos_possiveis_propria = ()
    pos_possiveis_adv = ()
    L_proprio = 0
    L_adv = 0
    for pos in obtem_posicoes_livres(tab):  # Procura pos livre
        for adj in obtem_posicoes_adjacentes(tab, pos):  # Vê adj a essa pos
            if obtem_valor(tab, adj) == -1 or obtem_valor(tab, adj) == 1:
                valor_adj = obtem_valor(tab, adj)  # Ver valor da adj para depois indentificar L_pro e L_adv
                comum = obtem_comum(tab, pos, adj)
                melhor = ver_sequencia(tab, pos, valor_adj, comum)
                if melhor > k:
                    melhor = k
                if valor_adj == jog:  # Caso a seq criada seja maior que L, L passa a ter o valor dessa seq e é guardada a pos
                    if melhor > L_proprio:
                        L_proprio = melhor
                        pos_possiveis_propria = (pos,)
                    elif melhor == L_proprio and pos not in pos_possiveis_propria:
                        pos_possiveis_propria += (pos,)
                else:
                    if melhor > L_adv:
                        L_adv = melhor
                        pos_possiveis_adv = (pos,)
                    elif melhor == L_adv and pos not in pos_possiveis_adv:
                        pos_possiveis_adv += (pos,)
    return L_proprio, L_adv, pos_possiveis_propria, pos_possiveis_adv


#Função Auxiliar
def normal(tab: tuple, jog: int, k: int) -> int:
    '''Recebe um tabuleiro, um jogador e um k e devolve a posição escolhida automaticamente de acordo com a estratégia normal.'''

    if len(obtem_posicoes_livres(tab)) == obtem_tamanho_tab(tab):  # Caso seja a primeira jogada, joga no centro
        return obtem_centro(tab)
    L_proprio, L_adv, pos_possiveis_propria, pos_possiveis_adv = obtem_sequencia(tab, jog, k)
    if L_proprio >= L_adv:
        return ordena_posicoes_tabuleiro(tab, pos_possiveis_propria)[0]
    else:
        return ordena_posicoes_tabuleiro(tab, pos_possiveis_adv)[0]



#Função Auxiliar
def dificil(tab: tuple, jog: int, k: int) -> int:
    '''Recebe um tabuleiro, um jogador e um k e devolve a posição escolhida automaticamente de acordo com a estratégia dificil.'''

    if jog == -1:    #definir qual é o jog e o adv
        adv = 1
    else:
        adv = -1
    marcar_empate = ()
    L_proprio, L_adv, pos_possiveis_propria, pos_possiveis_adv = obtem_sequencia(tab, jog, k)
    if L_proprio == k:          #Caso melhor seq do proprio seja = k
        return ordena_posicoes_tabuleiro(tab, pos_possiveis_propria)[0]
    elif L_adv == k:
        return ordena_posicoes_tabuleiro(tab, pos_possiveis_adv)[0]
    for pos in ordena_posicoes_tabuleiro(tab, obtem_posicoes_livres(tab)):    # Ver todas as pos livres para depois simular
        novo_tab = tab
        turno = 0
        while True:     #Inicio da simulação
            L_proprio_sim, L_adv_sim, _, _ = obtem_sequencia(novo_tab, jog, k)
            if turno == 0:
                novo_tab = marca_posicao(novo_tab, pos , jog)
            elif turno % 2 == 0:
                if L_proprio_sim == k:          #Caso o proprio consiga fazer uma sequencia == k, e como começa pelas pos perto do meio dá logo return
                    return pos       
                novo_tab = marca_posicao(novo_tab, normal(novo_tab, jog, k), jog)
            else:
                if L_adv_sim == k:             #Caso, no turno do adv, ele consiga ganhar, break da simulação
                    break
                novo_tab = marca_posicao(novo_tab, normal(novo_tab, adv, k), adv)
            if len(obtem_posicoes_livres(novo_tab)) == 0:      #Caso dê empate, marcar como empate
                marcar_empate += (pos,)
                break
            turno += 1
    if len(marcar_empate) != 0 and len(obtem_posicoes_livres(tab)) != len(marcar_empate):
        return marcar_empate[0]
    else:
        return ordena_posicoes_tabuleiro(obtem_posicoes_livres(tab)[0])
    




#2.3.3
def escolhe_posicao_auto(tab: tuple, jog: int, k: int, lvl: str) -> int:
    '''Recebe um tabuleiro, um jogador, um k e uma dificuldade e devolve a posição escolhida automaticamente de acordo com a dificuldade.'''


    if not (eh_tabuleiro(tab) and eh_jog(jog) and eh_k(k) and eh_lvl(lvl) and not eh_fim_jogo(tab, k)):
        raise ValueError('escolhe_posicao_auto: argumentos invalidos')
    if lvl == 'facil':
        return facil(tab, jog)
    elif lvl == 'normal':
        return normal(tab, jog, k)
    elif lvl == 'dificil':
        return dificil(tab, jog, k)

 

#2.3.4
def jogo_mnk(cfg: tuple, jog: int, lvl: str) -> int:
    '''Recebe um tuplo de três valores inteiros (m,n,k) que representam a configuração do jogo, um jogador e uma dificuldade
    e devolve o jogador que ganhou o jogo. É nesta função onde o jogo decorre'''

    if not(eh_jog(jog) and eh_lvl(lvl) and type(cfg)==tuple and len(cfg) == 3 and eh_k(cfg[2])):
        raise ValueError('jogo_mnk: argumentos invalidos')
    for i in range(len(cfg)-1):
        if not(type(cfg[i]) == int and 2<=cfg[i]<=100):
            raise ValueError('jogo_mnk: argumentos invalidos')
    print('Bem-vindo ao JOGO MNK.')
    if jog == 1:
        print("O jogador joga com 'X'.")
        adv = -1
        turno = 0
    else:
        print("O jogador joga com 'O'.")
        turno = 1
        adv = 1
    linhas_tab = (0,) * cfg[1]
    tab = (linhas_tab,) * cfg[0]
    print(tabuleiro_para_str(tab))
    while not eh_fim_jogo(tab, cfg[2]):
        if turno%2 == 0:
            tab = marca_posicao(tab,escolhe_posicao_manual(tab),jog)
            last = 0
        else:
            print(f'Turno do computador ({lvl}):')
            tab = marca_posicao(tab, escolhe_posicao_auto(tab,adv,cfg[2],lvl), adv)
            last = 1
        print(tabuleiro_para_str(tab))
        turno += 1
    if len(obtem_posicoes_livres(tab))==0:
        print('EMPATE')
        return 0
    elif last == 0:
        print('VITORIA')
        return jog
    else:
        print('DERROTA')
        return adv
    
jogo_mnk((3,3,3),-1,'dificil')
