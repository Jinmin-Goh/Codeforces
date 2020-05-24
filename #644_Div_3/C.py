# Contest No.: 644
# Problem No.: C
# Solver:      JEMINI
# Date:        20200524

import sys
import heapq

def main():
    t = int(input())
    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        nums = list(map(int, sys.stdin.readline().split()))
        oddCnt = 0
        evenCnt = 0
        for i in nums:
            if i % 2:
                oddCnt += 1
            else:
                evenCnt -= 1
        if oddCnt % 2 == 0:
            print("YES")
            continue
        nums.sort()
        flag = False
        for i in range(1, n):
            if nums[i] - nums[i - 1] == 1 and nums[i] % 2 + nums[i - 1] % 2 == 1:
                flag = True
        if flag:
            print("YES")
        else:
            print("NO")
        
    return

if __name__ == "__main__":
    main()