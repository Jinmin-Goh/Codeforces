# Contest No.: 648
# Problem No.: B
# Solver:      JEMINI
# Date:        20200607

import sys
import heapq

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        aList = list(map(int, sys.stdin.readline().split()))
        bList = list(map(int, sys.stdin.readline().split()))
        list0 = []
        list1 = []
        for i in range(n):
            if bList[i]:
                list1.append(aList[i])
            else:
                list0.append(aList[i])
        
        if list0 and list1:
            print("Yes")
        else:
            flag = True
            if list0:
                for i in range(len(list0) - 1):
                    if list0[i] > list0[i + 1]:
                        flag = False
                        break
            if list1:
                for i in range(len(list1) - 1):
                    if list1[i] > list1[i + 1]:
                        flag = False
                        break
            if flag:
                print("Yes")
            else:
                print("No")
    return

if __name__ == "__main__":
    main()