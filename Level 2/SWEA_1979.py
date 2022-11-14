if __name__ == '__main__':
    T = int(input())

    for test_case in range(1, T + 1):
        N, K = map(int, input().split())

        field = [list(map(int, input().split())) for _ in range(N)]

        result = 0
        for i in range(N):
            count = 1
            for j in range(N - 1):
                if field[i][j] and field[i][j + 1]:
                    count += 1
                else:
                    if count == K:
                        result += 1
                    count = 1

            if count == K:
                result += 1

        for j in range(N):
            count = 1
            for i in range(N - 1):
                if field[i][j] and field[i + 1][j]:
                    count += 1
                else:
                    if count == K:
                        result += 1
                    count = 1

            if count == K:
                result += 1

        print(f"#{test_case} {result}")