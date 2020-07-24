# Contest No.: 659
# Problem No.: C
# Solver:      JEMINI
# Date:        20200724

import sys
import heapq

def main():
    alphabet = "abcdefghijklmnopqrst"
    t = int(input())
    for _ in range(t):
        n = int(input())
        A = sys.stdin.readline().strip()
        B = sys.stdin.readline().strip()
        ADict = {}        
        BList = set()
        flag = False
        for i in range(n):
            if A[i] > B[i]:
                flag = True
                break
            if A[i] != B[i]:
                if A[i] not in ADict:
                    ADict[A[i]] = [i]
                else:
                    ADict[A[i]].append(i)
                BList.add(B[i])
        if flag:
            print(-1)
            continue
        AList = list(ADict.keys())
        BList = list(BList)
        
        AList += BList
        AList = list(set(AList))
        AList.sort()
        AList = list(reversed(AList))
        #BList.sort()
        ans = 0
        while AList:
            temp = AList.pop()
            tempList = []
            flag = False
            #print(temp, ADict[temp])
            for j in ADict[temp]:
                if temp < B[j]:
                    tempList.append(j)
                # elif A[j] in BList:
                #     flag = True
            # if flag:
            #     BList.remove(temp)
            #print(tempList)
            tempList = list(set(tempList))
            if tempList:
                ans += 1
                if AList:
                    # if AList[-1] > min(BList):
                    #     ADict[min(BList)] = tempList
                    #     AList.append(min(BList))
                    # else:
                    if AList[-1] in ADict:
                        ADict[AList[-1]] += tempList
                        ADict[AList[-1]] = list(set(ADict[AList[-1]]))
                    else:
                        ADict[AList[-1]] = tempList
                    
                #print(ADict, AList)
        print(min(ans, n))
    return

if __name__ == "__main__":
    main()