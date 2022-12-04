def snail(row, col, num):
    global maximum, visited, board, N

    if num > maximum:
        return

    #오른쪽으로 이동
    for i in range(1, N + 1):
        if col + i < N and not visited[row][col + i]:
            board[row][col + i] = num
            visited[row][col + i] = True
            num += 1
        else:
            col = col + i - 1
            break

    #아래쪽으로 이동
    for i in range(1, N + 1):
        if row + i < N and not visited[row + i][col]:
            board[row + i][col] = num
            visited[row + i][col] = True
            num += 1
        else:
            row = row + i - 1
            break


    #왼쪽으로 이동
    for i in range(1, N + 1):
        if col - i >= 0 and not visited[row][col - i]:
            board[row][col - i] = num
            visited[row][col - i] = True
            num += 1
        else:
            col = col - i + 1
            break

    #윗쪽으로 이동
    for i in range(1, N + 1):
        if row - i >= 0 and not visited[row - i][col]:
            board[row - i][col] = num
            visited[row - i][col] = True
            num += 1
        else:
            row = row - i + 1
            break

    snail(row, col, num)


if __name__ == '__main__':
    T = int(input())

    for test_case in range(1, T + 1):
        N = int(input())

        maximum = N * N
        visited = [[False] * N for _ in range(N)]
        board = [[0] * N for _ in range(N)]

        board[0][0] = 1
        visited[0][0] = True

        snail(0, 0, 2)

        print(f"#{test_case}")
        for row in board:
            print(*row)
