# Contest No.: 651
# Problem No.: C
# Solver:      JEMINI
# Date:        20200620

import sys
import heapq

def main():
    tempList = [True] * (10 ** 5 + 1)
    tempList[0] = False
    tempList[1] = False
    for i in range(10 ** 5 + 1):
        if tempList[i]:
            cnt = i * 2
            while cnt < 10 ** 5 + 1:
                tempList[cnt] = False
                cnt += i
    prime = []
    for i in range(10 ** 5 + 1):
        if tempList[i]:
            prime.append(i)

    t = int(input())
    for _ in range(t):
        n = int(input())
        if n == 2:
            print("Ashishgup")
            continue
        if n == 1:
            print("FastestFinger")
            continue
        if n % 2:
            print("Ashishgup")
            continue
        
        twoCnt = 0
        oddCnt = 0
        tempN = n
        for p in prime:
            if tempN < p:
                break
            while tempN % p == 0:
                tempN = tempN // p
                if p == 2:
                    twoCnt += 1
                else:
                    oddCnt += 1
        if tempN != 1:
            oddCnt += 1
        
        if oddCnt == 0:
            print("FastestFinger")
            continue
        
        elif twoCnt == 1:
            if oddCnt == 1:
                print("FastestFinger")
                continue
            else:
                print("Ashishgup")
                continue
        else:
            print("Ashishgup")
            continue
        
        
        
    return

if __name__ == "__main__":
    main()