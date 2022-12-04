if __name__ == '__main__':
    T = int(input())

    for test_case in range(1, T + 1):
        N = int(input())

        num_flag = [False] * 10
        i = 1
        while True:
            temp_num = N * i

            while temp_num != 0:
                index = temp_num % 10
                temp_num = temp_num // 10
                num_flag[index] = True

            if False not in num_flag:
                break
            else:
                i += 1

        print(f"#{test_case} {N * i}")
