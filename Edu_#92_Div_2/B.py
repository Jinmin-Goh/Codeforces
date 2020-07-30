# Contest No.: Edu92
# Problem No.: B
# Solver:      JEMINI
# Date:        20200729

import sys
import heapq

def main():
    t = int(input())
    for _ in range(t):
        n, k, z = map(int, sys.stdin.readline().split())
        nums = list(map(int, sys.stdin.readline().split()))
        sortedNums = nums[:]
        sortedNums.sort()
        
        twoSumList = []
        summedNums = [nums[0]]
        for i in range(n - 1):
            twoSumList.append([nums[i] + nums[i + 1], i])
            summedNums.append(summedNums[-1] + nums[i + 1])
        twoSumList.sort()
        #print(twoSumList)
        #print(summedNums)
        ans = 0
        for sumVal in reversed(twoSumList):
            i = sumVal[1] + 1
            if i > k:
                ans = max(ans, summedNums[k])
                continue

            tempAns = summedNums[i]
            tempK = k - i
            if (tempK + 1) // 2 <= z:
                tempAns += (tempK % 2) * nums[i - 1] + sumVal[0] * (tempK // 2)
            else:
                tempAns += sumVal[0] * z
                tempK -= 2 * z
                tempAns += summedNums[i + tempK] - summedNums[i]
            ans = max(ans, tempAns)

        print(ans)

    return

if __name__ == "__main__":
    main()