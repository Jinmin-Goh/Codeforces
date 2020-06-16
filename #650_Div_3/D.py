# Contest No.: 650
# Problem No.: D
# Solver:      JEMINI
# Date:        20200616

import sys
import heapq

def main():
    t = int(input())
    for _ in range(t):
        s = sys.stdin.readline().strip()
        n = int(input())
        nums = list(map(int, sys.stdin.readline().split()))
        if n == 1:
            print(s[0])
            continue
        numsSorted = [[nums[i], i] for i in range(n)]
        numsSorted.sort()
        numsSorted = list(reversed(numsSorted))

        strDict = {}
        for i in s:
            if i not in strDict:
                strDict[i] = 1
            else:
                strDict[i] += 1

        usedPos = []
        sList = [i for i in s]
        sList.sort()
        ans = [None] * n
        
        # backtracking?
        def backtracking(_ans: [int], _sList: [str], _usedPos: [int]) -> [str]:
            if len(_usedPos) == n:
                return _ans
            while _sList:
                _temp = _sList.pop()
                for i in range(n):
                    if _ans[i] != None:
                        continue
                    sumVal = 0
                    for j in range(len(_usedPos)):
                        if _ans[_usedPos[j]] != _temp:
                            sumVal += abs(i - _usedPos[j])
                    if sumVal == nums[i]:
                        _ans[i] = _temp
                        _usedPos.append(i)
                        tempAns = backtracking(_ans[:], _sList[:], _usedPos)
                        if tempAns:
                            return tempAns
                        _ans[i] = None
                        _usedPos.pop()
                        break
            return []
        
        realAns = backtracking(ans, sList, usedPos)
        ans = ""
        for i in realAns:
            ans += i
        print(ans)


    return

if __name__ == "__main__":
    main()