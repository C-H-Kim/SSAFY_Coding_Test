if __name__ == '__main__':
    T = int(input())

    for test_case in range(1, T + 1):
        N = int(input())
        N_list = list(map(int, input().split()))

        max_value = N_list[-1]
        profit = 0
        for idx in range(N-2, -1, -1):
            if N_list[idx] > max_value:
                max_value = N_list[idx]
            else:
                profit += max_value - N_list[idx]

        print(f"#{test_case} {profit}")