if __name__ == '__main__':
    alphabet = input()
    alphabet = list(alphabet)

    for i in alphabet:
        print(f"{ord(i) - 64}", end=' ')