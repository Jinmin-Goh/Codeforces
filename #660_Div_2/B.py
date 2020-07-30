# Contest No.: 660
# Problem No.: B
# Solver:      JEMINI
# Date:        20200730

import sys
import heapq

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        ndiv = (n - 1) // 4
        nrem = (n - 1) % 4
        ans = "9" * (n - (ndiv + 1)) + "8" * (ndiv + 1)
        print(ans)
        
    return

if __name__ == "__main__":
    main()