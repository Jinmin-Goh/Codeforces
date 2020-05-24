# Contest No.: 644
# Problem No.: A
# Solver:      JEMINI
# Date:        20200524

import sys
import heapq

def main():
    t = int(input())
    for _ in range(t):
        a, b = map(int, sys.stdin.readline().split())
        if a > b:
            a, b = b, a
        if a * 2 < b:
            print(b * b)
        else:
            print((2 * a) ** 2)
    return

if __name__ == "__main__":
    main()