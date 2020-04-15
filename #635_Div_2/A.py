# Contest No.: 635
# Problem No.: A
# Solver:      JEMINI
# Date:        20200415

import sys

def main():
    t = int(input())
    for _ in range(t):
        a, b, c, d = map(int, sys.stdin.readline().split())
        x = b
        y = c
        z = c
        
        print(x, y, z)
    return

if __name__ == "__main__":
    main()