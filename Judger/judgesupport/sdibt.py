"""acm.sdibt.edu.cn"""

import re

from . import OJ, NoMatchError, LoginError

class Runner(OJ):
    encoding = "utf8"

    def login(self):
        self.session.post("https://acm.sdibt.edu.cn/JudgeOnline/login.php", data={
            "user_id": self.username,
            "password": self.password,
            "submit": 'Submit',
        }, timeout = self.timeout)
        r = self.session.get("https://acm.sdibt.edu.cn/JudgeOnline/",timeout = self.timeout)
        r.encoding = self.encoding
        if self.username not in r.text:
            raise LoginError
        
    def submit(self, pid, language, code):
        self.session.post("https://acm.sdibt.edu.cn/JudgeOnline/submit.php?id=%d" % pid, data={
            "id": pid,
            "language": {"C": 0, "C++": 1, "Java": 3}[language],
            "source": code,
        }, timeout = self.timeout)
    
    def get_last_runid(self):
        r = self.session.get("https://acm.sdibt.edu.cn/JudgeOnline/status.php?user_id=%s" % self.username, timeout = self.timeout)
        r.encoding = self.encoding
        match = re.findall(r"<tr align=center class='\w+'><td>(\d+?)<td>",r.text)
        if not match:
            raise NoMatchError("runid")
        return int(match[0])
    
    def get_result(self, runid):
        print(runid)
        r = self.session.get("https://acm.sdibt.edu.cn/JudgeOnline/status.php?user_id=%s" % self.username, timeout = self.timeout)
        r.encoding = self.encoding
        #print(r.text)
        match = re.findall(r"<tr align=center class='\w+'><td>"+str(runid)+"<td><a href='userinfo.php\?user=.+?'>.+?<\/a><td>[\s\S]+?<\/a><td>([\s\S]+?)<td>(\d+?) <font color=red>kb<\/font><td>(\d+?) <font color=red>ms<\/font>",r.text)
        if not match:
            raise NoMatchError("result")
        memoryused, timeused = match[0][1], match[0][2]
        for i in match:
            for d in i:
                print("%s "%d,end='***')
            print()
        
        status = re.findall(r"<font color=\w+?>(.+?)</font>", match[0][0])
        if not status:
            status = re.findall(r"<font color=.*\w+?>(.+?)</font>", match[0][0])[0]
            
        else :
            status = status[0]
        return status, timeused, memoryused
    
    def get_compile_error_info(self, runid):
        r = self.session.get("https://acm.sdibt.edu.cn/JudgeOnline/ceinfo.php?sid=%s" % runid, timeout = self.timeout)
        r.encoding = self.encoding
        print(r.text)
        match = re.findall(r'<pre id="errtxt">([\s\S]+?)</pre>', r.text) 
        if not match:
            raise NoMatchError("errorinfo")
        return match[0]
    
