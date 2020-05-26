# Contest No.: 645
# Problem No.: B
# Solver:      JEMINI
# Date:        20200526

import sys
import heapq

def main():
    t = int(input())
    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        nums = list(map(int, sys.stdin.readline().split()))
        nums.sort()
        ans = 1
        temp = 0
        for i in range(n):
            if nums[i] <= ans + temp:
                ans += temp + 1
                temp = 0
            else:
                temp += 1
            #print(ans, temp)
        print(ans)
    return

if __name__ == "__main__":
    main()