from django.shortcuts import render, get_object_or_404, redirect
from .models import Problem, Status, Contest, Contest_Problem
from django.contrib.auth.decorators import login_required
from django.contrib import auth

from django.contrib.auth.models import AnonymousUser
import functools


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import time
import datetime
import sys
import os
sys.path.append(r'C:\Graduation_Project\spider')

import spider.main as spider
# Create your views here.



def home(request):
    return render(request, 'home.html')

# 题目列表


def problem(request):
    problems_all = Problem.objects.all()
    limit = 10
    paginator = Paginator(problems_all, limit)
    page = request.GET.get('page')
    try:
        problems = paginator.page(page)
    except PageNotAnInteger:
        problems = paginator.page(1)
    except EmptyPage:
        problems = paginator.page(paginator.num_pages)

    return render(request, 'problem.html', {'problems': problems})

# 题目描述


def problem_description(request, pk):
    problem = Problem.objects.get(id=pk)
    
    p_dsp = {}
    p_dsp['OJ'], p_dsp['ID'] = problem.p_oj, problem.p_id

    if request.method =="POST":
        p_dsp['Language'] = {
            "0": "C",
            "1": "C++",
            "2": "Java",
        }[request.POST['Language']]
        p_dsp['Code'] = request.POST['code']
        p_dsp['result'] = 'Queueing'
        p_dsp['username'] = request.user
        print(p_dsp['username'])
        obj = Status(p_oj=p_dsp['OJ'], p_id=p_dsp['ID'], p_result=p_dsp['result'], p_code=p_dsp['Code'],
                     Language=p_dsp['Language'], username=p_dsp['username'])
        obj.save()
    return render(request, 'problem_dsp.html', {'p_dsp': problem})

@login_required
def contest(request):
    if request.method == 'POST':
        msg = request.POST

        title = request.POST['title']
        time_start = request.POST['begintime']
        time_end = request.POST['endtime']
        description = request.POST['description']
        problem = request.POST['problem']
        if not problem:
            contests = Contest.objects.all()
            return render(request, 'contest.html', {'contests': contests})

        print('problem : %s' % problem)
        # print("title:%s\nbegintime:%s\nendtime:%s\ndescription:%s\nproblem:%s\n"%(title,time_start,time_end,description,problem))
        lst = []
        for i in problem.split('\r\n'):
            if i == '':
                continue
            j, p_title = i.split('|')
            poj, pid = j.split('-')
            lst.append([poj, pid, p_title])
        obj = Contest(c_title=title, time_start=time_start,
                      time_end=time_end, c_manager=request.user)
        obj.save()
        key = obj.pk
        for i in lst:
            tmp = Problem.objects.filter(p_oj=i[0], p_id=int(i[1])).count()
            if tmp > 0:
                Contest_Problem.objects.create(
                    p_oj=i[0], p_id=int(i[1]), p_title=i[2], c_id=key)
            else:
                #如果数据库中不存在 去爬取
                count, timeWait = 0, 1
                while True:
                    if count >= 3:
                        print("doesn't exist or Network interruption")
                        break

                    spider.storge_problem_information(i[0], int(i[1]))
                    if Problem.objects.filter(p_oj=i[0], p_id=int(i[1])).count() > 0:
                        break

                    else:
                        count += 1
                        time.sleep(timeWait)

                if count < 3:
                    Contest_Problem.objects.create(
                        p_oj=i[0], p_id=int(i[1]), p_title=i[2], c_id=key)

    contests = Contest.objects.all().order_by('-id')
    return render(request, 'contest.html', {'contests': contests})


def contestOverview(request, pk):
    c_Problems = Contest_Problem.objects.filter(c_id=pk)
    contest = Contest.objects.get(id=pk)
    Information = {
        'c_Problems': c_Problems,
        'contest': contest
    }
    return render(request, 'contestOverview.html', Information)


def contestProblemDetail(request, pk):
    "contestProblems.pk"
    """
    将contestProblem中的主键传递入函数
    在题库中查询题目相关信息
    """
    contestId = Contest_Problem.objects.get(id = pk).c_id
    p_dsp = {}
    if request.method == 'POST':
        

        sProblem = request.POST['problemInformation']
        lst = sProblem.split(':')
        p_dsp['OJ'], p_dsp['ID'] = lst[0].split('-')
        p_dsp['Language'] = {
            "0": "C",
            "1": "C++",
            "2": "Java",
        }[request.POST['Language']]
        p_dsp['code'] = request.POST['code']
        p_dsp['result'] = 'Queueing'
        p_dsp['username'] = request.user

        # print(p_dsp['OJ'],p_dsp['ID'],p_dsp['result'],p_dsp['code'],p_dsp['Language'],p_dsp['username'],pk)

        obj = Status(p_oj=p_dsp['OJ'], p_id=p_dsp['ID'], p_result=p_dsp['result'], p_code=p_dsp['code'],
                     Language=p_dsp['Language'], username=p_dsp['username'], contest_id=contestId)
        obj.save()

        contest = Contest.objects.get(id=contestId)
        cStatus = Status.objects.filter(contest_id=contestId)
        print(cStatus)
        cProblems = Contest_Problem.objects.filter(c_id=contestId)
        Information = {
            'cStatus': cStatus,
            'cProblems': cProblems,
            'contest': contest
        }
        return render(request, 'contestStatus.html', Information)

    c_problem = Contest_Problem.objects.get(id=pk)

    cProblems = Contest_Problem.objects.filter(c_id=contestId)
    contest = Contest.objects.get(id=contestId)
    problem_description = Problem.objects.get(
        p_oj=c_problem.p_oj, p_id=c_problem.p_id)
    Information = {
        'Problem': problem_description,
        'cProblems': cProblems,
        'contest': contest,
        'cProblemPk': c_problem.pk
    }
    return render(request, 'contestProblemDetail.html', Information)


def contestStatus(request, pk):
    print(pk)
    contest = Contest.objects.get(id=pk)
    cStatus = Status.objects.filter(contest_id=pk)
    print(cStatus)
    cProblems = Contest_Problem.objects.filter(c_id=pk)
    Information = {
        'cStatus': cStatus,
        'cProblems': cProblems,
        'contest': contest,
    }
    return render(request, 'contestStatus.html', Information)

"""
eq相等   ne、neq不相等，   gt大于， lt小于 gte、ge大于等于   lte、le 小于等于   not非   mod求模
def cmp_to_key(mycmp):
    'Convert a cmp= function into a key= function'
    class K:
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return K
"""
def cmp(x,y):
    if x["Accepted"] > y["Accepted"]:
        return 1
    elif x["Accepted"] < y["Accepted"]:
        return -1
    else:
        if x["Penalty"] < y["Penalty"]:
            return 1
        elif x["Penalty"] > y["Penalty"]:
            return -1
        else:
            return 0


def contestRank(request, pk):
    contest = Contest.objects.get(id = pk)
    cProblems = Contest_Problem.objects.filter(c_id = pk)
    cStatus = Status.objects.filter(contest_id=pk).reverse()

    contestRank = {}
    contestProblemDict = {} #标识题目
    mylst
    num = 0
    for i in cProblems:
        s = i.p_oj + '-' + str(i.p_id)

        contestProblemDict[s] = {
            "ID":s,
            "pos":num,
            "problemFirstAccept":False,
        }
        num += 1
    
    # 统计题目提交数目
    #print(cStatus)
    for status in cStatus:
        # 若用户没在rank表中 创建一个rank表
        if status.submitTime < contest.time_start or status.submitTime > contest.time_end:
            continue

        if status.username not in contestRank:
            contestRank[status.username] = {
                "username": status.username,
                "Penalty": datetime.timedelta(),
                "Problems": [],
                "Accepted": 0,
                "Total": 0,
            }
            for problem in cProblems:
                contestRank[status.username]["Problems"].append({
                    "firstAcceptTime": None,
                    "error":0,
                    "problemFirstAccept": False,
                })
        
        s = status.p_oj + '-' + str(status.p_id)
        numm = contestProblemDict[s]["pos"]
        if status.p_result == "Accepted":
            print(status.p_oj + '-' + str(status.p_id), end=":")
            print(status.p_result,end="_____if_____\n")
            if contestRank[status.username]["Problems"][numm]["firstAcceptTime"] == None:
                contestRank[status.username]["Problems"][numm]["firstAcceptTime"] = status.submitTime - contest.time_start
                # 记录第一次AC
                if contestProblemDict[s]["problemFirstAccept"] == False:
                    contestRank[status.username]["Problems"][numm]["problemFirstAccept"] = True
                    contestProblemDict[s]["problemFirstAccept"] = True
        else:
            print(status.p_oj + '-' + str(status.p_id), end=":")
            print(status.p_result,end="____else____\n")
            print(contestRank[status.username]["Problems"][numm]["firstAcceptTime"], end = " error time: ")

            if contestRank[status.username]["Problems"][numm]["firstAcceptTime"] == None:
                contestRank[status.username]["Problems"][numm]["error"] += 1

            print(contestRank[status.username]["Problems"][numm]["error"])
    
    # 计算罚时
    for user in contestRank:
        for problem in contestRank[user]["Problems"]:
            contestRank[user]["Total"] += problem["error"]
            if problem["firstAcceptTime"] != None:
                contestRank[user]["Total"] += 1
                contestRank[user]["Accepted"] += 1
                contestRank[user]["Penalty"] += problem["firstAcceptTime"] + problem["error"] * datetime.timedelta(minutes = 20)

    Rank = sorted(contestRank.values(), key=functools.cmp_to_key(cmp), reverse=True)
    
    for i in Rank:
        print(i["Total"])
    print(contestProblemDict)
    Information = {
        'cProblems': cProblems,
        'contest': contest,
        'Rank': Rank,
        'contestProblemDict':contestProblemDict,
    }
    return render(request, 'contestRank.html', Information)

def status(request):
    stat = Status.objects.all()
    return render(request, 'status.html', {"Status": stat})

def codeView(request, pk): 
    stat = Status.objects.get(id = pk)
    print(stat.p_oj, stat.p_id, stat.p_result, stat.p_code)
    return render(request, 'codeView.html', {"statusInfo":stat})

