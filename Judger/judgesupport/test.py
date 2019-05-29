import re, requests
import time
def login():
    session = requests.session()
    session.post("http://acm.sdibt.edu.cn/JudgeOnline/login.php", data={
        "user_id": 'qqqqqq',
        "password": '123456',
        "submit": 'Submit',
    }, timeout = 2)
    
    r = session.get("http://acm.sdibt.edu.cn/JudgeOnline/",timeout = 2)
    r.encoding = 'utf8'
    #print(r.text)
    if 'qqqqqq' in r.text:
        print("Login success")
    
    # time.sleep(1)
    code = r"""#include <stdio.h> 

int main() 

{ 

    int a,b; 

    scanf("%d %d",&a, &b); 

    printf("%d\n",a+b); 

    return 0; 

}"""
    language = "C"
    pid = 1000
    """session.post("http://acm.sdibt.edu.cn/JudgeOnline/submit.php?id=%d" % pid, data={
        "id": pid,
        "language": {"C": 0, "C++": 1, "Java": 3},
        "source": code,
    }, timeout = 2)"""
    #time.sleep(2)
    r = session.get("https://acm.sdibt.edu.cn/JudgeOnline/status.php?user_id=qqqqqq", timeout = 2)
    r.encoding = 'utf-8'
    #print(r.text)
    match = re.findall(r"<tr align=center class='\w+'><td>(\d+?)<td>",r.text)
    
    runid = match[0]
    print(runid)
    match = re.findall(r"<tr align=center class='\w+'><td>"+str(runid)+"<td><a href='userinfo.php\?user=.+?'>.+?<\/a><td>[\s\S]+?<\/a><td>([\s\S]+?)<td>(\d+?) <font color=red>kb<\/font><td>(\d+?) <font color=red>ms<\/font>",r.text)
    #match1 = re.findall(r"<td><a href='userinfo.php\?user=(.+?)'>.+?<\/a><td>[\s\S]+?<\/a><td>([\s\S]+?)<td>", r.text)
    
    #(\d+?)[\s\S]+?<font color=red>ms<\/font>
    #match2 = re.findall(r"<td>(\d+?) <font color=red>kb<\/font><td>(\d+?) <font color=red>ms<\/font>",r.text)
    #print("+++++++match+++++++++")
    #print(match)
    print("+++++++match++++++++")
    print(match)
    match = re.findall(r"<font color=\w+?>(.+?)</font>",match[0][0])
    print(match)
    return match
if __name__ == "__main__":
    login()



    

