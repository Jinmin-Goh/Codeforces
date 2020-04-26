# Contest No.: Edu 86
# Problem No.: B
# Solver:      JEMINI
# Date:        20200426

import sys

def main():
    t = int(input())
    for _ in range(t):
        word = sys.stdin.readline().strip()
        cnt = 0
        for i in word:
            if i == "0":
                cnt -= 1
            else:
                cnt += 1
        if abs(cnt) == len(word):
            print(word)
        else:
            ans = word[0]
            i = 0
            while i < len(word):
                if word[i] == "1":
                    if ans[-1] == "0":
                        ans += "1"
                        i += 1
                    else:
                        ans += "01"
                        i += 1
                else:
                    if ans[-1] == "1":
                        ans += "0"
                        i += 1
                    else:
                        ans += "10"
                        i += 1
            print(ans)

    return

if __name__ == "__main__":
    main()