if __name__ == '__main__':
    T = int(input())

    for test_case in range(1, T + 1):
        first_hour, first_min, second_hour, second_min = map(int, input().split())

        hour = first_hour + second_hour
        min = first_min + second_min

        if min > 59:
            min -= 60
            hour += 1

        if hour > 12:
            hour -= 12

        print(f"#{test_case} {hour} {min}")