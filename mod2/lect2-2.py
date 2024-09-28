def fibonacci(n):
    return 1 if n in (1,2) else (fibonacci(n - 1) + fibonacci(n - 2))


if __name__ == "__main__":
    print(fibonacci(int(input())))
