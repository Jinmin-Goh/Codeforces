# Contest No.: 663
# Problem No.: A
# Solver:      JEMINI
# Date:        20200809

import sys
import heapq

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        ans = [0] * n
        for i in range(n // 2):
            ans[i] = n - 2 * i
            ans[-1 - i] = n - (2 * i + 1)
        if n % 2:
            ans[n // 2] = 1
        for i in ans:
            print(i, end = " ")
        print("")

    return

if __name__ == "__main__":
    main()