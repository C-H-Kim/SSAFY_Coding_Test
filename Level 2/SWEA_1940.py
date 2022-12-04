if __name__ == '__main__':
    T = int(input())

    for test_case in range(1, T + 1):
        N = int(input())

        cur_speed = 0
        distance = 0
        for _ in range(N):
            command = list(map(int, input().split()))

            if command[0] == 1:
                cur_speed += command[1]
            elif command[0] == 2:
                cur_speed -= command[1]

                if cur_speed < 0:
                    cur_speed = 0
            else:
                pass

            distance += cur_speed

        print(f"#{test_case} {distance}")