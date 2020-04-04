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
        maxNum = max(nums)
        colorDict = {}
        primeDict = {}
        for i in nums:
            currColor = None
            tempPrime = []
            for p in primeList:
                if p > maxNum:
                    break
                #print(colorDict)
                #print(p, i)
                if i % p == 0:
                    tempPrime.append(p)
            
            for j in primeDict:
                flag = False
                for k in primeDict[j]:
                    flag = False                 
                    for p in tempPrime:
                        if p in k:
                            flag = True
                            break
                    if not flag:
                        break
                if flag:
                    currColor = j
                    break

            #for p in tempPrime:
            #    #print(p, i, currColor)
            #    if not colorDict:
            #        colorDict[1] = set()
            #        primeDict[1] = set()
            #        currColor = 1
            #    else:
            #        for j in primeDict:
            #            for k in primeDict[j]:
            #                if p in primeDict[j]:
            #                    if not currColor:
            #                        currColor = j
            #                    else:
            #                        currColor = min(currColor, j)
            if currColor == None:
                colorDict[len(colorDict) + 1] = set()
                primeDict[len(primeDict) + 1] = []
                currColor = len(colorDict)
            colorDict[currColor].add(i)
            primeDict[currColor].append(set(tempPrime))
            print(colorDict)
            print("")
            print(primeDict)
            print("")
        print(len(colorDict))
        for i in nums:
            for j in range(1, 12):
                if i in colorDict[j]:
                    print(j, end = " ")
                    break
        print("")
    return

if __name__ == "__main__":
    main()