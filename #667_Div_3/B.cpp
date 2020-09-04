// Contest No.: 667
// Problem No.: B
// Solver:      Jinmin Goh
// Date:        20200904

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

int nums[200010];

int main() {
    int t;
    scanf("%d", &t);
    for(int _ = 0; _ < t; _++) {
        long long int a, b, x, y, n;
        scanf("%lld %lld %lld %lld %lld", &a, &b, &x, &y, &n);
        
        long long diffA = a - x, diffB = b - y, diffVal;
        
        if(diffA + diffB <= n) {
            printf("%lld\n", x * y);
            continue;
        }
        long long int ans1 = 1, ans2 = 1;

        if(diffA >= n && diffB >= n) {
            printf("%lld\n", min(a * (b - n), b * (a - n)));
            continue;
        }
        else if(diffA < n && diffB < n) {
            ans1 *= y;
            ans1 *= a - (n - diffB);
            
            ans2 *= x;
            ans2 *= b - (n - diffA);
            printf("%lld\n", min(ans1, ans2));
        }
        else if(diffA < n && diffB >= n) {
            ans2 *= x;
            ans2 *= b - (n - diffA);
            printf("%lld\n", min(a * (b - n), ans2));
        }
        else {
            ans1 *= y;
            ans1 *= a - (n - diffB);
            printf("%lld\n", min(ans1, b * (a - n)));
        }

        
    }
    return 0;
}