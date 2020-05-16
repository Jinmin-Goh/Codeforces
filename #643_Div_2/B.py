# Contest No.: 643
# Problem No.: B
# Solver:      JEMINI
# Date:        20200516

import sys
import heapq

def main():
    t = int(input())
    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        nums = list(map(int, sys.stdin.readline().split()))
        numDict = {}
        nums.sort()
        for i in nums:
            if i not in numDict:
                numDict[i] = 1
            else:
                numDict[i] += 1
        sumVal = 0
        ans = 0
        for i in numDict:
            sumVal += numDict[i]
            if sumVal // i > 0:
                ans += sumVal // i
                sumVal = sumVal % i
        print(ans)
    return

if __name__ == "__main__":
    main()