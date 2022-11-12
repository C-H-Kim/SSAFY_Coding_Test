def num_check(num):
    count = 0
    flag = False
    while num != 0:
        digit = num % 10
        num = num // 10
        if digit == 3 or digit == 6 or digit == 9:
            count += 1

    if count >= 1:
        flag = True

    return flag, count

if __name__ == '__main__':
    N = int(input())

    for i in range(1, N + 1):
        flag, count = num_check(i)

        if flag:
            for j in range(count):
                print('-', end='')
            print(end=' ')
        else:
            print(i, end=' ')