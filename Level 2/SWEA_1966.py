T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    num_list = list(map(int, input().split()))
    num_list = sorted(num_list)

    print(f"#{test_case}", end=' ')

    for i in num_list:
        print(f"{i}", end=' ')

    print()