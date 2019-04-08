import sys
sys.stdin = open('sectionsum_input.txt', 'r')
sys.stdout = open('sectionsum_output.txt', 'w')

T = int(input())
for test_case in range(T):
    N, M = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    print(N, M)
    print(arr)

    min_sum = 0
    max_sum = 0
    curr_sum = 0
    for i in range(len(arr) - M + 1):
        for j in range(M):
            curr_sum += arr[i + j]
        if curr_sum > max_sum:
            max_sum = curr_sum
        if min_sum == 0 or curr_sum < min_sum:
            min_sum = curr_sum
        curr_sum = 0

    print(f'#{test_case + 1} {max_sum - min_sum}')
