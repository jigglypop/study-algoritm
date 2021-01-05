import sys
from pprint import pprint
sys.stdin = open('2240.txt', 'r')

input = sys.stdin.readline
S, W = map(int, input().split())
board = [0] + [int(input()) for _ in range(S)]
DP = [[-1] * (W+1) for _ in range(S+1)]


def go(s, w):
    if s == S + 1 and w <= W:
        return 0
    if w > W:
        return 0
    if DP[s][w] != -1:
        return DP[s][w]
    point = w % 2 + 1
    rest = 1 if point == board[s] else 0
    DP[s][w] = max(go(s+1, w+1), go(s+1, w)) + rest
    return DP[s][w]


print(max(go(1, 1), go(1, 0)))
