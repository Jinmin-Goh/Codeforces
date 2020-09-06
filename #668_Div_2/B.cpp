// Contest No.: 668
// Problem No.: B
// Solver:      Jinmin Goh
// Date:        20200906

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

long long nums[100010];

int main() {
    long long t;
    scanf("%lld", &t);
    for(long long _ = 0; _ < t; _++) {
        long long n;
        scanf("%lld", &n);
        for(long long i = 0; i < n; i++) {
            scanf("%lld", &nums[i]);
        }

        long long pl = n - 1, pr = n - 1;
        while(nums[pl] <= 0 && pl < n) {
            pl--;
        }
        while(nums[pr] >= 0 && pr >= 0) {
            pr--;
        }
        if(pl >= pr) {
            pl = pr;
            while(nums[pl] <= 0 && pl < n) {
                pl--;
            }
        }

        while(pl >= 0 && pr >= 0) {
            if(nums[pl] > -nums[pr]) {
                nums[pl] += nums[pr];
                nums[pr] = 0;
            }
            else {
                nums[pr] += nums[pl];
                nums[pl] = 0;
            }
            while(nums[pl] <= 0 && pl >= 0) {
                pl--;
            }
            while(nums[pr] >= 0 && pr >= 0) {
                pr--;
            }
            if(pl >= pr) {
                pl = pr;
                while(nums[pl] <= 0 && pl < n) {
                    pl--;
                }
            }
        }
        long long ans = 0;
        for(long long i = 0; i < n; i++) {
            if(nums[i] > 0) {
                ans += nums[i];
            }
        }
        printf("%lld\n", ans);
    }
    return 0;
}