import urllib
import requests
import re
debug = 0
rule = {}
rule[0] = r"<td align=center><h1 style='color:#1A5CC8'>(.*?[\s\S])</h1>"
rule[1] = r"Problem Description</div> <div class=panel_content>(.*?[\s\S]*?)</div>"
rule[2] = r"Input</div> <div class=panel_content>(.*?[\s\S]*?)</div>"
rule[3] = r"Output</div> <div class=panel_content>(.*?[\s\S]*?)</div>"
rule[4] = r'Sample Input</div><div class=panel_content><pre><div style="font-family:Courier New,Courier,monospace;">(.*?[\s\S]*?)</div>'
rule[5] = r'Sample Output</div><div class=panel_content><pre><div style="font-family:Courier New,Courier,monospace;">(.*?[\s\S]*?)</div>'

s = ['Problem Title','Problem Description','Input','Output','Sample Input','Sample Output']
def str_replace(match_str):
    return match_str.replace(r"src=", r"src=http://acm.hdu.edu.cn/")

def getProblem(id):
    url = "http://acm.hdu.edu.cn/showproblem.php?pid="
    url = url + str(id)
    return requests.get(url).text
    
def getPbInfo(id):
    res = []
    length = 0
    html = getProblem(id)
    try:

        for i in range(0,6):

            match_str = re.findall(rule[i], html)
            if match_str:
                res.append(str_replace(re.sub('<br>','\r\n',match_str[0])))
            else :
                length = length + 1
                res.append("NULL")
    except IndexError:
        pass

    return  [] if length == 6 else res



