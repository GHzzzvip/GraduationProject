
import os
import sys
import django
import time

sys.path.append(r'C:\Graduation_Project')
os.chdir(r'C:\Graduation_Project')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Graduation_Project.settings")
django.setup()

from VirtualJudge.models import Problem

import support.spiderSdibt as SDIBT
import support.spiderPoj as POJ
import support.spiderHdu as HDU

# 传入传入OnlineJudge编号和题目编号
def storge_problem_information(poj, pid):
    # 查询此题目是否存在于数据库中，若存在爬虫模块调用结束
    tmp = Problem.objects.filter(p_oj=poj, p_id=pid).count()
    if tmp > 0:
        return
    else:
        # 根据OnlineJudge编号确定获取题目信息
        lst = {
            "HDU": HDU.getPbInfo(pid),
            "POJ": POJ.getPbInfo(pid),
            "SDIBT": SDIBT.getPbInfo(pid),
        }[poj]
        # lst列表存储了爬取题目的信息列表，若列表数据小于六项，证明该题目不存在
        if len(lst) < 6:
            print("The Problem %s-%d doesn't exist" %(poj,pid))
            return

        # 将获取的题目信息存储于数据库中，采集工作结束
        Problem.objects.create(p_oj=poj, p_id=pid, p_title=lst[0], p_description=lst[1],p_input=lst[2], p_output=lst[3], p_sampleinput=lst[4], p_sampleoutput=lst[5])

#if __name__ == "__main__":
#
##hdu 1012 缺少
#
#    for i in range(1000, 1020):
#        print("******%d******" % i)
#        storge_problem_information('SDIBT', i)
#        storge_problem_information('HDU', i)
#        storge_problem_information('POJ', i)
#        time.sleep(0.5)
"""
******1000******
******1001******
******1002******
******1003******
******1004******
******1005******
******1006******
******1007******
******1008******
******1009******
******1010******
******1011******
******1012******
The Problem HDU-1012 doesn't exist
******1013******
******1014******
******1015******
The Problem HDU-1015 doesn't exist
******1016******
******1017******
******1018******
******1019******

"""