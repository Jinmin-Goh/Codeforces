# Contest No.: 644
# Problem No.: E
# Solver:      JEMINI
# Date:        20200524

import sys
import heapq

def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, sys.stdin.readline().split())
        strings = []
        for i in range(n):
            strings.append(sys.stdin.readline().strip())
        ansFlag = False
        countDict = {}
        for i in range(n):
            countDict[i] = 0
        
        def backtrack(ans: str, depth: int):
            #print(ans, depth)
            if depth == m:
                return ans
            for temp in range(n):
                if ans[depth] != strings[temp][depth]:
                    countDict[temp] += 1
                if countDict[temp] > 1:
                    return None
            return backtrack(ans, depth + 1)
        
        def numGen(numList: [str]):
            if numList and len(numList[0]) == m:
                return numList
            tempList = []
            if not numList:
                for temp in range(n):
                    tempList.append(str(temp))
            else:
                while numList:
                    tempStr = numList.pop()
                    for temp in range(n):
                        tempList.append(tempStr + str(temp))
            return numGen(tempList)
        numList = numGen([])
        
        for i in numList:
            for j in range(n):
                countDict[j] = 0
            ans = ""
            for j in range(m):
                ans += strings[int(i[j])][j]
            tempVal = backtrack(ans, 0)
            if tempVal != None:
                ansFlag = True
                break


        if not ansFlag:
            print(-1)
        else:
            print(ans)

        
        
    return

if __name__ == "__main__":
    main()