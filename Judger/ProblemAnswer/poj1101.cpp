 #include<cstdio>  
#include<cstring>  
#include<cstdlib>  
#include<cmath>  
#include<iostream>  
#include<algorithm>  
#include<vector>  
#include<map>  
#include<set>  
#include<queue>  
#include<string>  
#include<bitset>  
#include<utility>  
#include<functional>  
#include<iomanip>  
#include<sstream>  
#include<ctime>  
using namespace std;
 
#define N int(1e2)  
#define inf int(0x3f3f3f3f)  
#define mod int(1e9+7)  
typedef long long LL;
 
 
#ifdef CDZSC  
#define debug(...) fprintf(stderr, __VA_ARGS__)  
#else  
#define debug(...)   
#endif  
 
char s[N][N];int n,m,vis[N][N];
 
int vx[] = { 0, 0, 1, -1 };
int vy[] = { 1, -1, 0, 0 };
 
struct point
{
	int dicx, dicy, step, x, y;
	point(int _dx, int _dy, int _s, int _x, int _y) : dicx(_dx), dicy(_dy), step(_s), x(_x), y(_y){}
	point(){}
};
 
bool judge(int x, int y)
{
	return (x >= 0 && x <= n + 1 && y >= 0 && y <= m + 1);
}
 
int bfs(int a, int b, int c, int d)
{
	int ans = inf;
	point top;
	memset(vis, 0, sizeof(vis));
	queue<point>q;
	q.push(point(0, 0, 0, a, b));
	vis[a][b] = 1;
	while (!q.empty())
	{
		int tx, ty, dx, dy, seg;
		top = q.front(); q.pop();
		if (top.x == c&&top.y == d)
		{
			ans = min(ans, top.step);
		}
		for (int i = 0; i < 4; i++)
		{
			dx = top.dicx;
			dy = top.dicy;
			tx = top.x+vx[i];
			ty = top.y+vy[i];
			seg = top.step;
			if (!judge(tx, ty))
			{
				continue;
			}
			if (vis[tx][ty] || s[tx][ty] == 'X')
			{
				continue;
			}
			vis[tx][ty] = 1;
			if (vx[i] == dx&&vy[i] == dy)
			{
				q.push(point(dx, dy, seg, tx, ty));
			}
			else
			{
				q.push(point(vx[i], vy[i], seg+1, tx, ty));
			}
		}
	}
	return ans;
}
 
int main()
{
#ifdef CDZSC  
	freopen("i.txt", "r", stdin);
	//freopen("o.txt","w",stdout);  
	int _time_jc = clock();
#endif
	int a,b,c,d,cass=0;
	while (~scanf("%d%d", &m, &n))
	{
		int cas = 0;
		if (n == 0 && m == 0)break;
		getchar();
		for (int i = 1; i <= n; i++)
		{
			gets(s[i] + 1);
			//puts(s[i]+1);
		}
		for (int i = 0; i <= m+1; i++)
		{
			s[0][i] = '0';
			s[n + 1][i] = '0';
		}
		for (int i = 0; i <= n+1; i++)
		{
			
			s[i][0] = '0';
			s[i][m + 1] = '0';
			s[i][m + 2] = '\0';
		}
		if (cass)puts("");
		printf("Board #%d:\n", ++cass);
		while (~scanf("%d%d%d%d", &a, &b, &c, &d))
		{
			if (a == 0 && b == 0 && c == 0 && d == 0)break;
			s[d][c] = '0';
			int ans = bfs(b, a, d, c);
			
			if (ans!=inf)
				printf("Pair %d: %d segments.\n", ++cas,ans);
			else
				printf("Pair %d: impossible.\n", ++cas);
			s[d][c] = 'X';
		}
	}
#ifdef CDZSC  
	debug("time: %d\n", int(clock() - _time_jc));
#endif  
	return 0;
}       