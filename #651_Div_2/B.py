# Contest No.: 651
# Problem No.: B
# Solver:      JEMINI
# Date:        20200620

import sys
import heapq

def main():
    #tempList = [True] * (2002)
    #tempList[0] = False
    #tempList[1] = False
    #for i in range(2002):
    #    if tempList[i]:
    #        cnt = i * 2
    #        while cnt < 2002:
    #            tempList[cnt] = False
    #            cnt += i
    #prime = []
    #for i in range(2002):
    #    if tempList[i]:
    #        prime.append(i)

    t = int(input())
    for _ in range(t):
        n = int(input())
        nums = list(map(int, sys.stdin.readline().split()))

        oddList = []
        evenList = []

        for i in range(2 * n):
            if nums[i] % 2:
                oddList.append(i + 1)
            else:
                evenList.append(i + 1)
        
        if len(oddList) % 2:
            while len(oddList) > 1:
                print(oddList.pop(), oddList.pop())
            while len(evenList) > 1:
                print(evenList.pop(), evenList.pop())
        
        else:
            if evenList:
                while oddList:
                    print(oddList.pop(), oddList.pop())
                while len(evenList) > 2:
                    print(evenList.pop(), evenList.pop())
            else:
                while len(oddList) > 2:
                    print(oddList.pop(), oddList.pop())
                


        #pVal = None
        #for p in prime:
        #    remainCheck = [0] * p
        #    for i in range(2 * n):
        #        remainCheck[nums[i] % p]
        #    if p == 2:
        #        if (remainCheck[0] % 2) != (remainCheck[1] % 2):
        #            continue
        #        else:
        #            pVal = p
        #            break
        #    else:
        #        if remainCheck[p // 2] > 2:
        #            continue
        #        cnt = remainCheck[p // 2]
        #        diffList = []
        #        flag = True
        #        if remainCheck[p // 2] > 0:
        #            diffList.append(p // 2)
        #        for i in range(p // 2):
        #            if remainCheck[i] != remainCheck[p - i - 1]:
        #                cnt += abs(remainCheck[i] - remainCheck[p - i - 1])
        #                diffList.append(i)
        #            if cnt > 2:
        #                flag = False
        #                break
        #        if flag:
        #            pVal = p
        #            break
        #        else:
        #            continue
        #print("prime:", p)
            
    return

if __name__ == "__main__":
    main()