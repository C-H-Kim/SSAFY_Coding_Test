if __name__ == '__main__':
    nums = list(map(int, input().split()))
    P = int(nums[0])
    K = int(nums[1])

    count = 1
    while K != P:
        K += 1
        count += 1

    print(count)