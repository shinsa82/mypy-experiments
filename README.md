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
