import urllib
import requests
import re
#(.*?[\s\S]*?)
debug = 0
rule = {}

rule[0] = r"<center><h2>(.*?[\s\S]*?)</h2><span class=green>"
rule[1] = r"Description</h2><p>(.*?[\s\S]*?)</p>"
rule[2] = r"Input</h2><p>(.*?[\s\S]*?)</p>"
rule[3] = r"Output</h2><p>(.*?[\s\S]*?)</p>"
rule[4] = r'Sample Input</h2><pre>(.*?[\s\S]*?)</pre>'
rule[5] = r'Sample Output</h2><pre>(.*?[\s\S]*?)</pre>'

s = ['Problem Title','Description','Input','Output','Sample Input','Sample Output']

def str_replace(match_str):
    return match_str.replace(r'src="', r'src="http://acm.sdibt.edu.cn')

def getProblem(id):
    
    url = "http://acm.sdibt.edu.cn/JudgeOnline/problem.php?id="
    url = url + str(id)
    """headers = {'User-Agent':
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
               'Chrome/70.0.3538.110 Safari/537.36'}
    
    req = urllib.request.Request(url = url, headers = headers)
    res = urllib.request.urlopen(req)
    html = res.read().decode('utf-8')
    """
    return requests.get(url).text

def getPbInfo(id):
    res = []
    html = getProblem(id)
    """
    if debug:    
        path = 'c:\\Users\\GHz\\Code\\Project\\Graduation_Project\\crawler\\Problems'
        t = open("%s\sdibt_test%s.txt" % (path, id), "a")"""
    try:

        for i in range(0,6):
            reg = []
            reg = re.compile(rule[i])
            match_str = re.findall(reg, html)[0]
            match_str = str_replace(match_str)
            res.append(match_str)
    except IndexError:
        pass

    return res
    


