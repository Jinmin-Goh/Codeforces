# Contest No.: 641
# Problem No.: A
# Solver:      JEMINI
# Date:        20200512

import sys

def main():
    t = int(input())    
    primeList = [True] * (10 ** 6 + 1)
    primeList[0] = False
    primeList[1] = True
    prime = []
    for i in range(2, 10 ** 6 + 1):
        if primeList[i]:
            cnt = 2 * i
            prime.append(i)
            while cnt <= 10 ** 6:
                primeList[cnt] = False
                cnt += i
        
    for _ in range(t):
        a, b = map(int, sys.stdin.readline().split())
        ans = a
        if a % 2:
            if a in prime:
                ans += a
                b -= 1
            else:
                for i in prime:
                    if not a % i:
                        ans += i
                        b -= 1
                        break
        if b > 0:
            ans += 2 * b
        print(ans)

    return

if __name__ == "__main__":
    main()