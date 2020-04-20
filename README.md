# mypy-experiments

Experiments of mypy

## Setup

I'm using pyenv (of anyenv) and miniconda:

```shell
pyenv install miniconda3-4.7.12
pyenv local miniconda3-4.7.12
conda create -n mypy python==3.8.2 pandas mypy pytest
```

By the commands above, the following libraries are installed:

- pandas: 1.0.3
- mypy: 0.770
- pytest: 5.4.1

The crated conda env can be directly activated by pyenv.

## Reference in Japanese (参考文献)

- Python 標準ライブラリ, 開発ツール, typing --- 型ヒントのサポート: https://docs.python.org/ja/3/library/typing.html
- PEP 483 -- The Theory of Type Hints: https://www.python.org/dev/peps/pep-0483
- PEP 484 -- Type Hints: https://www.python.org/dev/peps/pep-0484
- Mypy, Welcome to Mypy documentation!: https://mypy.readthedocs.io/en/latest/index.html

## 基本的な使い方

`mypy` は Python の gradual-typing ベースの型判定/型推論ツールである。推論は単純なものに限られる。

まずはこれで厳し目にチェックするとよいと思う。

```bash
mypy --strict --pretty <file or module or package>
```

## 依存ライブラリの型情報について

たとえば `mypy` インストール後のデフォルト状態で、Pandas を import するようなプログラムはエラーになる。

```bash
$ mypy --strict --pretty  .
dataframe.py:1: error: Skipping analyzing 'pandas': found module but no type hints or library stubs
    from pandas import DataFrame
    ^
dataframe.py:1: note: See https://mypy.readthedocs.io/en/latest/running_mypy.html#missing-imports
Found 1 error in 1 file (checked 2 source files)
```

エラーを避けるためには、メッセージにあるように、提供されている型ヒントかスタブをインストールする必要がある。
