def find_fibo(n):
    if n <= 2:
        return 1
    fib_x, fib_next = 1, 1
    i = 3
    while i <= n:
        i += 1
        fib_x, fib_next = fib_next, fib_x + fib_next
    return fib_next


def list_fib(n):
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    else:
        i = 3
        a, b = 1, 1
        _ = [1, 1]

        while i <= n:
            a, b = b , a + b
            i = i + 1
            _.append(b)
        return _

for x in range(1, 11):
    print(find_fibo(x))
if __name__ == "__main__":
    print(list_fib(1))
    print(list_fib(2))
    print(list_fib(10))