# Contest No.: 643
# Problem No.: C
# Solver:      JEMINI
# Date:        20200516

import sys
import heapq

def main():
    a, b, c, d = map(int, input().split())
    dpList = [min(c - b + 1, b - a + 1)] * (c + b + 1)
    for i in range(min(c - b + 1, b - a + 1)):
        dpList[a + b + i] = i + 1
        dpList[-i - 1] = i + 1
    for i in range(a + b):
        dpList[i] = 0
    sumList = [0] * len(dpList)
    sumList[-1] = dpList[-1]
    for i in reversed(range(len(dpList) - 1)):
        sumList[i] = sumList[i + 1] + dpList[i]
    #print(dpList)
    #print(sumList)
    ans = 0
    for i in range(c, d + 1):
        if i > len(sumList) - 2:
            break
        ans += sumList[i + 1]
    print(ans)
    return

if __name__ == "__main__":
    main()