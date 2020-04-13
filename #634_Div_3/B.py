# Contest No.: 634
# Problem No.: B
# Solver:      JEMINI
# Date:        20200413

import sys

def main():
    t = int(input())
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for _ in range(t):
        n, a, b = map(int, sys.stdin.readline().split())
        ans = "a" * (a - b)
        ans += alphabet[:b]
        while len(ans) < n:
            ans += ans[-a]
        print(ans)
    return

if __name__ == "__main__":
    main()