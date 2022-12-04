if __name__ == '__main__':
    T = int(input())

    for test_case in range(1, T + 1):
        N = int(input())

        char_list = [list(map(str, input().split())) for _ in range(N)]
        count = 1

        print(f"#{test_case}")
        for _ in range(N):
            iteration = int(char_list[0][1])
            for _ in range(iteration):
                print(char_list[0][0], end='')
                count += 1

                if count > 10:
                    print()
                    count = 1

            char_list.pop(0)

        print()
