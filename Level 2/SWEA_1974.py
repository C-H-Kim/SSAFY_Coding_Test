if __name__ == '__main__':
    T = int(input())

    for test_case in range(1, T + 1):
        board = []
        for i in range(9):
            board.append(list(map(int, input().split())))

        flag = True

        #행 검사
        for i in range(9):
            arr = [False] * 10
            arr[0] = True

            for j in range(9):
                if not arr[board[i][j]]:
                    arr[board[i][j]] = True
                else:
                    break

            if False in arr:
                flag = False
                break

        #열 검사
        for j in range(9):
            arr = [False] * 10
            arr[0] = True

            for i in range(9):
                if not arr[board[i][j]]:
                    arr[board[i][j]] = True
                else:
                    break

            if False in arr:
                flag = False
                break

        #칸 검사
        for i in range(3):
            for j in range(3):
                arr = [False] * 10
                arr[0] = True

                for a in range(3):
                    for b in range(3):
                        if not arr[board[i * 3 + a][j * 3 + b]]:
                            arr[board[i * 3 + a][j * 3 + b]] = True
                        else:
                            break

                if False in arr:
                    flag = False
                    break

            if not flag:
                break

        if flag:
            print(f"#{test_case} 1")
        else:
            print(f"#{test_case} 0")