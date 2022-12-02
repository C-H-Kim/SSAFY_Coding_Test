if __name__ == '__main__':
    T = int(input())

    for test_case in range(1, T + 1):
        N, M = map(int, input().split())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))

        end = abs(M - N)

        sum_list = []
        if N < M:
            for i in range(end + 1):
                sum = 0
                for j in range(N):
                    sum += A[j] * B[i + j]
                sum_list.append(sum)
        else:
            for i in range(end + 1):
                sum = 0
                for j in range(M):
                    sum += A[i + j] * B[j]
                sum_list.append(sum)

        print(f"#{test_case} {max(sum_list)}")
