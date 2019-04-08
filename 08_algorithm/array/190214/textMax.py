import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
# sys.stderr = open('error.txt', 'w')

T = int(input())
for test_case in range(T):
    N = int(input())
    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))
    print(N)
    print(arr)

T = int(input())
for test_case in range(T):
    N, arr = input().split()
    N = int(N)
    print(N, arr)

T = int(input())
for test_case in range(T):
    N = int(input())
    arr = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        tmp = input()
        for j in range(N):
            arr[i][j] = int(tmp[j])
    print(N)
    print(arr)
