if __name__ == '__main__':
    T = int(input())

    #dr -> delta row : 우 하 좌 상으로 움직일 때 행에 더해주는 인덱스
    #dc -> delta col : 우 하 좌 상으로 움직일 때 열에 더해주는 인덱스
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    for test_case in range(1, T + 1):
        N = int(input())
        #row, col은 0,0부터 시작
        r = 0
        c = 0
        #direction은 방향을 설정해주는 변수 -> 0, 1, 2, 3 순서로 우 하 좌 상을 의미
        direction = 0

        board = [[0] * N for _ in range(N)]

        for n in range(1, N * N + 1):
            board[r][c] = n
            r += dr[direction]
            c += dc[direction]

            if r < 0 or c < 0 or r >= N or c >= N or board[r][c] != 0:
                r -= dr[direction]
                c -= dc[direction]

                direction = (direction + 1) % 4

                r += dr[direction]
                c += dc[direction]

        print(f"#{test_case}")
        for row in board:
            print(*row)
