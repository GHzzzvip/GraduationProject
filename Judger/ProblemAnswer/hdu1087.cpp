#include <cstdio> 
#include <cstring>
#include <algorithm> 

#define MAX(m, n) ( (m > n) ? m : n )

namespace {
    using std::scanf;
    using std::printf;
    using std::memset;
}

const int g_kMaxSize = 1001;

int main(int argc, const char *argv[])
{
    int n;
    int arr[g_kMaxSize] = { 0 };
    int dp[g_kMaxSize] = { 0 };
    int i, j;
    int res;
    while (~scanf("%d", &n)) {
        if (!n) {
            break;
        }

        for (i = 0; i < n; ++i) {
            scanf("%d", &arr[i]);
        }

        dp[0] = arr[0];
        for (i = 1; i < n; ++i) {
            dp[i] = arr[i];
            for (j = 0; j < i; ++j) {  //在i位置之前寻找符合条件的j
                if (arr[j] < arr[i]) {
                    dp[i] = MAX(dp[i], dp[j] + arr[i]);
                }
            }
        }

        //在dp数组中寻找最后需要求解的最大递增子数组和
        res = -1;
        for (i = 0; i < n; ++i) {
            res = MAX(res, dp[i]);
        }

        printf("%d\n", res);
    }
    return 0;
}