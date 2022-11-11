if __name__ == '__main__':
    A, B = map(int, input().split())

    if A - B == -1 or A - B == 2:
        print("B")
    elif A - B == 1 or A - B == -2:
        print("A")
    else:
        pass