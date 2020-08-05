// Contest No.: 661
// Problem No.: C
// Solver:      Jinmin Goh
// Date:        20200805

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

int nums[100];


int main() {
    int t;
    scanf("%d", &t);
    for(int _ = 0; _ < t; _++) {
        int n;
        map<int, int> numMap;
        scanf("%d", &n);
        for(int i = 0; i < n; i++) {
            scanf("%d", &nums[i]);
            if(numMap.find(nums[i]) == numMap.end()) {
                numMap[nums[i]] = 1;
            }
            else {
                numMap[nums[i]]++;
            }
        }
        sort(nums, nums + n);
        int ans = 0;
        for(int subSum = 2; subSum <= 2 * n; subSum++) {
            int cnt = 0;
            for(int p1 = 1; p1 <= (subSum - 1) / 2; p1++) {
                if(numMap.find(p1) != numMap.end() && numMap.find(subSum - p1) != numMap.end()) {
                    cnt += min(numMap[p1], numMap[subSum - p1]);
                }
            }
            if((!(subSum % 2)) && (numMap.find(subSum / 2) != numMap.end())) {
                cnt += numMap[subSum / 2] / 2;
            }
            
            ans = max(ans, cnt);
        
        }
        printf("%d\n", ans);
    }
    return 0;
}