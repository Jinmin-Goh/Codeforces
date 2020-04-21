# Contest No.: 636
# Problem No.: D
# Solver:      JEMINI
# Date:        20200421

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
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        nums = list(map(int, input().split()))
        sumList = [0] * (2 * k + 1)
        checkList = [0] * (2 * k + 1)
        for i in range(n // 2):
            s = max(nums[i], nums[-i - 1]) + k
            t = min(nums[i], nums[-i - 1]) + 1
            
            checkList[2] += 2
            checkList[t] -= 1
            checkList[nums[i] + nums[-i - 1]] -= 1
            if nums[i] + nums[-i - 1] < 2 * k:
                checkList[nums[i] + nums[-i - 1] + 1] += 1
            if s < 2 * k:
                checkList[s + 1] += 1
        #print(checkList)
        for i in range(2, 2 * k + 1):
            sumList[i] = sumList[i - 1] + checkList[i]
        #print(sumList)
        ans = n
        for i in range(2, 2 * k + 1):
            ans = min(sumList[i], ans)
        print(ans)
    return

if __name__ == "__main__":
    main()