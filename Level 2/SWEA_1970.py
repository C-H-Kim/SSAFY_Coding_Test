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

        #나누는 수의 맨 앞자리가 5이면 5로 나눈다. -> 다음 나누는 수는 이전 나누는 수의 1/5이기 때문
        if divisor_cnt % 2 == 0:
            divisor = divisor // 5
        #나누는 수의 맨 앞자리가 1이면 2로 나눈다. -> 다음 나누는 수는 이전 나누는 수의 절반이기 때문
        else:
            divisor = divisor // 2

        #나누는 수의 순서를 파악하기 위한 변수 +1
        divisor_cnt += 1

    print(f"#{test_case}")
    print(f"{output_str}")