if __name__ == '__main__':
    N = int(input())

    num_list = list(map(int, input().split()))
    num_list.sort()

    print(num_list[int(N/2)])