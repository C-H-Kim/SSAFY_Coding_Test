if __name__ == '__main__':
    T = int(input())

    for test_case in range(1, T + 1):
        num_list = list(map(int, input().split()))
        max = -1
        for i in num_list:
            if i > max:
                max = i
        print(f"#{test_case} {max}")