   #include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <cctype>
using namespace std;

#define LEFT  -1    // 左括号
#define RIGHT -2    // 右括号
#define MUL   -3    // *
#define ADD   -4    // +
#define SUB   -5    // -
#define OP    -6    // 有运算符
#define NONE  -10

const int maxn = 100;
char a[maxn];   // 原始的等式数据
int b[maxn];    // 伪表达式
int best[maxn]; // 存储答案
int op[maxn];   // 运算符在数组b中的位置
int bn;         // 数组b的项数
int iLeft;      // 等号左边的数
int possible;   // 是否有解
int apos, bpos, opos;   // 位置指针

// 跳过空格
void skipSpace(){
    while(a[apos] && a[apos] == ' ') apos++;
}

int compute(); //前向声明，间接递归
int bracket(){
    int sum;
    if(b[bpos] == LEFT){
        bpos++; // 跳过左括号
        sum = compute();    // 计算括号里面的值
        bpos++; // 跳过右括号
    }else sum = b[bpos++];    // 没有括号
    return sum;
}

int compute(){
    int sum = bracket();    // 右边第一个数
    while(b[bpos] == MUL || b[bpos] == ADD || b[bpos] == SUB){
        int operation = b[bpos++];     // 取出运算符
        int ret = bracket();    // 取下一个数
        switch(operation){
            case MUL: sum *= ret; break;
            case ADD: sum += ret; break;
            case SUB: sum -= ret; break;
        }
    }
    return sum;
}

void dfs(int dep){
    if(possible) return;
    if(dep == opos){
        bpos = 0;
        int iRight = compute();
        if(iRight == iLeft){
            possible = 1;
            for(int i = 0; i < bn; ++i) best[i] = b[i];
        }
        return;
    }

    b[op[dep]] = ADD; dfs(dep + 1);
    b[op[dep]] = SUB; dfs(dep + 1);
    b[op[dep]] = MUL; dfs(dep + 1);

}

int main(){
#ifndef ONLINE_JUDGE
freopen("data.in", "r", stdin);
#endif // ONLINE_JUDGE

    int _ = 1;
    while(gets(a) && strchr(a, '=')){
        possible = 0;
        for(int i = 0; i < maxn; ++i) b[i] = NONE;
        apos = 0;
        sscanf(a, "%d", &iLeft);    // '='左边的数
        while(a[apos] && isdigit(a[apos])) apos++;
        skipSpace();
        apos++; //跳过 '='
        bn = 0;
        opos = 0;
        while(skipSpace(), a[apos]){
            if(a[apos] == '('){ // 左括号
                b[bn++] = LEFT;
                apos++;
                continue;
            }
            if(a[apos] == ')'){ // 右括号
                b[bn++] = RIGHT;
                apos++;
            }else{
                sscanf(a + apos, "%d", &b[bn++]);   // 读取数字
                while(a[apos] && isdigit(a[apos])) apos++;
            }
            skipSpace();
            // 如果不是结尾和')'，则有一个运算符
            if(a[apos] && a[apos] != ')'){
                op[opos++] = bn;
                b[bn++] = OP;
            }
        }

        dfs(0);
        printf("Equation #%d:\n", _++);
        if(!possible || !bn){
            printf("Impossible\n");
        }else if(bn == 1 && iLeft == b[0]){
            printf("%d=%d\n", iLeft, iLeft);
        }else{
            printf("%d=", iLeft);
            for(int i = 0; i < bn; ++i){
                switch(best[i]){
                    case ADD:   printf("+"); break;
                    case SUB:   printf("-"); break;
                    case MUL:   printf("*"); break;
                    case LEFT:  printf("("); break;
                    case RIGHT: printf(")"); break;
                    default :   printf("%d", b[i]); break;
                }
            }
            printf("\n");
        }
        printf("\n");
    }

    return 0;
}