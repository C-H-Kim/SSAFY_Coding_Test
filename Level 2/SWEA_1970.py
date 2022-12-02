T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    dividend = N
    divisor = 50000
    divisor_cnt = 0
    output_str = ''

    while divisor != 5:
        cnt = dividend // divisor
        dividend = dividend % divisor

        output_str = output_str + str(cnt) + " "

        if divisor_cnt % 2 == 0:
            divisor = divisor // 5
        else:
            divisor = divisor // 2

        divisor_cnt += 1

    print(f"#{test_case}")
    print(f"{output_str}")