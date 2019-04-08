import sys
sys.stdin = open('minmax_input.txt', 'r')
sys.stdout = open('minmax_output.txt', 'w')

T = int(input())
for test_case in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    min_num = arr[0]
    max_num = arr[0]

    for i in range(N):
        if arr[i] > max_num:
            max_num = arr[i]
        if arr[i] < min_num:
            min_num = arr[i]

    print(f'#{test_case + 1} {max_num - min_num}')
