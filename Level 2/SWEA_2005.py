if __name__ == '__main__':
    T = int(input())

    for test_case in range(1, T + 1):
        N = int(input())

        print(f"#{test_case}")
        temp_list = []
        for i in range(1, N + 1):
            prev_list = temp_list
            if i == 1:
                print(f"1", end='')
            else:
                temp_list = []

                temp_list.append(1)
                for j in range(1, i - 1):
                    temp_list.append(prev_list[j - 1] + prev_list[j])
                temp_list.append(1)

                for val in temp_list:
                    print(val, end=' ')
            print()