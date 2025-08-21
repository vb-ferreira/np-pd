import marimo

__generated_with = "0.14.17"
app = marimo.App(width="medium", layout_file="layouts/beginner.slides.json")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""O [NumPy]([http://](https://numpy.org/)) é principal pacote para **computação científica** do Python. É também a **base** da biblioteca para análise de dados **Pandas**.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# **Por quê usar arrays NumPy?**""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Arrays NumPy são muito **parecidos com listas** do Python, porém bem **mais rápidos**!

    Listas podem armazenar tipos heterogêneos (por exemplo, ints e floats). Os **dados em um array devem ser do mesmo tipo**.

    Como os arrays contêm um tipo de dado **homogêneo**, você pode executar operações como `sum()` em um array de floats sem se preocupar que um desses elementos possa ser uma string.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# **Operações básicas**""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## **1-D Array**""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## **2-D Array**""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""**Criando** um array **unidimensional** a partir de uma lista.""")
    return


@app.cell
def _(np):
    array_1d = np.array([10, 20, 30, 40, 50])
    print(array_1d)
    return (array_1d,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Verificando a **dimensionalidade**.""")
    return


@app.cell
def _(array_1d):
    print(array_1d.ndim)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Verificando o **formato**.""")
    return


@app.cell
def _(array_1d):
    print(array_1d.shape)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Verificando o **número de elementos**.""")
    return


@app.cell
def _(array_1d):
    print(len(array_1d))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Você pode **criar** um array **bidimensional** a partir de uma **lista de listas**.""")
    return


@app.cell
def _(np):
    array_2d = np.array([
        [10, 20, 30, 40, 50], 
        [100, 200, 300, 400, 500]
    ])
    print(array_2d)
    return (array_2d,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Verifificando a **dimensionalidade**.""")
    return


@app.cell
def _(array_2d):
    print(array_2d.ndim)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Verificando o **formato**.""")
    return


@app.cell
def _(array_2d):
    print(array_2d.shape)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Verificando o **"tamanho"**.""")
    return


@app.cell
def _(array_2d):
    print(len(array_2d))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    /// tip | Dica

    Você pode se surpreender ao ver que `arr_2d` tem "tamanho" 2, não 10. Isso porque `arr_2d` pode ser interpretado como **um array que contém 2 arrays** dentro dele. Se quiser obter o número **total de elementos** aninhados no array, você pode usar o atributo `size` do array.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Verificando o **número de elementos** de um array **bidirecional**.""")
    return


@app.cell
def _(array_2d):
    print(array_2d.size)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Verificando o **tipo de objeto** contido em um array.""")
    return


@app.cell
def _(array_2d):
    print(array_2d.dtype)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# **Regras básicas**""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Existem **duas regras básicas** para um **array numpy**:

    1. Todos os **elementos** do array devem ser do **mesmo tipo** e **tamanho** .
    2. Se os elementos de um array também forem arrays, esses arrays internos devem ter o mesmo tipo e número de elementos entre si. Em outras palavras, **arrays multidimensionais devem ser retangulares, não irregulares**.
    """
    )
    return


@app.cell
def _(np):
    print(np.array([1, 'dois', 3]))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    /// attention | Atenção!

    Se você tentar criar um array a partir de uma lista que contém uma mistura de inteiros e strings, o numpy **não apresentará erro**. No entanto, ele **converte os inteiros em strings** para satisfazer a propriedade de que todos os elementos tem que ser do mesmo tipo.
    """
    )
    return


@app.cell
def _(np):
    array_irregular = np.array([
        [1, 2, 3, 4],
        [5, 6]
    ], dtype=object)

    print(array_irregular)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    /// attention | Atenção!

    Se você tentar criar um array a partir de **listas irregulares** o NumPy não lançará um **erro**, a não ser que você informe explicitamente `dtype=object`. Isso significa, porém, que o array é essencialmente uma lista Python e não oferece os benefícios de desempenho de usar um array.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# **Criando Arrays NumPy**""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Criando um array **unidimensional** de **zeros**.""")
    return


@app.cell
def _(np):
    print(np.zeros(shape=3))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Criando um array **bidimensional (3x5)** de **zeros**.""")
    return


@app.cell
def _(np):
    print(np.zeros(shape=(3, 5)))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Criando arrays com um **valor qualquer**.""")
    return


@app.cell
def _(np):
    print(np.full(shape=(3, 5), fill_value='gato'))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Criando um array **sequencial**.""")
    return


@app.cell
def _(np):
    print(np.arange(start=0, stop=5, step=1)) # o mesmo que np.arange(5)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    /// tip | Dica

    Note que no `arange()` o **ínicio é inclusivo** e o **fim exclusivo**.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# **Indexação**""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## **1-D Array**""")
    return


@app.cell
def _(array_1d):
    array_1d
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Você pode **acessar** um elemento de um array da mesma forma que uma lista em Python.""")
    return


@app.cell
def _(array_1d):
    print(array_1d[0]) # primeiro elemento
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Acessando o **último** elemento com **índice negativo**.""")
    return


@app.cell
def _(array_1d):
    print(array_1d[-1])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Se tentarmos **acessar um elemento fora dos limites** do array, receberemos um **erro “out of bounds”**.""")
    return


@app.cell
def _(array_1d):
    try:
        print(array_1d[999])
    except:
        print('out of bounds')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Podemos **acessar múltiplos elementos** passando um array com seus índicies.""")
    return


@app.cell
def _(array_1d):
    print(array_1d[[0, 1, -1]]) # primeiro, segundo e último elemento
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    O **fatiamento (slicing)** também é similar aos das listas em Python.

    A **assinatura** é: `array[ start index : end index : step size ]`
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## **2-D Array**""")
    return


@app.cell(hide_code=True)
def _(np):
    new_array = np.array([
        [5, 10, 15, 20],
        [25, 30, 35, 40],
        [45, 50, 55, 60]
    ])
    new_array
    return (new_array,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Internamente, o array acima é apenas um **bloco contíguo de memória que armazena alguns dados**. Como definimos um **array bidimensional**, o NumPy nos fornece **dois eixos** para indexar seus valores.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.image("public/img1.png", width=500)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Como o array tem **dois eixos (dimensões)**, o NumPy interpreta os dados como uma **matriz retangular**, onde o **eixo 0** é o eixo da **linha** e o **eixo 1** é o eixo da **coluna**. Isso significa que podemos subdividi-lo ausando uma **combinação** de índices de linha e coluna.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Recuperando o **penúltimo** e o **último** elemento das linhas **2** e **3**.""")
    return


@app.cell
def _(new_array):
    print(new_array[1:3, [-2, -1]])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# **Matemática básica com arrays**""")
    return


@app.cell
def _(np):
    foo = np.array([[4, 3], [1, 0]])
    bar = np.array([[1, 2], [3, 4]])
    return bar, foo


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""**Adição** de arrays.""")
    return


@app.cell
def _(bar, foo):
    print(foo + bar)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    /// tip | Dica

    Os valores de `foo` e `bar` são somados elemento a elemento (**[1, 1] + [1, 1]**, etc.). Esse padrão é chamado **element wise** e **se aplica a todas as operações matemáticas entre matrizes de tamanhos idênticos**.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## **Broadcasting**""")
    return


@app.cell
def _(foo):
    print(foo + 5)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Perceba que foi adicionado `5` a cada elemento do array. O mesmo ocorre na subtração, multiplicação, divisão e todas as outras operações aritméticas binárias. Esse comportamento é conhecido como [broadcasting]([http://](https://numpy.org/doc/stable/user/basics.broadcasting.html)). O discutiremos em detalhes mais adiante.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# **Desafios**""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## **High School Reunion**""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Com a reunião do colégio se aproximando rapidamente, você decide entrar em forma e perder peso. Você registra seu peso todos os dias durante cinco semanas, começando na segunda-feira.""")
    return


@app.cell
def _(np):
    pesos = 185 - np.arange(5*7) / 5

    print(pesos)
    return (pesos,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Dados esses pesos diários, construa um array com seu peso médio por fim de semana (sábado e domingo).""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### **My Try** 👽""")
    return


@app.cell
def _(pesos):

    _semanas = pesos.reshape(5, 7)
    # Seleciona os 2 últimos elementos de cada linha (ainda um arra 2-D)
    _fds = _semanas[:5, [-2, -1]]
    # Tira a média de cada linha
    _medias = _fds.mean(axis=1)

    print('Resultado: ', _medias)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### **Solution**""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## **Gold Miner**""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## **Roux**""")
    return


@app.cell
def _(pesos):
    _sabados = pesos[5::7]
    _domingos = pesos[6::7]
    _medias = (_sabados + _domingos) / 2

    print('Resultado: ', _medias)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Depois de maratonar o Discovery Channel, você larga o emprego de advogado para se tornar um minerador de ouro. Você decide prospectar cinco locais sob uma matriz de terra de 7x7. Quanto ouro você descobre em cada local?""")
    return


@app.cell
def _(np):
    np.random.seed(5555)
    gold = np.random.randint(low=0, high=10, size=(7,7))

    # print(gold)
    # [[2 3 0 5 2 0 3]
    #  [8 8 0 7 1 5 3]
    #  [0 1 6 2 1 4 5]
    #  [4 0 8 9 9 8 7]
    #  [4 2 7 0 7 2 1]
    #  [9 8 9 2 5 0 8]
    #  [1 9 8 2 6 4 3]]

    locs = np.array([
        [0,4],
        [2,2],
        [2,3],
        [5,1],
        [6,3]
    ])
    return gold, locs


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### **My Try** 👽""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Defina um array chamado `roux` como um array 1-D tal que, quando invertido, representa a sequência de números quadrados 1, 4, 9, 16, etc. com zeros intercalados entre eles.

    ```
    # roux array of length 5
    [9 0 4 0 1]

    # roux array of length 8
    [ 0 16  0  9  0  4  0  1]

    # roux array of length 12
    [ 0 36  0 25  0 16  0  9  0  4  0  1]
    ```
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Implemente uma função chamada `make_roux(n)` que insere `n`, o tamanho desejado do array, e gera como saída o array "roux" correspondente. Teste-a nos exemplos acima.

    **Obs**: Se o array for par inicia com zero, se for ímpar, com um quadrado.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### **My Try** 👿""")
    return


@app.cell
def _(gold, locs):
    _indices_linhas = locs[:, 0]
    _indices_colunas = locs[:, 1]
    _gold_found = gold[_indices_linhas, _indices_colunas] # fancy indexing

    print('Resultado: ', _gold_found)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Não consegui desenvolver.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# **Dependências**""")
    return


@app.cell
def _():
    import marimo as mo
    import numpy as np
    return mo, np


if __name__ == "__main__":
    app.run()
