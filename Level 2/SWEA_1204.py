if __name__ == '__main__':
    T = int(input())

    for test_case in range(1, T + 1):
        N = int(input())
        num_list = list(map(int, input().split()))

        num_freq = [0] * 101
        max_freq = 0
        for i in num_list:
            num_freq[i] += 1

            if max_freq <= num_freq[i]:
                max_freq = num_freq[i]
                max_freq_score = i

        print(f"#{test_case} {max_freq_score}")