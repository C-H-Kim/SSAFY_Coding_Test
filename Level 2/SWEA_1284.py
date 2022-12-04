if __name__ == '__main__':
    T = int(input())

    for test_case in range(1, T + 1):
        #P -> A사 1L당 요금
        #Q -> B사 R리터 이하 요금 / R -> B사 누진세 기준 / S -> R리터 초과량에 대한 1L당 요금
        #W -> 사용한 수도의 양
        P, Q, R, S, W = map(int, input().split())

        A = P * W

        if R < W:
            B = Q + (W - R) * S
        else:
            B = Q

        print(f"#{test_case} {min(A, B)}")