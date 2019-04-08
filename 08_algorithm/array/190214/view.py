import sys
sys.stdin = open('input.txt', 'r')


for test_case in range(10):
    N = int(input())
    arr = list(map(int, input().split()))
    print(N)
    print(arr)

    count = 0

    for i in range(2, len(arr) - 2):
        max_val = arr[i]

        if arr[i - 2] > arr[i - 1]:
            left_max_val = arr[i - 2]
        else:
            left_max_val = arr[i - 1]

        if arr[i + 1] > arr[i + 2]:
            right_max_val = arr[i + 1]
        else:
            right_max_val = arr[i + 2]

        if left_max_val > right_max_val:
            if max_val > left_max_val:
                count += max_val - left_max_val
        else:
            if max_val > right_max_val:
                count += max_val - right_max_val

    print(f'#{test_case +1} {count}')
