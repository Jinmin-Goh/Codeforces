// Contest No.: Edu95
// Problem No.: C
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

int AList[110], LList[110], newList[110], sumList[110];

int main() {
    int t;
    scanf("%d", &t);
    for(int _ = 0; _ < t; _++) {
        int n = 0;
        scanf("%d", &n);
        for(int i = 0; i < n; i++) {
            scanf("%d", &AList[i]);
        }
        for(int i = 0; i < n; i++) {
            scanf("%d", &LList[i]);
        }
        vector<int> tempList;
        for(int i = 0; i < n; i++) {
            if(LList[i]) continue;
            tempList.push_back(AList[i]);
        }
        sort(tempList.begin(), tempList.end(), greater<>());
        int cnt = 0;
        for(int i = 0; i < n; i++) {
            if(LList[i]) {
                newList[i] = AList[i];
            }
            else {
                newList[i] = tempList[cnt];
                cnt++;
            }
            printf("%d ", newList[i]);
        }
        printf("\n");
        int ans = 0;
        sumList[0] = newList[0];
        for(int i = 1; i < n; i++) {
            sumList[i] = sumList[i - 1] + newList[i];
            if(sumList[i] < 0) {
                ans = i + 1;
            }
        }
        //printf("%d", ans);
    }
    return 0;
}