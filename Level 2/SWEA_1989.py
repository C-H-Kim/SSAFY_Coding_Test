if __name__ == '__main__':
    T = int(input())

    for test_case in range(1, T + 1):
        word = input()
        length = len(word)
        pivot = length // 2

        flag = 1
        for i in range(pivot):
            if word[i] == word[length - 1 - i]:
                continue
            else:
                flag = 0
                break

        print(f"#{test_case} {flag}")