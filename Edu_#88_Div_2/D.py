# Contest No.: Edu 88
# Problem No.: D
# Solver:      JEMINI
# Date:        20200528

import sys
import heapq

# wrong answer
# answer uses DP, with O(61 * n) time
def main():
    n = int(input())
    nums = list(map(int, sys.stdin.readline().split()))
    ans = 0
    for i in range(-30, 31):
        tempAns = 0
        for j in range(n):
            tempAns += nums[j]
            if nums[j] > i:
                tempAns = -31 * n
            ans = max(ans, tempAns - i)
            if tempAns < 0:
                tempAns = 0
    print(ans)
    return

if __name__ == "__main__":
    main()