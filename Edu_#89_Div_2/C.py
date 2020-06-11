# Contest No.: Edu89
# Problem No.: C
# Solver:      JEMINI
# Date:        20200611

import sys
import heapq

def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, sys.stdin.readline().split())
        table = []
        for i in range(n):
            table.append(list(map(int, sys.stdin.readline().split())))
        ans = 0

        if n <= m:
            for i in range((n + m - 1) // 2):
                pointer = 0
                cnt0 = 0
                cnt1 = 0
                while i - pointer >= 0 and pointer < n:
                    if table[pointer][i - pointer] == 0:
                        cnt0 += 1
                    else:
                        cnt1 += 1

                    if table[-pointer - 1][pointer - i - 1] == 0:
                        cnt0 += 1
                    else:
                        cnt1 += 1
                    pointer += 1
                ans += min(cnt0, cnt1)
        else:
            for i in range((n + m - 1) // 2):
                pointer = 0
                cnt0 = 0
                cnt1 = 0
                while i - pointer >= 0 and pointer < m:
                    if table[i - pointer][pointer] == 0:
                        cnt0 += 1
                    else:
                        cnt1 += 1

                    if table[pointer - i - 1][-pointer - 1] == 0:
                        cnt0 += 1
                    else:
                        cnt1 += 1
                    pointer += 1
                ans += min(cnt0, cnt1)
        print(ans)
    return

if __name__ == "__main__":
    main()