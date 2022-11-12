if __name__ == '__main__':
    T = int(input())

    for test_case in range(1, T + 1):
        string = input()
        word = ''
        for char in string:
            word += char
            word_len = len(word)
            if word == string[word_len:2 * word_len]:
                rest = string[word_len:]
                rest = rest.replace(word, '')
                if len(rest) < word_len:
                    break

        print(f"#{test_case} {word_len}")