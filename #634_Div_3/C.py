# Contest No.: 634
# Problem No.: C
# Solver:      JEMINI
# Date:        20200413

import sys

def main():
    t = int(input())
    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        nums = list(map(int, sys.stdin.readline().split()))
        numDict = {}
        if n <= 1:
            print(0)
            continue
        maxKey = nums[0]
        for i in nums:
            if i not in numDict:
                numDict[i] = 1
            else:
                numDict[i] += 1
            if numDict[i] > numDict[maxKey]:
                maxKey = i
        if numDict[maxKey] == 1:
            print(1)
            continue
        else:
            if numDict[maxKey] - 1 >= len(numDict):
                print(len(numDict))
            else:
                print(min(len(numDict) - 1, numDict[maxKey]))
    return

if __name__ == "__main__":
    main()