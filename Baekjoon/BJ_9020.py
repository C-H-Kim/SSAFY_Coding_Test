def is_prime(n):
    arr = [True] * (n + 1)
    arr[0] = arr[1] = False

    for i in range(2, n + 1):
        if arr[i]:
            j = 2

            while i * j <= n:
                arr[i * j] = False
                j += 1

    return arr


if __name__ == '__main__':
    arr = is_prime(10000)
    T = int(input())

    for test_case in range(T):
        N = int(input())
        a = N // 2
        b = N // 2

        while True:
            if arr[a] and arr[b]:
                print(f"{a} {b}")
                break
            a -= 1
            b += 1