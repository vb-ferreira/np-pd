import marimo

__generated_with = "0.14.17"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# **Broadcasting**""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Já vimos que quando adicionamos um escalar a um array 1-D o escalar é adicionado a **cada elemento** do array.""")
    return


@app.cell
def _(np):
    print(np.array([1, 2, 3]) + 0.5)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""É como se o NumPy expandisse o escalar em um array de 3 elementos e então fizesse a adição **elemento a elemento** entre os arrays. (**O NumPy não faz isso porque seria muito ineficiente**, mas seria uma forma de obter o mesmo resultado). Este é um exemplo de **broadcasting**.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    /// attention | Atenção!

    **Nem todos** os pares de arrays são **compatíveis** para broadcasting. Dimensões de um array são compatíveis se forem **iguais** ou uma delas for **1**.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""**Exmplo 1**:""")
    return


@app.cell
def _(np):
    np.random.seed(1234)
    _A = np.random.randint(low = 1, high = 10, size = (3, 4))
    _B = np.random.randint(low = 1, high = 10, size = (3, 1))

    # print(_A)
    # [[4 7 6 5]
    #  [9 2 8 7]
    #  [9 1 6 1]]

    # print(_B)
    # [[7]
    #  [3]
    #  [1]]

    # Compatibilidade

    _A.shape  # (3, 4)
    _B.shape  # (3, 1)
    ##           ^  ^
    ##           compatíveis

    print(_A + _B)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Aqui, `A` é um array 3x4 e `B` é um array 3x1. **Começamos comparando a última dimensão de cada array**.

    1. Como a última dimensão de `A` tem comprimento 4 e a última dimensão de `B` tem comprimento 1, o NumPy poderia expandir `B` fazendo 4 cópias dele ao longo de seu segundo eixo. Portanto, essas dimensões são compatíveis.
    2. Agora, precisamos comparar a primeira dimensão de `A` e `B`. Como ambas têm comprimento 3, elas são compatíveis.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    /// tip | Dica

    Métodos como o `newaxis` e o `reshape` podem ser usados para tentar arrays compatíveis para o **broadcasting**.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# **Indexação Booleana**""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Com a indexação booleana, você pode **subdividir/fatiar** um array A usando outro array B de valores booleanos, que funciona como uma **máscara**.""")
    return


@app.cell
def _(np):
    array_ib = np.array([
        [3, 9, 7],
        [2, 0, 3],
        [3, 3, 1]
    ])

    mascara = array_ib == 3
    print(mascara)
    return array_ib, mascara


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Podemos usar `mascara` para **identificar/filtrar** elementos de `array_ib` que são **iguais a 3**.""")
    return


@app.cell
def _(array_ib, mascara):
    print(array_ib[mascara])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## **Fancy Indexing**""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Assim como arrays de inteiros, podemos usar arrays booleanas 1-D para **selecionar linhas ou colunas específicas** de um array 2-D.""")
    return


@app.cell
def _(array_ib):
    print(array_ib)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Ainda usando a **indexação booleana normal**, podemos selecionar as linhas da seguinte forma:""")
    return


@app.cell
def _(array_ib, np):
    r13 = np.array([True, False, True]) # linhas 1 e 3
    r23 = np.array([False, True, True]) # linhas 2 e 3

    print('Linhas 1 e 3:\n', array_ib[r13])
    print('Linhas 2 e 3:\n', array_ib[r23])
    return r13, r23


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Agora, observe o que acontece a seguir:""")
    return


@app.cell
def _(array_ib, r13, r23):
    print(array_ib[r13, r23]) # isso é equivalente a array_ib[[0,2], [1,2]]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    O NumPy trata índices booleanos como índices inteiros, onde **os inteiros usados são os índices dos elementos True**. Em outras palavras, **o NumPy trata o array de índices booleanos [True, False, True] como o array de índices inteiros [0, 2]** e **trata o array de índices booleanos [False, True, True] como o array de índices inteiros [1, 2]**.

    Portanto, `array_ib[r13, c23]` é equivalente a `array_ib[[0, 2], [1, 2]]`. Lembre-se de que, ao **combinar arrays de índices** de linha e coluna dessa maneira, o NumPy usa os índices correspondentes de cada array de índices (**índice de linha com índice de linha, índice de coluna com índice de coluna)** para selecionar elementos do array de destino, neste caso, os elementos **(0, 1)** e **(2, 2)**.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    /// tip | Dica

    A técnica de **fancy indexing** se baseia em fornecer uma **lista de índices para cada dimensão** que você quer selecionar. No caso, se você quer selecionar todas as linhas, mas apenas as colunas 1 e 2, use: `array_ib[:, [1, 2]]` ou `array_ib[:, [False, True, True]]`.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## **Operadores lógicos**""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""**Operadores lógicos** nos permitem **combinar arrays booleanos**. Eles incluem o operador "**bitwise-and**", o operador "**bitwise-or**" e o operador "**bitwise-xor**".""")
    return


@app.cell
def _(np):
    b1 = np.array([False, False, True, True])
    b2 = np.array([False, True, False, True])

    b1 & b2  # [False, False, False,  True], and
    b1 | b2  # [False,  True,  True,  True], or
    b1 ^ b2  # [False,  True,  True, False], xor (True apenas se diferentes!)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Um array de booleanos pode ser **negado** prefixando o operador `~`.""")
    return


@app.cell
def _(np):
    print(~np.array([False, True]))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# **Randomização e Generators**""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Desde a versão 1.17.0 do Numpy, **é recomendado usar um [Generator]([http://](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.default_rng)) para produzir valores aleatórios em vez de usar o [módulo random]([http://](https://numpy.org/doc/stable/reference/random/index.html?highlight=random#module-numpy.random))** diretamente.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## **Exemplos**""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""**1) Amostra de números inteiros, com substituição**: escolha três números inteiros no intervalo de 1 a 6, com substituição.""")
    return


@app.cell
def _(np):
    _generator = np.random.default_rng(seed=123)
    _sample = _generator.integers(low=1, high=7, size=3)

    print(_sample)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""**2) Amostra de números inteiros, sem substituição**: escolha três números inteiros no intervalo de 0 a 9, sem substituição.""")
    return


@app.cell
def _(np):
    _generator = np.random.default_rng(seed=123)
    _sample = _generator.choice(a=10, size=3, replace=False)

    print(_sample)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""**3) Permutação**: embaralhe aleatoriamente as linhas de um array.""")
    return


@app.cell
def _(np):
    _teste = np.array([
        [1, 2],
        [3, 4],
        [5, 6],
        [7, 8],
        [9, 10]
    ])

    _generator = np.random.default_rng(seed=123)
    _teste_permut = _generator.permutation(_teste, axis=0)

    print(_teste_permut)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""**4) Amostra de uma distribuição uniforme**: retire uma amostra aleatória de quatro valores entre 1 e 2 e gere a saída como um array 2x2.""")
    return


@app.cell
def _(np):
    _generator = np.random.default_rng(seed=123)
    _sample = _generator.uniform(low=1.0, high=2.0, size=(2, 2))

    print(_sample)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""**6) Amostra de uma distribuição normal**: retire uma amostra aleatória de dois valores de uma distribuição normal padrão e, em seguida, gere a saída como uma matriz 1-D de tamanho 2.""")
    return


@app.cell
def _(np):
    _generator = np.random.default_rng(seed=123)
    _sample = _generator.normal(loc=0.0, scale=1.0, size=2)

    print(_sample)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# **Desafios**""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## **Love Distance**""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## **Professor Prick**""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### **My Try** 👽""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## **Psycho Parent**""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### **My Try** 👿""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### **My Try** 👽""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Você é um professor vingativo e uma das suas maiores irritações é quando os alunos fazem as provas às pressas. Para dar uma lição neles, você decide dar zeros aos três primeiros alunos que tirarem menos de sessenta pontos, na ordem em que entregaram as provas.

    Dado um conjunto unidimensional de números inteiros, identifique os três primeiros valores menores que sessenta e substitua-os por zero.
    """
    )
    return


@app.cell
def _(np):
    _generator = np.random.default_rng(80085)
    scores = np.round(_generator.uniform(low=30, high=100, size=15))

    print(scores)
    return (scores,)


@app.cell
def _(np, scores):
    # Encontra os índices onde o valor é menor que 60
    indices = np.where(scores < 60)

    # Atribui o valor "0" aos elementos nos 3 primeiros índices
    scores[indices[0][:3]] = 0

    print('Resultado: ', scores)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Ansioso para deixar sua marca na Associação de Pais e Mestres, você decide que a melhor maneira de esconder ovos para a próxima caça aos ovos de Páscoa é usar o NumPy. Você representa o campo como uma matriz de 10x10 de 0's.""")
    return


@app.cell
def _(np):
    field = np.zeros(shape = (10, 10))

    print(field)
    return (field,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Insira 20 valores normais aleatórios em locais aleatórios (não repetidos) na grade. Assim, você saberá quanto doce esconder em cada local.""")
    return


@app.cell
def _(field, np):
    _generator = np.random.default_rng(seed=123)
    _values = _generator.normal(loc=0.0, scale=1.0, size=20)

    # Gera um array de 20 (len(_values)) números inteiros aleatórios entre 0 e 99 (field.siza)
    _indices = _generator.choice(field.size, len(_values), replace=False) 

    # Atribue os valores a uma view unidimensional de `field`
    field.ravel()[_indices] = _values

    print('Resposta:\n', field)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    /// tip | Dica

    O método `ravel()` tranforma um array multidimensional em unidimensional, ou seja, o **achata (flatten)**. Mas não retorna uma cópia ou altera o original, apenas apresenta uma **view (visualização temporária)**.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Você é um "cientista de relacionamentos" e desenvolveu um questionário que determina a pontuação de amor de uma pessoa — um número real entre 0 e 100. Sua teoria é que duas pessoas com pontuações de amor semelhantes devem formar uma boa combinação 👩‍❤️‍💋‍👨

    Dadas as pontuações de amor de 10 pessoas diferentes, crie um array bidimensional onde `(i, j)` fornece a diferença absoluta entre as pontuações de amor da pessoa `i` e da pessoa `j`.
    """
    )
    return


@app.cell
def _(np):
    _generator = np.random.default_rng(1010)
    love_scores = np.round(_generator.uniform(low=0, high=100, size=10), 2)

    print(love_scores)
    return (love_scores,)


@app.cell
def _(love_scores, np):
    np.set_printoptions(linewidth=999) # configuração de output
    # Adiciona 1 eixo a cada dimensão e faz a subtração (10, 1) - (1, 10)
    _resultado = np.abs(love_scores[:, np.newaxis] - love_scores[np.newaxis, :])

    print('Resultado: \n', _resultado)
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
