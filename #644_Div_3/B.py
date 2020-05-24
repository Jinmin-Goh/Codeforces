# Contest No.: 644
# Problem No.: B
# Solver:      JEMINI
# Date:        20200524

import sys
import heapq

def main():
    t = int(input())
    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        nums = list(map(int, sys.stdin.readline().split()))
        nums.sort()
        ans = nums[1] - nums[0]
        for i in range(1, n):
            ans = min(ans, nums[i] - nums[i - 1])
        print(ans)
    return

if __name__ == "__main__":
    main()