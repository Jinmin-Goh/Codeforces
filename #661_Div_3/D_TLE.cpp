// Contest No.: 661
// Problem No.: D
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

char nums[200010], belong[200010];

int main() {
    int t;
    scanf("%d", &t);
    for(int _ = 0; _ < t; _++) {
        int n;
        scanf("%d", &n);
        scanf("%s", nums);
        int remain = n, cnt = 1;
        for(int i = 0; i < n; i++) {
            belong[i] = 0;
        }
        while(remain > 0) {
            int p = 0;
            while(belong[p]) {
                p++;
            }
            bool oneFlag = nums[p] == '1';
            belong[p] = cnt;
            oneFlag = !oneFlag;
            remain--;
            p++;
            while(p < n) {
                if(oneFlag && nums[p] == '1' && !belong[p]) {
                    belong[p] = cnt;
                    oneFlag = !oneFlag;
                    remain--;
                }
                else if(!oneFlag && nums[p] == '0' && !belong[p]) {
                    belong[p] = cnt;
                    oneFlag = !oneFlag;
                    remain--;
                }

                p++;
            }

            cnt ++;
        }
        printf("%d\n", cnt - 1);
        for(int i = 0; i < n; i++) {
            printf("%d ", belong[i]);
        }
        printf("\n");
    }
    return 0;
}