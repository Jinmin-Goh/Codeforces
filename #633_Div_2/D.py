# Contest No.: 633
# Problem No.: D
# Solver:      JEMINI
# Date:        20200413

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
    graphDict = {}
    leafSet = set()
    middleSet = set()
    for _ in range(n - 1):
        a, b = map(int, input().split())
        if a not in graphDict:
            leafSet.add(a)
            graphDict[a] = [b]
        else:
            middleSet.add(a)
            if a in leafSet:
                leafSet.remove(a)
            graphDict[a].append(b)
        if b not in graphDict:
            leafSet.add(b)
            graphDict[b] = [a]
        else:
            middleSet.add(b)
            if b in leafSet:
                leafSet.remove(b)
            graphDict[b].append(a)
    # find leaves
    middleList = list(middleSet)
    maxAns = n - 1
    minAns = 1
    temp = 0
    for i in middleList:
        flag = False
        cnt = 0
        for j in graphDict[i]:
            if j in leafSet:
                cnt += 1
        if cnt > 1:
            temp += cnt
    maxAns -= temp // 2
    print(minAns, maxAns)

    # find all 
    return

if __name__ == "__main__":
    main()