// Contest No.: 672
// Problem No.: B
// Solver:      Jinmin Goh
// Date:        20200924

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

long long nums[200010];

int main() {
    long long t;
    scanf("%lld", &t);
    for(long long _ = 0; _ < t; _++) {
        long long n;
        scanf("%lld", &n);
        for(long long i = 0; i < n; i++) {
            scanf("%lld", &nums[i]);
        }
        sort(nums, nums + n);
        long long twoVal = 1;
        long long cnt = 0, ans = 0;
        while(twoVal * 2 <= nums[0]) {
            twoVal *= 2;
        }
        for(long long i = 0; i < n; i++) {
            //printf("%d %d\n", twoVal, nums[i]);
            if(twoVal * 2 <= nums[i]) {
                ans += cnt * (cnt - 1) / 2;
                while(twoVal * 2 <= nums[i]) {
                    twoVal *= 2;
                }
                cnt = 1;
                //printf("%lld\n", ans);
            }
            else {
                cnt++;
            }
            
        }
        ans += cnt * (cnt - 1) / 2;
        printf("%lld\n", ans);
    }
    return 0;
}