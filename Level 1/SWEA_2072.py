if __name__ == '__main__':
    T = int(input())

    for test_case in range(1, T + 1):
        num_list = list(map(int, input().split()))
        odd_nums = [x for x in num_list if x % 2 == 1]
        print(f"#{test_case} {sum(odd_nums)}")