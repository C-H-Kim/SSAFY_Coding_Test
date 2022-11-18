if __name__ == '__main__':
    T = 10

    for test_case in range(1, T + 1):
        N = int(input())

        buildings = list(map(int, input().split()))
        count_sum = 0
        for i in range(2, N - 2):
            near_max_height = max(buildings[i - 2], buildings[i - 1], buildings[i + 1], buildings[i + 2])
            if near_max_height < buildings[i]:
                count_sum = count_sum + buildings[i] - near_max_height

        print(f"#{test_case} {count_sum}")