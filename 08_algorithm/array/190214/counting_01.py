k = 4
arr = [0, 4, 1, 3, 1, 2, 4, 1]
cnt = [0] * (k + 1)
sor = [0] * len(arr)

for i in arr:
    cnt[i] += 1
print(cnt)

for i in range(len(cnt) - 1):
    cnt[i + 1] += cnt[i]
print(cnt)

for i in range(len(arr) - 1, -1, -1):
    cnt[arr[i]] -= 1
    sor[cnt[arr[i]]] = arr[i]
print(sor)
