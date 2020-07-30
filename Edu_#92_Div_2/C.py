# Contest No.: Edu92
# Problem No.: C
# Solver:      JEMINI
# Date:        20200729

import sys
import heapq

def main():
    t = int(input())
    for _ in range(t):
        strN = input()
        
        flag = False
        temp = strN[0]
        for i in strN:
            if i != temp:
                flag = True
        if not flag or len(strN) == 2:
            print(0)
            continue

        ans = len(strN)
        for i in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            for j in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                if j == i:
                    continue
                cnt = 0
                tempFlag = False
                for k in strN:
                    if k == i and not tempFlag:
                        tempFlag = True
                    elif k == j and tempFlag:
                        cnt += 2
                        tempFlag = False
                #print(i, j, cnt)
                ans = min(ans, len(strN) - cnt)
        
        for i in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            cnt = 0
            for k in strN:
                if k == i:
                    cnt += 1
            ans = min(ans, len(strN) - cnt)
        print(ans)

    return

if __name__ == "__main__":
    main()