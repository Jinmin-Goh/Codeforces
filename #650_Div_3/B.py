# Contest No.: 650
# Problem No.: B
# Solver:      JEMINI
# Date:        20200616

import sys
import heapq

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        nums = list(map(int, sys.stdin.readline().split()))
        #print(nums)
        oddCnt = 0
        evenCnt = 0
        for i in range(n):
            if i % 2 and nums[i] % 2 == 0:
                oddCnt += 1
            if i % 2 == 0 and nums[i] % 2:
                evenCnt += 1
        #print(oddCnt, evenCnt)
        if oddCnt + evenCnt == 0:
            print(0)
            continue
        if oddCnt != evenCnt:
            print(-1)
        else:
            print(oddCnt)

    return

if __name__ == "__main__":
    main()