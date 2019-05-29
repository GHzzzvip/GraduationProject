import urllib
import requests
import re

debug = 0
rule = {}

rule[0] = r'<div class="ptt" lang="en-US">(.*?[\s\S])</div>'
rule[1] = r'Description</p><div class="ptx" lang="en-US">(.*?[\s\S]*?)</div>'
rule[2] = r'Input</p><div class="ptx" lang="en-US">(.*?[\s\S]*?)</div>'
rule[3] = r'Output</p><div class="ptx" lang="en-US">(.*?[\s\S]*?)</div>'
rule[4] = r'Sample Input</p><pre class="sio">(.*?[\s\S]*?)</pre>'
rule[5] = r'Sample Output</p><pre class="sio">(.*?[\s\S]*?)</pre>'
s = ['Problem Title:\n','Description:\n','Input:\n','Output:\n','Sample Input:\n','Sample Output:\n']
def str_replace(match_str):
    import re
    if len(re.findall(r'src="', match_str)) > 0:
        return match_str.replace('src="', 'src="http://poj.org/')
    if len(re.findall(r"src='", match_str)) > 0:
        return match_str.replace("src='", "src='http://poj.org/")
    if len(re.findall(r"src=", match_str)) > 0:
        return match_str.replace("src=", "src=http://poj.org/")
    return match_str

def getProblem(id):
    
    url = "http://poj.org/problem?id="
    url = url + str(id)
    """
    #headers = {'User-Agent':
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
               'Chrome/70.0.3538.110 Safari/537.36'}
    
    #req = urllib.request.Request(url = url, headers = headers)
    #res = urllib.request.urlopen(req)
    #html = res.read().decode('utf-8')
    """
    return requests.get(url).text

def getPbInfo(id):
    res = []
    html = getProblem(id)
    """
    if debug:
        path='c:\\Users\\GHz\\Code\\Project\\Graduation_Project\\crawler\\Problems'
        t = open("%s\poj_test%s.txt" % (path, id), "a")"""

    try:

        for i in range(0,6):
            reg = []
            reg = re.compile(rule[i])
            match_str = re.findall(reg, html)[0]
            match_str = re.sub('<br>', '\r\n',match_str)
            match_str = str_replace(match_str)
            res.append(match_str)

            if debug:
                t.write(s[i])
                t.write(match_str)    
        if debug:
            t.close()
    except IndexError:
        pass
    return res