// Contest No.: 666
// Problem No.: B
// Solver:      Jinmin Goh
// Date:        20200830

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

long long int nums[100010];

int main() {
    long long int n;
    scanf("%lld", &n);
    for(int i = 0; i < n; i++) {
        scanf("%lld", &nums[i]);
    }
    long long int ans = 0;

    sort(nums, nums + n);

    long long int lo = 1, hi = ceil(pow(nums[n - 1], (double) 1 / (n - 1))) + 1, minVal = 1e18;
    while(lo <= hi) {
        long long mid1 = (2 * lo + hi) / 3, mid2 = (lo + hi * 2) / 3;
        long long midVal1 = 0, midVal2 = 0;
        
        for(int i = 0; i < n; i++) {
            midVal1 += abs(((long long int) pow(mid1, i)) - nums[i]);
            midVal2 += abs(((long long int) pow(mid2, i)) - nums[i]);
        }

        if(midVal1 > midVal2) {
            minVal = min(minVal, min(midVal1, midVal2));
            lo = mid1 + 1;
        }
        else {
            minVal = min(minVal, min(midVal1, midVal2));
            hi = mid2 - 1;
        }
        
    }

    printf("%lld", minVal);
    return 0;
}