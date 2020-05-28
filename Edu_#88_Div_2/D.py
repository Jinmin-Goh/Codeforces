# Contest No.: Edu 88
# Problem No.: D
# Solver:      JEMINI
# Date:        20200528

import sys
import heapq

# wrong answer
# answer uses DP, with O(61 * n) space
def main():
    n = int(input())
    nums = list(map(int, sys.stdin.readline().split()))
    ans = 0
    maxVal = [nums[0], 0]
    sumList = [0] * n
    sumList[0] = nums[0]
    for i in range(1, n):
        sumList[i] = max(0, sumList[i - 1] + nums[i])
        if sumList[i] == 0 or maxVal[0] < nums[i]:
            maxVal = [nums[i], i]
        ans = max(ans, sumList[i] - max(0, maxVal[0]))
        #print(sumList)
        #print(maxVal)
    #print(sumList)
    print(ans)
    return

if __name__ == "__main__":
    main()