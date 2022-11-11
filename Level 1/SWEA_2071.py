if __name__ == '__main__':
    T = int(input())

    for test_case in range(1, T + 1):
        num_list = list(map(int, input().split()))
        avg = int(round(sum(num_list) / len(num_list), 0))
        print(f"#{test_case} {avg}")