from functools import cache


@cache
def fibonacci(num: str) -> int:
    if num <= 0:
        return 0
    elif num <= 2:
        return num - 1
    return fibonacci(num-1) + fibonacci(num-2)


print(fibonacci(40))
