# Contest No.: 660
# Problem No.: A
# Solver:      JEMINI
# Date:        20200730

import sys
import heapq

def main():
    
    t = int(input())
    for _ in range(t):
        n = int(input())
        flag = False
        prime = [2,3,5,7,11,13,17]
        nearPrime = [6, 10, 14]
        ans = []
        ans.sort()            
        if n <= 30:
            print("NO")
        else:
            print("YES")
            if n - 30 in nearPrime:
                print(6, 10, 15, n - 31)
            else:
                print(6, 10, 14, n - 30)



    return

if __name__ == "__main__":
    main()