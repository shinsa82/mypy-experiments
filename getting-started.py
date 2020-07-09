from typing import Iterable, List


def greeting(name: str) -> str:
    return 'Hello ' + name


greeting(3)
greeting(b'Alice')


def p() -> None:
    print('hello')


a = p()


def f():
    1 + 'x'  # No static type error (dynamically typed)


def g() -> None:
    1 + 'x'  # Type check error (statically typed)


def greeting2(name: str, excited: bool = False) -> str:
    message = 'Hello, {}'.format(name)
    if excited:
        message += '!!!'
    return message


greeting2('test', 1)
greeting2('test', False)
greeting2('test', name='test')


def stars(*args: int, **kwargs: float) -> None:
    # 'args' has type 'Tuple[int, ...]' (a tuple of ints)
    # 'kwargs' has type 'Dict[str, float]' (a dict of strs to floats)
    for arg in args:
        print(arg)
    for key, value in kwargs:
        print(key, value)


def greet_all(names: List[str]) -> None:
    for name in names:
        print('Hello ' + name)


names = ["Alice", "Bob", "Charlie"]
ages = [10, 20, 30]

greet_all(names)   # Ok!
greet_all(ages)    # Error due to incompatible types


def greet_all2(names: Iterable[str]) -> None:
    for name in names:
        print('Hello ' + name)
