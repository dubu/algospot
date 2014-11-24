__author__ = 'dubuapt'

from itertools import accumulate, islice

def solve(N, L, costs):
    return min(cost_total / n
               for i in range(N-L+1)
               for n, cost_total
               in enumerate(islice(accumulate(costs[i:]), i+L-1, None), L)
    )

def main():
    C = int(input())
    for _ in range(C):
        N, L = map(int, input().split())
        costs = tuple(map(int, input().split()))
        print(solve(N, L, costs))

main()

