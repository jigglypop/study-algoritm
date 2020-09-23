import sys
from math import ceil, log2
sys.stdin = open('11505.txt', 'r')
input = sys.stdin.readline

N, M, K = map(int, input().split())
board = [int(input())for _ in range(N)]
tree = [0] * (1 << ceil(log2(N))+1)


def init(node, start, end):
    if start == end:
        tree[node] = board[start]
    else:
        mid = (start + end) // 2
        init(2 * node, start, mid)
        init(2 * node + 1, mid + 1, end)
        tree[node] = tree[2 * node] * tree[2 * node + 1] % 1000000007


init(1, 0, N-1)


def update(node, start, end, index, value):
    if index < start or index > end:
        return
    if start == end:
        tree[node] = value
        return
    mid = (start + end) // 2
    update(2 * node, start, mid, index, value)
    update(2 * node + 1, mid+1, end, index, value)
    tree[node] = tree[2*node] * tree[2*node+1] % 1000000007


def query(node, start, end, s, e):
    if s > end or e < start:
        return -1
    if s <= start and end <= e:
        return tree[node]
    mid = (start + end) // 2
    left = query(2*node, start, mid, s, e)
    right = query(2*node + 1, mid+1, end, s, e)
    if left == -1:
        return right
    elif right == -1:
        return left
    else:
        return left * right


for _ in range(M+K):
    a, b, c = map(int, input().split())
    if a == 1:
        update(1, 0, N-1, b-1, c)
    if a == 2:
        print(query(1, 0, N-1, b-1, c-1) % 1000000007)
