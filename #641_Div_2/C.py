# Contest No.: 641
# Problem No.: C
# Solver:      JEMINI
# Date:        20200512

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

def main():
    n = int(input())
    nums = list(map(int, input().split()))

    primeList = [True] * ((10 ** 5) * 2 + 1)
    primeList[0] = False
    primeList[1] = False
    prime = []
    for i in range(2, (10 ** 5) * 2 + 1):
        if primeList[i]:
            cnt = 2 * i
            prime.append(i)
            while cnt <= (10 ** 5) * 2:
                primeList[cnt] = False
                cnt += i
    
    
    ans = 1
    for i in prime:
        noCnt = 0
        bigCnt = 0
        tempList = []
        for j in nums:
            if j < i:
                bigCnt += 1
            if j % i or j < i:
                noCnt += 1
            else:
                tempj = j
                cnt = 0
                while not tempj % i:
                    temp = 1
                    while not tempj % (i ** (temp * 2)):
                        temp <<= 1
                    cnt += temp
                    tempj = tempj // (i ** temp)
                if len(tempList) < 2:
                    tempList.append(cnt)
                    tempList.sort()
                else:
                    if tempList[0] <= cnt <= tempList[1]:
                        tempList[1] = cnt
                    elif cnt < tempList[0]:
                        tempList[1] = tempList[0]
                        tempList[0] = cnt
            if noCnt >= 2:
                break
        if bigCnt == n:
            break
        if noCnt == 0:
            ans *= i ** tempList[1]
        elif noCnt == 1:
            ans *= i ** tempList[0]

    print(ans)
                    
    
    return

if __name__ == "__main__":
    main()