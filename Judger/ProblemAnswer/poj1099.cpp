#include<stdio.h>
#include<string.h>
#include <iostream>

using namespace std;
#define N 60

int x,y,n;
char mat[N][N];

struct node
{
    int num,id;
    int hang,lie;
} map[N][N];

void init()
{
    int i,j;
    memset(mat,0,sizeof(mat));
    for(i=1; i<=x; i++) //空格 和 '*'
    {
        for(j=1; j<=y; j++)
        {
            if(i==1 || i==x || j==1 || j==y) mat[i][j]='*';
            else mat[i][j]=' ';
        }
    }
    for(i=2; i<x; i=i+4) //H原子
    {
        for(j=2; j<y; j=j+4)
            mat[i][j]='H';
    }
    for(i=4; i<x; i=i+4) //H原子
    {
        for(j=4; j<y; j=j+4)
            mat[i][j]='H';
    }
    for(i=2; i<x; i=i+4) //O原子
    {
        for(j=4; j<y; j=j+4)
            mat[i][j]='O';
    }
}
void putmat()
{
    int i,j;
    for(i=1; i<=x; i++)
    {
        for(j=1; j<=y; j++)
            printf("%c",mat[i][j]);
        puts("");
    }
}
int main()
{
    int i,j,h,g,time=1;
    while(scanf("%d",&n),n)
    {
        if(time>1)puts("");
        memset(map,0,sizeof(map));
        y=4*n+3, x=4*n-1;//x行数,y列数
        for(i=1; i<=n; i++)
        {
            for(j=1; j<=n; j++)
            {
                scanf("%d",&map[i][j].num);
                map[i][j].id=n*(i-1)+j;
                map[i][j].hang=map[i][j].lie=map[i][j].num;
                map[i][j].hang+=map[i][j-1].hang;
                map[i][j].lie+=map[i-1][j].lie;
            }
        }

        init();
        int k=1;
        for(i=1; i<=x; i++)
        {
            for(j=1; j<=y; j++)
            {
                if(mat[i][j]=='O')
                {
                    int find=0;
                    for(h=1; h<=n; h++)
                    {
                        for(g=1; g<=n; g++)
                            if(map[h][g].id==k)
                            {
                                find=1,k++;
                                break;
                            }
                        if(find)break;
                    }
                    if(map[h][g].num==1) mat[i][j-1]='-',mat[i][j+1]='-';
                    else if(map[h][g].num==-1) mat[i-1][j]='|',mat[i+1][j]='|';
                    else if(map[h][g].num==0)
                    {
                        if(map[h][g].hang==0) mat[i][j-1]='-';
                        else if(map[h][g].hang==1) mat[i][j+1]='-';
                        if(map[h][g].lie==0) mat[i+1][j]='|';
                        else if(map[h][g].lie==1) mat[i-1][j]='|';
                    }
                }
            }
        }
        printf("Case %d:\n\n",time++);
        putmat();
    }
    return 0;
}