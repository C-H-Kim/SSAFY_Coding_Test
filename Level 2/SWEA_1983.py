def find_index(k_score, sort_list):
    idx = 0
    for i in sort_list:
        if k_score == i:
            break
        idx += 1
    return idx


def designate_grade(idx, bundle_num):
    if idx // bundle_num == 0:
        grade = 'A+'
    elif idx // bundle_num == 1:
        grade = 'A0'
    elif idx // bundle_num == 2:
        grade = 'A-'
    elif idx // bundle_num == 3:
        grade = 'B+'
    elif idx // bundle_num == 4:
        grade = 'B0'
    elif idx // bundle_num == 5:
        grade = 'B-'
    elif idx // bundle_num == 6:
        grade = 'C+'
    elif idx // bundle_num == 7:
        grade = 'C0'
    elif idx // bundle_num == 8:
        grade = 'C-'
    else:
        grade = 'D0'
    return grade


if __name__ == '__main__':
    T = int(input())

    for test_case in range(1, T + 1):
        N, K = map(int, input().split())

        score = []
        for _ in range(N):
            mid, final, assign = map(int, input().split())

            total_score = mid * 0.35 + final * 0.45 + assign * 0.2
            score.append(total_score)

        sort_score = sorted(score, reverse=True)

        index = find_index(score[K - 1], sort_score)

        group_num = N // 10
        K_grade = designate_grade(index, group_num)

        print(f"#{test_case} {K_grade}")