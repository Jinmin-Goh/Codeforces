# Contest No.: 648
# Problem No.: A
# Solver:      JEMINI
# Date:        20200607

import sys
import heapq

def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        table = []
        for __ in range(n):
            table.append(list(map(int, sys.stdin.readline().split())))
        rowCnt = n
        colCnt = m
        for i in range(n):
            if 1 in table[i]:
                rowCnt -= 1
        for i in range(m):
            for j in range(n):
                if table[j][i] == 1:
                    colCnt -= 1
                    break
        ans = min(rowCnt, colCnt)
        if ans % 2:
            print("Ashish")
        else:
            print("Vivek")

    return

if __name__ == "__main__":
    main()