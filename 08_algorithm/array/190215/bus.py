import sys
sys.stdin = open('bus_input.txt', 'r')
sys.stdout = open('bus_output.txt', 'w')

T = int(input())
for test_case in range(T):
    K, N, M = list(map(int, input().split()))
    stop = list(map(int, input().split()))

    bias = 0
    cnt = 0
    for i in range(N):
        if len(stop) == 0:
            break
        elif len(stop) == 1:
            stop.append(N)

        if K < stop[0] - bias:
            cnt = 0
            break
        elif stop[0] - bias <= K < stop[1] - bias:
            bias = stop[0]
            cnt += 1
            stop = stop[1:]
        elif stop[1] - bias == K:
            if stop[1] == N:
                break
            bias = stop[1]
            cnt += 1
            stop = stop[2:]
        else:
            stop = stop[1:]

    print(f'#{test_case + 1} {cnt}')
