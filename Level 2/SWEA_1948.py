if __name__ == '__main__':
    T = int(input())

    for test_case in range(1, T + 1):
        m1, d1, m2, d2 = map(int, input().split())

        day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        count = 0

        for i in range(m1, m2):
            count += day[i - 1]

        count = count - d1 + d2 + 1

        print(f"#{test_case} {count}")