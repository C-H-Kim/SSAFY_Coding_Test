def promising(cdx):
    global board

    for i in range(cdx):
        if board[cdx] == board[i] or cdx - i == abs(board[cdx] - board[i]):
            return False

    return True


def nqueen(cdx):
    global count
    global N
    global board

    if cdx == N:
        count += 1
        return

    for i in range(N):
        board[cdx] = i
        if promising(cdx):
            nqueen(cdx + 1)

    return


if __name__ == '__main__':
    T = int(input())

    for test_case in range(1, T + 1):
        N = int(input())
        count = 0
        board = [0] * N

        nqueen(0)

        print(f"#{test_case} {count}")