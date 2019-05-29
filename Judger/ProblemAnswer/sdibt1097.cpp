#include <iostream>

using namespace std;

struct node
{
    int lastlocation;
    int totalweight;
    node(){lastlocation = -1; totalweight = 999999999;}
};

int main()
{
    int n,m;
    while(cin >> n >> m)
    {
        node dp[12][102];
        int nums[12][102] = {0};
        for(int i = 1; i <= n; ++i)
        {
            for(int j = 1; j <= m; ++j)
            {
                cin >> nums[i][j];
            }
        }
        int l1,l2,l3,w1,w2,w3;
        for(int i = 1; i <= n; ++i)
        {
            dp[i][m].totalweight = nums[i][m];
            dp[i][m].lastlocation = 0;
        }
        for(int col = m-1; col >= 1; --col)
        {
            for(int row = n; row >= 1; --row)
            {
                l1 = row-1;
                if(l1 == 0)
                {
                    l1 = 1;
                    l2 = 2;
                    l3 = n;

                }
                else if(l1 == n-1)
                {
                    l1 = 1;
                    l2 = n - 1;
                    l3 = n;
                }
                else
                {
                    l2 = row;
                    l3 = row + 1;
                }
                w1 = dp[l1][col+1].totalweight;
                w2 = dp[l2][col+1].totalweight;
                w3 = dp[l3][col+1].totalweight;
                if(w1 <= w2 && w1 <= w3)
                {
                    dp[row][col].totalweight = w1;
                    dp[row][col].lastlocation = l1;
                }
                else if(w2 < w1 && w2 <= w3)
                {
                    dp[row][col].totalweight = w2;
                    dp[row][col].lastlocation = l2;
                }
                else
                {
                    dp[row][col].totalweight = w3;
                    dp[row][col].lastlocation = l3;
                }
                if(dp[row][col].totalweight == 999999999)dp[row][col].lastlocation = -1;
                else
                {
                    dp[row][col].totalweight += nums[row][col];
                }
            }
        }
        int start = n, min_weight = dp[n][1].totalweight;
        for(int i = n-1; i >= 1; --i)
        {
            if(dp[i][1].totalweight <= min_weight)
            {
                min_weight = dp[i][1].totalweight;
                start = i;
            }
        }
        int current = start;
        cout << current;
        for(int i = 1; i < m; ++i)
        {
            cout << ' ' << dp[current][i].lastlocation;
            current = dp[current][i].lastlocation;
        }
        cout << endl;
        cout << dp[start][1].totalweight << endl;
    }

    return 0;
}
