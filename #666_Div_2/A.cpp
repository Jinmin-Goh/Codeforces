// Contest No.: 666
// Problem No.: A
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

char nums[150];

int main() {
    int t;
    scanf("%d", &t);
    for(int _ = 0; _ < t; _++) {
        int n;
        scanf("%d", &n);
        int lenSum = 0;
        for(int i = 0; i < 150; i++) {
            nums[i] = 0;
        }
        for(int i = 0; i < n; i++) {
            char temp[1010];
            scanf("%s", temp);
            lenSum += strlen(temp);
            for(int j = 0; j < strlen(temp); j++) {
                nums[temp[j]]++;
            }
        }
        if(lenSum % n) {
            printf("NO\n");
            continue;
        }
        bool flag = false;
        for(int i = 97; i < 123; i++) {
            if(nums[i] % n) {
                flag = true;
            }
        }
        if(flag) {
            printf("NO\n");
            continue;
        }
        else {
            printf("YES\n");
            continue;
        }

    }
    return 0;
}