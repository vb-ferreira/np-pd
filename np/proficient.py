import marimo

__generated_with = "0.14.17"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# **`where()`**""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Já vimos que o `where()` pode ser usado para retornar **índices** de um array com base em uma **condição**. Mas ele é mais poderoso que isso, podendo atuar como um **if-else**.""")
    return


@app.cell
def _(np):
    arr_where = np.array([
        [1, 2, 3],
        [4, 5, 6]
    ])

    print(np.where(arr_where % 2 == 0, 'par', 'ímpar'))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# **Funções matemáticas**""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## **`sum()`**""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Vamos ver alguns exemplos de uso da função `sum()`.""")
    return


@app.cell
def _(np):
    soma = np.array([
        [5.0, 2.0, 9.0],
        [1.0, 0.0, 2.0],
        [1.0, 7.0, 8.0]
    ])
    return (soma,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Somando **todos** os valores do array.""")
    return


@app.cell
def _(np, soma):
    print(np.sum(soma))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Somando na **direção** do **eixo 0** (**column sums**).""")
    return


@app.cell
def _(np, soma):
    print(np.sum(soma, axis=0))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Somando na **direção** do **eixo 1** (**row sums**).""")
    return


@app.cell
def _(np, soma):
    print(np.sum(soma, axis=1))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Se o array contiver `NaN`, a função `sum()` retornará `NaN`.""")
    return


@app.cell
def _(np):
    arr_nan= np.array([np.nan, 1, 10])

    print(np.sum(arr_nan))
    return (arr_nan,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Existem **3 técnicas** para evitar isso (**escapar os NaN's**).""")
    return


@app.cell
def _(arr_nan, np):
    # parâmetro `where`
    print(np.sum(arr_nan, where = ~np.isnan(arr_nan)))  # 11.0

    # função nan_to_num()
    print(np.sum(np.nan_to_num(arr_nan)))  # 11.00

    # função nansum()
    print(np.nansum(arr_nan)) # 11.0
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    /// tip | Dica

    O NumPy disponibiliza [diversas outras]([http://](https://numpy.org/doc/stable/reference/routines.math.html)) **funções matemáticas**.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# **Truth Value Testing**""")
    return


@app.cell
def _(np):
    arr1 = np.array([
        [np.nan,    4.4],
        [   1.0,    3.2],
        [np.nan, np.nan],
        [   0.1, np.nan]
    ])
    return (arr1,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## **`all()`**""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Você pode usar a função `all()` para verificar se **todos os valores** em um array **atendem a alguma condição**.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Verificando se **todos** os valores são `NaN`.""")
    return


@app.cell
def _(arr1, np):
    print(np.all(np.isnan(arr1)))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Verificando se **todos** os valores em **cada linha** são `NaN`.""")
    return


@app.cell
def _(arr1, np):
    print(np.all(np.isnan(arr1), axis=1)) # use axis=0 para verificar as colunas
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## `any()`""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Funciona da mesma forma que o `all()`, mas verifica se **qualquer valor** atende a determinada **condição**.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Verificando se existe **ao menos um** `NaN` no array.""")
    return


@app.cell
def _(arr1, np):
    print(np.any(np.isnan(arr1)))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# `concatenate()`""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Você pode usar a função `concatenate()` para **combinar** dois ou mais arrays.""")
    return


@app.cell
def _(np):
    zeros = np.zeros(shape = (3,2))
    print(zeros)

    ones = np.ones(shape = (2,2))
    print(ones)
    return ones, zeros


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Concatenando `zeros` com algumas cópias de si mesmo, como **linhas** (empilhando, _row-wise_).""")
    return


@app.cell
def _(np, zeros):
    print(np.concatenate((zeros, zeros, zeros), axis=0))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Concatenando `zeros` e `ones` como **linhas**.""")
    return


@app.cell
def _(np, ones, zeros):
    print(np.concatenate((zeros, ones), axis=0))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    /// attention | Atenção!

    Ao concatenar arrays, eles devem ter exatamente o **mesmo formato, excluindo o eixo ao longo do qual você está concatenando**. Por exemplo, se tentarmos concatenar `zeros` e `ones` como **colunas** (lado a lado, _column-wise_), o NumPy lançará um erro (excluindo o eixo das colunas, um array tem 3 e outro 2 linhas).
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# **Stacking**""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## **`vstack()`**""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    A função `vstack()` recebe um **argumento** - uma **tupla de arrays**. Você poderia **descrever seu algoritmo** em pseudocódigo como:

    ```
    Para cada array na tupla:
      Se o array for unidimensional:
        Promova o array para bidimensional, atribuindo a ele um novo eixo frontal.
      Se todos os arrays tiverem o mesmo formato:
        Concatene os arrays ao longo do eixo 0 (direção das linhas).
      Caso contrário:
        Lance um erro.
    ```
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Visualmente, você pode imaginar `vstack()` **empilhando verticalmente** arrays 1-d ou 2-d.""")
    return


@app.cell
def _(np):
    v1 = np.array(['a', 'b'])
    v2 = np.array(['c', 'd'])

    print(np.vstack((v1, v2)))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## **`hstack()`**""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    A **mesma lógica** do `vstack()`, só que coloca os arrays **lado a lado**.

    Temos ainda o `stack()`, no qual definimos se a **concatenação** será **vertical ou horizontal** com o argumento `axis.`
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# **Ordenação**""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Você pode usar a função `sort()` do NumPy para **ordenar** os elementos de um array. Ela tem três parâmetros principais:

    - `a`: o array que você deseja ordenar.
    - `axis`: o eixo ao longo do qual ordenar (`O` padrão, `-1`, ordena ao longo do último eixo).
    - `kind`: o tipo de ordenação que você deseja que o NumPy implemente. Por padrão, é usado o **quicksort**.

    Por exemplo, aqui criamos um array unidimensional, `ord1`, e o ordenamos em ordem crescente.
    """
    )
    return


@app.cell
def _(np):
    _ord1 = np.array([1, 7, 3, 9, 0, 9, 1])

    print('Array ordenado: ', np.sort(_ord1))
    print('Array original: ', _ord1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Note que o array **original não é modificado**.

    Se quisermos que a ordenação se dê **inplace**, podemos usar o **método de array** `sort()`.
    """
    )
    return


@app.cell
def _(np):
    _ord1 = np.array([1, 7, 3, 9, 0, 9, 1])
    _ord1.sort()

    print('Array ordenado: ', _ord1)
    print('Array original: ', _ord1) # original foi modificado
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    /// tip | Dica

    Se você tiver um array com valores `NaN`, o método `sort()` os coloca no **final** do array.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Infelizmente, o NumPy **não possui uma maneira direta** de classificar arrays em **ordem decrescente**. No entanto, existem algumas maneiras de fazer isso. Uma delas é usando o **fatiamento**.""")
    return


@app.cell
def _(np):
    _ord1 = np.array([1, 7, 3, 9, 0, 9, 1])

    print('Array em ordem reversa: ', np.sort(_ord1)[::-1])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## **`argsort()`**""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""A função `argsort()` funciona exatamente como `sort()`, exceto que ele **retorna um array de índices** indicando a posição para a qual cada valor do array seria mapeado caso ordenado.""")
    return


@app.cell
def _(np):
    ord2 = np.array([3, 0, 10, 5])

    print(np.argsort(ord2))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    O array retornado `argsort()` nos diz que:

    - o menor elemento de `ord2` está na posição 1.
    - o segundo menor elemento de `ord2` está na posição 0.
    - o terceiro menor elemento de `ord2` está na posição 3.
    - o quarto menor elemento de `ord2` está na posição 2.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# **`unique()`**""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Você pode usar a função `unique()` para obter os elementos únicos de um array, ou seja, para **desconsiderar duplicatas**.""")
    return


@app.cell
def _(np):
    arr3 = np.array(['b', 'b', 'a', 'a', 'c', 'c'])

    print(np.unique(arr3))
    return (arr3,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Você deve ter notado que "b" aparece primeiro em `arr3`, mas "a" aparece primeiro no output. Isso ocorre porque `unique()` retorna os elementos únicos **ordenados** de forma crescente por padrão.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Você pode usar o parâmetro `return_counts=True` para retornar a **contagem/frequência** de cada elemento único.""")
    return


@app.cell
def _(arr3, np):
    print(np.unique(arr3, return_counts=True))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Observe que isso nos retorna uma **tupla** em que o primeiro elemento é um array contém os elementos únicos ordenados, e o segundo as respectivas frequências.""")
    return


@app.cell
def _(arr3, np):
    uniques, freq = np.unique(arr3, return_counts=True)

    print(f'Freqências de {uniques}:  {freq}')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# **Desafios**""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## **Movie Ratings**""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Você recebe uma matriz 10x2 de floats, onde cada linha representa um filme. A primeira coluna representa a classificação do filme e a segunda coluna representa a classificação do diretor.""")
    return


@app.cell
def _(np):
    _generator = np.random.default_rng(123)
    ratings = np.round(_generator.uniform(low=0.0, high=10.0, size=(10, 2)))
    ratings[[1,2,7,9], [0,0,0,0]] = np.nan

    print(ratings)
    return (ratings,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Crie uma terceira coluna que represente a classificação geral. A classificação geral é igual à classificação do filme, se houver, caso contrário, à classificação do diretor.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### **My Try** 👽""")
    return


@app.cell
def _(np, ratings):
    _resultado = np.hstack(
        (
            ratings,
            np.where(~np.isnan(ratings[:, 0]), ratings[:, 0], ratings[:, 1])[:, np.newaxis]
        )
    )

    print('Resultado:\n', _resultado)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    /// details | **Explicação**
        type: info

        **[1]**: Usamos um `isnan()` invertido para selecionar os valores da "primeira coluna" qua não são `NaN`.<br>
        **[2]**: O `where()` retornará um array 1-d, logo, precisamos adicionar 1 eixo ele com `[:, np.newaxis]` para podermos concatená-lo horizontalmente com o `hstack()` ao original.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## **Taco Truck**""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Você possui um food truck de tacos aberto 24 horas por dia, 7 dias por semana, e gerencia cinco funcionários que o administram. Os funcionários trabalham sozinhos em turnos de oito horas. Você decide que a melhor maneira de definir a agenda deles para a semana seguinte é criar várias agendas aleatórias e selecionar a que melhor lhe parecer.

    Você cria um array de 1000x21 de IDs aleatórios de funcionários, onde o elemento (i,j) fornece o ID do funcionário que trabalha no turno j para o horário i.
    """
    )
    return


@app.cell
def _(np):
    _generator = np.random.default_rng(999)
    schedules = _generator.integers(low=0, high=5, size=(1000, 21))

    print(schedules)
    return (schedules,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Uma escala é válida desde que nenhum funcionário trabalhe em dois turnos consecutivos. Obtenha os índices de linha de todas as escalas válidas.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### **My Try** 👿""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### **Solution**""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Não consegui desenvolver.""")
    return


@app.cell
def _(np, schedules):
    is_valid = np.all(schedules[:, :-1] != schedules[:, 1:], axis=1)
    _resultado = np.nonzero(is_valid)[0]

    print('Resultado: ', _resultado)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    /// details | **Explicação**
        type: info
    
        **[1]**: Comparamos os valores da primeira à penúltima linha com os valores da segunda à última para encontrar as linhas em que todos os pares de valores adjascentes são distintos. Isso retornará um array de booleanos com 1000 posições. Cada valor indica se a linha satisfaz ou não a condição.<br>
        **[2]**: A função `npnonzero()` retorna os índices dos valore `True` (`0 == False`, `1 == True`).
    """
    )
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
