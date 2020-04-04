# Problem No.: B
# Solver:      Jinmin Goh
# Date:        20200331

import sys

def main():
    t = int(input())
    checkList = [True] * 10001
    checkList[0] = False
    checkList[1] = False
    primeList = []
    for i in range(10001):
        if checkList[i]:
            primeList.append(i)
            temp = 2 * i
            while temp <= 10000:
                checkList[temp] = False
                temp += i
    for _ in range(t):
        n = int(sys.stdin.readline())
        nums = list(map(int, sys.stdin.readline().split()))
        numSet = set(nums)
        maxNum = max(nums)
        colorDict = {}
        primeDict = {}
        for i in nums:
            currColor = None
            tempPrime = []
            for p in primeList:
                if p > maxNum:
                    break
                if i % p == 0:
                    if p not in primeDict:
                        primeDict[p] = [i]
                    else:
                        primeDict[p].append(i)
        print(primeDict)
        while primeDict:
            maxLen = 0
            maxPos = None
            for i in primeDict:
                if maxLen < len(primeDict[i]):
                    maxPos = i
                    maxLen = len(primeDict[i])
            colorDict[maxPos] = set(primeDict[maxPos])
            for i in primeDict[maxPos]:
                if i in numSet:
                    numSet.remove(i)
                for j in primeDict:
                    if i in primeDict[j]:
                        primeDict[j].pop(primeDict[j].index(i))
            del primeDict[maxPos]
        print(colorDict)
        for i in nums:
            for j in colorDict:
                if i in colorDict[j]:
                    print(j, end = " ")
                    break
        print("")
    return

if __name__ == "__main__":
    main()