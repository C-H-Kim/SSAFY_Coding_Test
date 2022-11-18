if __name__ == '__main__':
    T = 10

    for test_case in range(1, T + 1):
        dump = int(input())
        box = list(map(int, input().split()))

        for i in range(dump):
            box = sorted(box)
            box[0] += 1
            box[99] -= 1

        diff = max(box) - min(box)

        print(f"#{test_case} {diff}")