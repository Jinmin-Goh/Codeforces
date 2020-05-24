# Contest No.: 644
# Problem No.: D
# Solver:      JEMINI
# Date:        20200524

import sys
import heapq


def main():
    


    t = int(input())
    for _ in range(t):
        a, b = map(int, sys.stdin.readline().split())
        if a <= b:
            print(1)
            continue
        if b == 1:
            print(a)
            continue
        temp = 0
        for i in range(1, min(b + 1, int(a ** 0.5) + 1)):
            if a % i == 0:
                temp = max(temp, i)
                if a // i <= b:
                    temp = max(temp, a // i)
        print(a // temp)
    return

if __name__ == "__main__":
    main()