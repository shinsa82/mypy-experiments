# mypy-experiments

Experiments of mypy

## Setup

I use pyenv (of anyenv) and miniconda:

```bash
pyenv virtualenv miniconda3-latest mypy-experiments
pyenv local mypy-experiments
conda create -n mypy python==3.8.2 pandas mypy pytest autopep8
```

> `autopep8` is used by VSCode to format source.

At the time of writing, the following libraries are installed by the commands above:

- python: 3.8.3
- pandas: 1.0.5
- mypy: 0.782
- mypy_extensions: 0.4.3
- pytest: 5.4.3

The created conda env can be directly activated by `pyenv activate mypy-experiments`.
You may also need to execute `pyenv rehash` to set PATH correctly.

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

エラーを避けるためには、メッセージにあるように、提供されている型ヒントかスタブを作成またはインストールする必要がある。
作成したらこのように実行。

```bash
 MYPYPATH=stubs mypy dataframe.py --pretty
```

## Stub の自動生成 (stubgen)

`stubgen` は mypy に付属の stub 生成ツールである。
なぜか `-v` をつけないと正しく動かない。サブプロセスの生成に失敗してたので、pyenv + virtualenv と標準出力の相性かもしれない。

**なお、この生成したファイルでは mypy は通らない。**

```bash
stubgen -m pandas -o stubs -v
```

(ほんとうは `stubgen -p pandas` とするべきだったのかもしれない)

## Stub の手動作成

しょうがないので手動生成する。[stubs/pandas/__init__.pyi](stubs/pandas/__init__.pyi) に型定義を書き込む。
API ドキュメントの変数名と型に合わせて、適当に作成する。必要ない部分は `...` で省略する。

> この `...` は便宜上省略しているのではなくて Python の正当なトークンである。

```python
from typing import Any, List, Optional


class DataFrame:
    def __init__(self, data: Optional[List[Any]] = None): ...
```

これで、前述の mypy チェックが通る。
