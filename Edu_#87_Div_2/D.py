# Contest No.: Edu 87
# Problem No.: D
# Solver:      JEMINI
# Date:        20200517

import sys
import heapq

def main():
    n, q = map(int, input().split())
    aList = list(map(int, sys.stdin.readline().split()))
    kList = list(map(int, sys.stdin.readline().split()))
    posCnt = 0
    negCnt = 0
    cnt = n
    zeroPos = None
    for i in kList:
        if i > 0:
            posCnt += 1
            cnt += 1
        else:
            negCnt += 1
            cnt -= 1
        if cnt == 0:
            zeroPos = posCnt + negCnt - 1
    # optimize
    if negCnt - posCnt == n:
        print(0)
        return
    if negCnt == 0:
        print(aList[0])
        return
    if kList[-1] > 0:
        print(kList[-1])
        return
    if zeroPos != None:
        kList = kList[zeroPos + 1:]
        aList = []
    #print(aList, kList)
    negFlag = False
    for i in kList:
        if i > 0:
            negFlag = False
            aList.append(i)
        else:
            if not negFlag:
                negFlag = True
                aList.sort()
            aList.pop(-i - 1)
    #print(aList)
    print(aList[0])
    return

if __name__ == "__main__":
    main()