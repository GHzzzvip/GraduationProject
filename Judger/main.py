import os
import sys
import django
import time

sys.path.append(r'C:\Graduation_Project')
os.chdir(r'C:\Graduation_Project')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Graduation_Project.settings")

django.setup()
import judgesupport
import judgesupport.sdibt
import judgesupport.poj
import judgesupport.hdu
from VirtualJudge.models import Status

accounts = {
    "SDIBT":{
        "username": "qqqqqq",
        "password": "123456",
    },
    "POJ":{
        "username": "jk15171230",
        "password": "123456",
    },
    "HDU":{
        "username": "jk15171230",
        "password": "123456",
    },
}
timeout = 3
time_interval = 0.5

def server():
    
    while True:
        record = Status.objects.filter(p_result='Queueing').order_by("submitTime").first()
        print("record->%s" % record)
        if not record:
            time.sleep(3)
            continue
        print("New Task: %s %d"%(record.p_oj, record.p_id))

        try:
            OJ = {
                "SDIBT":judgesupport.sdibt.Runner,
                "POJ":judgesupport.poj.Runner,
                "HDU":judgesupport.hdu.Runner,
            }[record.p_oj]
            record.p_runid, record.p_result, record.p_timeused, record.p_memoryused = OJ(accounts[record.p_oj], timeout, time_interval).judge(record.p_id, record.Language, record.p_code)
        except KeyError:
            #若不是三个OJ其中的一个 删除此条记录
            print("OJ not support %s" % record.p_oj)
            record.delete()
        except judgesupport.LoginError:
            # 登录失败 不做任何处理下次还会继续判这道题
            print("Login error")
        except judgesupport.SubmitError:
            # 提交失败
            print("Submit error")
        except judgesupport.NoMatchError as err:
            # 没有匹配到数据
            print("No match error: %s" % err)
        except Exception as err:
            # 未知错误
            print("Unknown error: %s" % err)
        
        else:
            record.save()
            print("更新成功")

if __name__ == "__main__":
    print("server->")
    server()