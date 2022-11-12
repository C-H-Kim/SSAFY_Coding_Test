def find_sum(i, j, area, M):
    sum = 0
    for a in range(M):
        for b in range(M):
            sum += area[i + a][j + b]
    return sum

if __name__ == '__main__':
    T = int(input())

    for test_case in range(1, T + 1):
        N, M = map(int, input().split())

        area = []
        for i in range(N):
            area.append(list(map(int, input().split())))

        row_col = N - (M - 1)

        sum_list = []
        for i in range(row_col):
            for j in range(row_col):
                sum = find_sum(i, j, area, M)
                sum_list.append(sum)

        max_sum = max(sum_list)

        print(f"#{test_case} {max_sum}")