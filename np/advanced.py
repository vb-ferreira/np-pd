import marimo

__generated_with = "0.14.17"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# **Indexação avançada**""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Anteriormente, discutimos técnicas básicas de indexação de arrays. Aqui, discutiremos técnicas avançadas e nos aprofundaremos em como a indexação de arrays funciona.

    Começamos configurando um array 3x2x4 de inteiros, `arr_teste1`.
    """
    )
    return


@app.cell
def _(np):
    arr_teste1 = np.arange(3*2*4).reshape((3, 2, 4))
    print(arr_teste1)
    return (arr_teste1,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Neste caso, podemos pensar em `arr_teste1` como uma linha de arrays onde o elemento (i,j,k) corresponde à: `i` (array, 0 a 2), `j` (linha, 0 a 1) e `k` (coluna, 0 a 3). 

    Logo, `arr_teste1[:, :, 0]` solicita "cada matriz, cada linha, coluna 0", resultando no subarray a seguir.
    """
    )
    return


@app.cell
def _(arr_teste1):
    print(arr_teste1[:, :, 0])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    /// attention | Aviso

    Estaa seção não foi propriamente explorada.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# **View vs Copy**""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    É importante entender quando a indexação de arrays produz uma **view** e quando produz uma **cópia**.

    Suponha que temos este array 2D, `arr_test2`.
    """
    )
    return


@app.cell
def _(np):
    arr_test2 = np.arange(12).reshape(3, -1)
    print(arr_test2)
    return (arr_test2,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    /// tip | Dica

    O valor `-1` serve como um coringa para a dimensão do array. Ele instrui o NumPy a **calcular automaticamente** o **tamanho** dessa **dimensão**, com base no número total de elementos e nas outras dimensões especificadas.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Podemos **selecionar** as duas primeiras colunas usando **indexing** ou **slicing**.""")
    return


@app.cell
def _(arr_test2):
    first2Cols1 = arr_test2[:, [0,1]]
    first2Cols2 = arr_test2[:, :2]
    return first2Cols1, first2Cols2


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""À primeira vista, essas técnicas parecem produzir o mesmo resultado:""")
    return


@app.cell
def _(first2Cols1, first2Cols2, np):
    print(np.all(first2Cols1 == first2Cols2))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Mas, por baixo dos panos, essas técnicas são **sutilmente diferentes**. `first2Cols1` é uma **cópia** de `arr_test2`, enquanto `first2Cols2` é uma **view** de `arr_test2`.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    /// attention | Atenção

    Se modificarmos uma **cópia**, **o original não é alterado**. Se modificarmos uma **view**, **o original é alterado**.

    Em geral, quando você subdivide um array usando **apenas slicing**, o NumPy **retorna uma view** do array original. Você pode **forçar** o NumPy a copiar os dados usando o método `copy()` do array.
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
