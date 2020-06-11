# Contest No.: Edu89
# Problem No.: B
# Solver:      JEMINI
# Date:        20200611

import sys
import heapq

def main():
    t = int(input())
    for _ in range(t):
        n, x, m = map(int, sys.stdin.readline().split())
        table = []
        for _ in range(m):
            table.append(list(map(int, sys.stdin.readline().split())))
        #print(table)
        ans = [None, None]
        for i in range(m):
            if ans[0] == None:
                if table[i][0] <= x <= table[i][1]:
                    ans = [table[i][0], table[i][1]]
            else:
                if ans[0] <= table[i][1]:
                    ans[0] = min(ans[0], table[i][0])
                if ans[1] >= table[i][0]:
                    ans[1] = max(ans[1], table[i][1])
            #print(ans)
        if ans[0] == None:
            print(1)
        else:
            print(ans[1] - ans[0] + 1)
    return

if __name__ == "__main__":
    main()