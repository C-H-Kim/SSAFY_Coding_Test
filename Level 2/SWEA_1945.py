if __name__ == '__main__':
    T = int(input())

    for test_case in range(1, T + 1):
        N = int(input())

        divisor_cnt = [0] * 5
        divisor = [2, 3, 5, 7, 11]

        for i in range(5):
            while N % divisor[i] == 0:
                N = N // divisor[i]
                divisor_cnt[i] += 1

        print(f"#{test_case}", end=' ')
        for i in divisor_cnt:
            print(f"{i}", end=' ')
        print()