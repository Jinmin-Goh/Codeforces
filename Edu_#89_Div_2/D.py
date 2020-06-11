# Contest No.: Edu89
# Problem No.: D
# Solver:      JEMINI
# Date:        20200611

##### FAST INPUT #####
import os
import sys
from io import BytesIO, IOBase

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")
##### END OF FAST INPUT #####
#import sys
import heapq

def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    return gcd(b, a % b)

def main():
    n = int(input())
    nums = list(map(int, input().split()))
    ans1 = []
    ans2 = []
    ansDict = {}
    for i in range(n):
        flag = False
        num = nums[i]
        if num in ansDict:
            ans1.append(ansDict[num][0])
            ans2.append(ansDict[num][1])
            continue
        tempAns = None
        for j in range(2, int(num ** 0.5) + 1):
            if num % j == 0:
                temp = num
                cnt = j
                while temp != 1 and temp % cnt == 0:
                    while True:
                        if temp % (cnt ** 2) == 0:
                            cnt = cnt ** 2
                        else:
                            break
                    temp //= cnt
                    cnt = j
                if temp != 1:
                    flag = True
                    tempAns = [temp, num // temp]
                break

        if flag:
            ans1.append(tempAns[0])
            ans2.append(tempAns[1])
            ansDict[num] = tempAns
        else:
            ans1.append(-1)
            ans2.append(-1)
            ansDict[num] = [-1, -1]
    
    for i in ans1:
        print(i, end= " ")
    print("")
    for i in ans2:
        print(i, end= " ")
    
            

    return

if __name__ == "__main__":
    main()