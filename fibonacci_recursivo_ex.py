def fibonacci(n):
    if n < 2:     # base da recursao
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)   # chamada recursiva