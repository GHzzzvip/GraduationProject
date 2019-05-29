#include <stdio.h>
int main()
{
    int a,b,m,t;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d",&m);
        b=0;
        for(int i=0;i<m;i++)
        {
            scanf("%d",&a);
            b+=a;
        }
        printf("%d\n",b);
    }
    return 0;
}