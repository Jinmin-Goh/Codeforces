# Contest No.: 632
# Problem No.: A
# Solver:      JEMINI
# Date:        20200408

import sys

def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, sys.stdin.readline().split())
        if n * m % 2:
            flag = True
            for i in range(n):
                for j in range(m):
                    if flag:
                        print("B", end = "")
                    else:
                        print("W", end = "")
                    flag = not flag
                print("")
        else:
            if n % 2:
                flag = True
                for i in range(n - 1):
                    for j in range(m):
                        if flag:
                            print("B", end = "")
                        else:
                            print("W", end = "")
                        flag = not flag
                    flag = not flag
                    print("")
                temp = "BW" * (m // 2 - 1) + "BB"
                print(temp)
            else:
                flag = True
                for i in range(m - 1):
                    if flag:
                        print("B", end = "")
                    else:
                        print("W", end = "")
                    flag = not flag
                print("B")
                flag = False
                for i in range(m - 1):
                    if flag:
                        print("B", end = "")
                    else:
                        print("W", end = "")
                    flag = not flag
                print("B")
                flag = True
                for i in range(2, n):
                    for j in range(m):
                        if flag:
                            print("B", end = "")
                        else:
                            print("W", end = "")
                        flag = not flag
                    print("")

    return

if __name__ == "__main__":
    main()