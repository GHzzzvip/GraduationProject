#include<iostream>
#include<cstring>
using namespace std;
int main()
{
    string r;
    int n,dianwei;
    const int R_LEN=160;
    short result[R_LEN],jieguo[R_LEN],chengshu[6];
    while(cin>>r>>n)
    {
        int len=0;
        for(int i=0;i<R_LEN;++i) jieguo[i]=result[i]=0;
        for(int i=0;i<6;++i) chengshu[i]=0;
        dianwei = 0;
        size_t pos = r.find(".");
        if(pos != string::npos) dianwei=(5-pos)*n;
        for(int i=5,j=0;i>=0;--i)
        {
            if(r[i]!='.')
            {
                jieguo[j]=result[j]=chengshu[j]=r[i]-'0';
                ++j;
            }
        }
        while(n>=2)
        {
            --n;
            for(int i=0;i<R_LEN;++i) result[i]=0;
            for(int i=0;i<5;++i)
            {
                int c;
                for(int j=0;j<R_LEN;++j)
                {
                    if(chengshu[i]==0) break;
                    c=chengshu[i]*jieguo[j];
                    result[i+j]+=c;
                    for(int t=i+j;result[t]>9;++t)
                    {
                        result[t+1]+=result[t]/10;
                        result[t]=result[t]%10;
                    }
                }
            }
            for(int i=0;i<R_LEN;++i) jieguo[i]=result[i];
        }
        int firstindex=-1;
        for(int i=R_LEN-1;i>=dianwei;--i)
        {
            if(result[i]>0)
            {
                firstindex=i;
                break;
            }
        }
        int lastindex=-1;
        for(int i=0;i<dianwei;++i)
        {
            if(result[i]>0)
            {
                lastindex=i;
                break;
            }
        }
        if(firstindex!=-1)//输出小数点前的部分
        {
            while(firstindex>=dianwei)
            {
                cout<<result[firstindex];
                --firstindex;
            }
        }
        if(lastindex!=-1);
        {
            cout<<'.';
            --dianwei;
            while(dianwei>=lastindex)
            {
                cout<<result[dianwei];
                --dianwei;
            }
        }
        cout<<endl;
    }
}