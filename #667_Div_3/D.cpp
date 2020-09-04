// Contest No.: 667
// Problem No.: D
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

int main() {
    long long t;
    scanf("%lld", &t);
    for(long long _ = 0; _ < t; _++) {
        char n[30];
        long long s;
        scanf("%s %lld", n, &s);
        long long cnt = 1, sumVal = 0;
        long long intN = atoi(n);
        
        for(long long i = 0; n[i] != NULL; i++) {
            sumVal += n[i] - 48;
        }
        if(sumVal <= s) {
            printf("0\n");
            continue;
        }

        long long length = strlen(n), pos = length - 2;
        long long ans = 10 - (n[length - 1] - 48);
        sumVal -= n[length - 1] - 48;
        while(pos >= 0) {
            long long posNum = n[pos] - 48;
            if(sumVal + 1 <= s) {
                break;
            }
            else {
                pos--;
                sumVal -= posNum;
                ans += (long long) (9 - posNum) * (long long) pow(10, length - pos - 2);
            }
        }
        
        printf("%lld\n", ans);
        
    }
    return 0;
}