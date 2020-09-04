// Contest No.: 667
// Problem No.: A
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
        int n, m;
        scanf("%d %d", &n, &m);
        printf("%d\n", (abs(n - m) + 9) / 10);
    }
    return 0;
}