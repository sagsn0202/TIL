import sys
sys.stdin = open('flatten_input.txt', 'r')
sys.stdout = open('flatten_output.txt', 'w')

for test_case in range(10):
    N = int(input())
    arr = list(map(int, input().split()))

    new_arr = [0] * 100
    for val in arr:
        new_arr[val - 1] += 1

    box = 0
    for i in range(99, -1, -1):
        if new_arr[i] >= 1:
            if N - new_arr[i] < 0:
                start = i
                break
            else:
                new_arr[i - 1] += new_arr[i]
                box += new_arr[i]
                N -= new_arr[i]
                new_arr[i] = 0

    box += N
    for i in range(100):
        if new_arr[i] >= 1:
            if box - new_arr[i] < 0:
                end = i
                break
            else:
                new_arr[i + 1] += new_arr[i]
                box -= new_arr[i]
                new_arr[i] = 0

    print(f'#{test_case + 1} {start - end}')
