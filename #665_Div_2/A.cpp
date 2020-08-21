// Contest No.: 665
// Problem No.: A
// Solver:      Jinmin Goh
// Date:        20200821

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
        int n, k, ans = 0;
        scanf("%d %d", &n, &k);
        if(n == k) {
            printf("%d\n", 0);
        }
        if(n > k) {
            printf("%d\n", (n - k) % 2);
        }
        if(n < k) {
            printf("%d\n", k - n);
        }
    }
    return 0;
}