# Contest No.: 649
# Problem No.: A
# Solver:      JEMINI
# Date:        20200613

import sys
import heapq

def main():
    t = int(input())
    for _ in range(t):
        n, x = map(int, sys.stdin.readline().split())
        nums = list(map(int, sys.stdin.readline().split()))
        sumVal = sum(nums)
        if sumVal % x:
            print(n)
            continue
        
        flag = False
        for i in nums:
            if i % x:
                flag = True
                break
        
        if not flag:
            print(-1)
            continue
        
        pFront = 0
        while nums[pFront] % x == 0:
            pFront += 1

        pRear = n - 1
        while nums[pRear] % x == 0:
            pRear -= 1
        #print(pFront, pRear, nums[pFront], nums[pRear])
        if pFront == 0:
            print(pRear + 1)
        elif pRear == n - 1:
            print(n - pFront)
        else:
            print(n - min(pFront + 1, n - pRear))


    return

if __name__ == "__main__":
    main()