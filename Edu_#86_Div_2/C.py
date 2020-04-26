# Contest No.: Edu 86
# Problem No.: C
# Solver:      JEMINI
# Date:        20200426

import sys

def gcd(a: int, b: int) -> int:
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def main():
    t = int(input())
    for _ in range(t):
        a, b, q = map(int, sys.stdin.readline().split())
        modVal = None
        modVal = a * b // gcd(a, b)
        checkList = [0] * modVal
        loopSum = 0
        for i in range(modVal):
            if ((i % a) % b) != ((i % b) % a):
                loopSum += 1
            checkList[i] = loopSum
        
        for i in range(q):
            l, r = map(int, sys.stdin.readline().split())
            def calcSum(n: int) -> int:
                return loopSum * (n // modVal) + checkList[n % modVal]
            ans = calcSum(r) - calcSum(l - 1)
            print(ans, end = " ")
        print("")
    return

if __name__ == "__main__":
    main()