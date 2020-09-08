// Contest No.: 669
// Problem No.: B
// Solver:      Jinmin Goh
// Date:        20200908

#include <cstring>
#include <iostream>
#include <cstdlib>
#include <list>
#include <array>
#include <atomic>
#include <algorithm>
#include <deque>
#include <iterator>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <valarray>
#include <vector>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
using namespace std;

int nums[1010], used[1010];

int gcd(int a, int b) {
    if(a < b) {
        swap(a, b);
    }
    if(b == 0) {
        return a;
    }
    return gcd(b, a % b);
}

int main() {
    int t;
    scanf("%d", &t);
    for(int _ = 0; _ < t; _++) {
        int n;
        scanf("%d", &n);
        for(int i = 0; i < n; i++) {
            scanf("%d", &nums[i]);
        }
        int cnt = 1;
        sort(nums, nums + n);
        printf("%d ", nums[n - 1]);
        for(int i = 0; i < n; i++) {
            used[i] = 0;
        }
        used[n - 1] = 1;
        int currVal = nums[n - 1];
        while(cnt < n) {
            int maxGCD = 1, maxPos = 0;
            for(int i = n - 2; i >= 0; i--) {
                if(used[i]) continue;
                if(gcd(currVal, nums[i]) >= maxGCD) {
                    maxPos = i;
                    maxGCD = gcd(currVal, nums[i]);
                }
            }
            printf("%d ", nums[maxPos]);
            used[maxPos] = 1;
            currVal = maxGCD;
            cnt++;
        }
        printf("\n");
    }
    return 0;
}