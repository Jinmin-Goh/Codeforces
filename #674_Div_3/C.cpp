// Problem No.: C
// Solver:      Jinmin Goh
// Date:        20200928

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

int nums[300010];

int main() {
    int t;
    scanf("%d", &t);
    for(int _ = 0; _ < t ; _++) {
        int n;
        scanf("%d", &n);
        
        int tempVal = int(sqrt((double)n) * 2 - 1);
        if(int(sqrt(n)) * int(sqrt(n)) == n) {
            printf("%d\n", tempVal - 1);
        }
        else {
            printf("%d\n", tempVal);
        }
    }
    return 0;
}