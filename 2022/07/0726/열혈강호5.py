import sys
from collections import deque
sys.stdin = open('./text/11408.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()

INF = sys.maxsize
X, Y = Split()
S = X + Y
E = X + Y + 1
N = X + Y + 2
C = [[0] * (N) for _ in range(N)]
F = [[0] * (N) for _ in range(N)]
W = [[0] * (N) for _ in range(N)]
graph = [[] for _ in range(N)]
count = 0
total = [0]
for i in range(X):
    C[S][i] = 1
    graph[S].append(i)
    graph[i].append(S)
for i in range(Y):
    C[i + X][E] = 1
    graph[i + X].append(E)
    graph[E].append(i + X)

for i in range(X):
    temp = List()
    jobs = [temp[i:i + 2] for i in range(1, len(temp), 2)]
    for job in jobs:
        j, c = job
        j -= 1
        C[i][j + X] = 1
        W[i][j + X] = c
        W[j + X][i] = -c
        graph[i].append(j + X)
        graph[j + X].append(i)

def SPFA():
    Q = deque([S])
    prev = [-1] * (X + Y + 2)
    dp = [INF] * (X + Y + 2)
    dp[S] = 0
    inQ = [False] * (X + Y + 2)
    inQ[S] = True
    while Q:
        x = Q.popleft()
        inQ[x] = False
        for v in graph[x]:
            if C[x][v] - F[x][v] > 0 and dp[v] > dp[x] + W[x][v]:
                dp[v] = dp[x] + W[x][v]
                prev[v] = x
                if not inQ[v]:
                    Q.append(v)
                    inQ[v] = True
    return prev

result = 0
while True:
    prev = SPFA()
    if prev[E] == -1:
        break
    flow = INF
    x = E
    while x != S:
        flow = min(flow, C[prev[x]][x] - F[prev[x]][x])
        x = prev[x]
    x = E
    while x != S:
        result += flow * W[prev[x]][x]
        F[prev[x]][x] += flow
        F[x][prev[x]] -= flow
        x = prev[x]
    count += 1

print(count)
print(result)