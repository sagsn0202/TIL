import sys
sys.stdin = open('numbercard_input.txt', 'r')
sys.stdout = open('numbercard_output.txt', 'w')

T = int(input())
for test_case in range(T):
    N = int(input())
    arr = list(map(int, filter(str.isdigit, input())))
    print(N)
    print(arr)

    prev_cnt = 0
    curr_cnt = 0
    for idx in range(10):
        for val in arr:
            if idx == val:
                curr_cnt += 1
        if prev_cnt <= curr_cnt:
            std = idx
            prev_cnt = curr_cnt
        curr_cnt = 0

    print(f'#{test_case + 1} {std} {prev_cnt}')
