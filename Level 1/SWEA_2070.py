if __name__ == '__main__':
    T = int(input())

    for test_case in range(1, T + 1):
        numbers = list(map(int, input().split()))

        if numbers[0] < numbers[1]:
            sign = '<'
        elif numbers[0] == numbers[1]:
            sign = '='
        else:
            sign = '>'

        print(f"#{test_case} {sign}")