def check_divisor(num, N):
    if N % num == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    N = int(input())

    for i in range(1, N + 1):
        if(check_divisor(i, N)):
            print(i, end=' ')