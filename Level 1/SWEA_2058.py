if __name__ == '__main__':
    N = input()
    digit_list = list(N)

    sum = 0
    for i in digit_list:
        sum += int(i)

    print(sum)