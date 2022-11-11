if __name__ == '__main__':
    T = int(input())

    for test_case in range(1, T + 1):
        num_list = list(map(int, input().split()))

        a = num_list[0]
        b = num_list[1]

        print(f"#{test_case} {a // b} {a % b}")