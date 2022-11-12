if __name__ == '__main__':
    T = int(input())

    for test_case in range(1, T + 1):
        N = int(input())

        sum = 0
        for i in range(1, N + 1):
            if i % 2 == 1:
                sum += i
            else:
                sum -= i

        print(f"#{test_case} {sum}")