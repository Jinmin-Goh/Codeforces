// Contest No.: Edu95
// Problem No.: A
// Solver:      Jinmin Goh
// Date:        20200914

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
        long long x, y, k;
        scanf("%lld %lld %lld", &x, &y, &k);
        printf("%lld\n", (k + k * y + x - 3) / (x - 1) + k);
    }
    return 0;
}