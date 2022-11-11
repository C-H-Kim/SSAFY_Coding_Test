if __name__ == '__main__':
    T = int(input())

    for test_case in range(1, T + 1):
        date = input()

        year = int(date[:4])
        month = int(date[4:6])
        day = int(date[6:])

        if month in [1, 3, 5, 7, 8, 10, 12]:
            if day < 0 or day > 31:
                print(f"#{test_case} -1")
            else:
                print("#%d %04d/%02d/%02d" % (test_case, year, month, day))
        elif month in [4, 6, 9, 11]:
            if day < 0 or day > 30:
                print(f"#{test_case} -1")
            else:
                print("#%d %04d/%02d/%02d" % (test_case, year, month, day))
        elif month == 2:
            if day < 0 or day > 28:
                print(f"#{test_case} -1")
            else:
                print("#%d %04d/%02d/%02d" % (test_case, year, month, day))
        else:
            print(f"#{test_case} -1")