django == 1.11.4
python == 3.6.7


pip install django == 1.11.4
pip install django-widget-tweaks
测试账号：
jk15171230  z19971117


modify:
    spider:
        main.py:
            修改路径到当前项目所在路径
    judger：
        main.py:
            修改路径到当前项目所在路径
    VirtualJudge:
        views.py:
            修改路径到当前项目所在路径


signup:
	需要删除打印日志

	
            
备注:
1.31 更改：
problem_dsp.html: 重新创建一个submit post

2.1 添加：
代码查看功能

下一步更改：
1、添加分页功能
2、修复抓取sdibt编译错误结果的


#include "stdio.h"
int main()
{
	char printVector[200][200] = {'0'}; 
	int scanfVector[50][50];
	int scanfSide[10] = {0};
	int n = 0;
	int num = 0;
	int rankNum = 0; //记录O当前的行数
	while (scanf("%d", &n), n)
	{
		scanfSide[num++] = n;
		int i;
		for (i = 0; i < n; i++)
		{
			//rankNum ++; //记录当前列数
			int rowNum = 2; //记录O在当前行的列数
			int j;
			for (j = 0; j < n; j++)
			{
				scanf("%d", &scanfVector[i][j]);
				if (scanfVector[i][j] == 1)
				{
					printVector[rankNum][rowNum - 2] = 'H';
					printVector[rankNum][rowNum - 1] = '-';
					printVector[rankNum][rowNum] =     'O';
					printVector[rankNum][rowNum + 1] = '-';
					printVector[rankNum][rowNum + 2] = 'H';
				}
				else if (scanfVector[i][j] == -1)
				{
					if(rankNum - 2 < 0)
						continue;
					printVector[rankNum - 2][rowNum] = 'H';
					printVector[rankNum - 1][rowNum] = '|';
					printVector[rankNum][rowNum] =     'O';
					printVector[rankNum + 1][rowNum] = '|';
					printVector[rankNum + 2][rowNum] = 'H';
				}
				else if (scanfVector[i][j] == 0)//类型和他前一个字符有关
				{
					//朝下
					if (i == 0 || printVector[rankNum - 2][rowNum] == 'H')
					{
						//朝左
						if (j == 0 || printVector[rankNum][rowNum - 2] != 'H')
						{
							printVector[rankNum][rowNum - 2] = 'H';
							printVector[rankNum][rowNum - 1] = '-';
							printVector[rankNum][rowNum] = 'O';
							printVector[rankNum + 1][rowNum] = '|';
							printVector[rankNum + 2][rowNum] = 'H';
						}
						else
						{
							printVector[rankNum][rowNum + 2] = 'H';
							printVector[rankNum][rowNum + 1] = '-';
							printVector[rankNum][rowNum] = 'O';
							printVector[rankNum + 1][rowNum] = '|';
							printVector[rankNum + 2][rowNum] = 'H';
						}
					}
					else //朝上
					{
						if (rankNum - 2 < 0)
							continue;
						//朝左
						if (j == 0 || printVector[rankNum][rowNum - 2] != 'H')
						{
							printVector[rankNum - 2][rowNum] = 'H';
							printVector[rankNum - 1][rowNum] = '|';
							printVector[rankNum][rowNum] = 'O';
							printVector[rankNum][rowNum - 1] = '-';
							printVector[rankNum][rowNum - 2] = 'H';
						}
						else
						{
							printVector[rankNum - 2][rowNum] = 'H';
							printVector[rankNum - 1][rowNum] = '|';
							printVector[rankNum][rowNum] = 'O';
							printVector[rankNum][rowNum + 1] = '-';
							printVector[rankNum][rowNum + 2] = 'H';
						}
					}
				}
				rowNum += 4; //
			}
			if (i < n - 1)
				rankNum += 4;
			else
				rankNum++;
		}
	}


	int tempRank = 0;
	int rank = 0;
	int i;
	for (i = 0;i < num;i++)
	{
		printf("Case %d\n\n",i + 1);
		for (rank = tempRank; rank <= (scanfSide[i] - 1) * 4 + tempRank; rank++)
		{
			if(rank == tempRank)
			{
				int k;
				for (k = 0; k <= scanfSide[i] * 4 + 2; k++)
				{
					printf("*");
				}
				printf("\n");
			}
			printf("*");
			int row;
			for (row = 0; row <= scanfSide[i] * 4; row++)
			{
				if (printVector[rank][row] != '0')
					printf("%c", printVector[rank][row]);
				else
					printf(" ");
			}
			printf("*");
			printf("\n");
			if (rank == (scanfSide[i] - 1) * 4 + tempRank)
			{
				int k;
				for (k = 0; k <= scanfSide[i] * 4 + 2; k++)
				{
					printf("*");
				}
				printf("\n\n");
			}
		}
		tempRank = rank;
	}
	return 0;
}

