// Contest No.: 672
// Problem No.: C
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

long long nums[300010];

int main() {
    long long t;
    scanf("%lld", &t);
    for(long long _ = 0; _ < t; _++) {
        long long n, q;
        scanf("%lld %lld", &n, &q);
        long long maxVal = 0;
        for(long long i = 0; i < n; i++) {
            scanf("%lld", &nums[i]);
            maxVal = max(maxVal, nums[i]);
        }
        if(n <= 2) {
            printf("%lld\n", maxVal);
            continue;
        }
        bool decFlag = false, incFlag = false;
        long long currMin = nums[0], currMax = nums[0], ans = 0;
        
        if(nums[0] < nums[1]) {
            incFlag = true;
            currMax = nums[1];
        }
        else if(nums[0] > nums[1]) {
            decFlag = true;
            currMin = nums[1];
        }

        for(long long i = 1; i < n - 1; i++) {
            //printf("%d %d %d %d %d\n", i, decFlag, incFlag, currMin, currMax);
            if(nums[i] < nums[i + 1]) {
                if(decFlag) {
                    decFlag = false;
                    incFlag = true;
                    ans += currMax - nums[i];
                    currMin = nums[i];
                    currMax = nums[i + 1];
                }
                if(incFlag) {
                    currMax = nums[i + 1];
                }
            }
            else if(nums[i] > nums[i + 1]) {
                if(incFlag) {
                    incFlag = false;
                    decFlag = true;
                    //ans += currMin - nums[i];
                    currMax = nums[i];
                    currMin = nums[i + 1];
                }
                if(decFlag) {
                    currMin = nums[i + 1];
                }
            }
        }
        ans += currMax;
        printf("%lld\n", ans);
    }
    return 0;
}