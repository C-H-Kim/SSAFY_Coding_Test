if __name__ == '__main__':
    T = int(input())

    for test_case in range(1, T + 1):
        num_list = list(map(int, input().split()))

        num_list.remove(max(num_list))
        num_list.remove(min(num_list))

        avg = sum(num_list) / len(num_list)
        avg = round(avg)

        print(f"#{test_case} {avg}")