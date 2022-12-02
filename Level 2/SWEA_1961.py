def rotation(arr, N):
    temp_arr = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            temp_arr[i][j] = arr[N - 1 - j][i]
    return temp_arr


if __name__ == '__main__':
    T = int(input())

    for test_case in range(1, T + 1):
        N = int(input())

        origin_arr = [list(map(int, input().split())) for _ in range(N)]

        arr_90 = rotation(origin_arr, N)
        arr_180 = rotation(arr_90, N)
        arr_270 = rotation(arr_180, N)

        print(f"#{test_case}")

        for i in range(N):
            print("".join(map(str, arr_90[i])), end=" ")
            print("".join(map(str, arr_180[i])), end=" ")
            print("".join(map(str, arr_270[i])), end=" ")
            print()
