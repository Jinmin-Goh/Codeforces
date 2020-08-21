// Contest No.: 665
// Problem No.: C
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

int nums[100010], reference[100010];

int gcd(int a, int b) {
    if(a < b) {
        swap(a, b);
    }
    if(b == 0) {
        return a;
    }

    return gcd(b, a % b);
}

int main() {
    int t;
    scanf("%d", &t);
    for(int _ = 0; _ < t; _++) {
        int n, ans = 0, minVal = 1e9;
        scanf("%d", &n);

        for(int i = 0; i < n; i++) {
            scanf("%d", &nums[i]);
            reference[i] = nums[i];
            minVal = min(minVal, nums[i]);
        }

        sort(reference, reference + n);
        vector<int> diffList;
        for(int i = 0; i < n; i++) {
            if(nums[i] != reference[i]) {
                diffList.push_back(nums[i]);
            }
        }
        if(diffList.size() == 0) {
            printf("YES\n");
            continue;
        }
    
        sort(diffList.begin(), diffList.end());
        int gcdVal = diffList.front();
        bool flag = false;
        vector<int>::iterator iter;
        for(iter = diffList.begin() + 1; iter != diffList.end(); iter++) {
            gcdVal = gcd(gcdVal, *iter);
        }
        if(gcdVal % minVal) {
            printf("NO\n");
        }
        else {
            printf("YES\n");
        }

    }
    return 0;
}