# Problem No.: C
# Solver:      Jinmin Goh
# Date:        20200403
 
import sys
 
def main():
    n, m = map(int, input().split())
    nums = list(map(int, sys.stdin.readline().split()))
    sumVal = sum(nums)
    diff = sumVal - n
    if sumVal < n or sumVal >= n * (n + 1) // 2:
        print(-1)
        return
    nums.sort()
    nums = list(reversed(nums))
    pointer = 0
    colDict = {}
    ans = []
    endPos = None
    for i in range(len(nums)):
        if nums[i] + pointer > n:
            print(-1)
            return
        else:
            if not colDict:
                colDict[i] = (pointer, pointer + nums[i] - 1)
                endPos = nums[i] - 1
                continue
            tempSum = 0
            for j in colDict:
                tempSum += max(0, colDict[j][1] - pointer)
            #while diff <= tempSum or pointer <= endPos:
            #    pointer += 1
            #    tempSum = 0
            #    for j in colDict:
            #        tempSum += max(0, colDict[j][1] - pointer)
            if diff > tempSum:
                ans.append(pointer + 1)
                diff -= tempSum
            elif diff > 0:
                ans.append(pointer + 1)
                diff = 0
            else:
                ans.append(pointer + nums)
    
    for i in ans:
        print(i, end = " ")

    
    return
 
if __name__ == "__main__":
    main()