"""OJ判题"""

import time
import requests

debug = True

class OJ:
    """判题基类"""

    def __init__(self, account, timeout, time_interval):
        """初始化登录会话"""
        self.username = account["username"]
        self.password = account["password"]
        self.timeout = timeout
        self.time_interval = time_interval
        self.session = requests.session()

    def judge(self, pid, language, code):
        """核心判题方法"""

        # 登录
        if debug:
            print("Login...", end="")
        time.sleep(self.time_interval)
        self.login()

        if debug:
            print("getting old runid...", end="")
        time.sleep(self.time_interval)
        runid_old = self.get_last_runid()
        if debug:
            print(runid_old)

        if debug:
            print("submitting...", end="")
        time.sleep(self.time_interval)
        self.submit(pid, language, code)
        n = 0
        while True:
            if debug:
                print("Getting new runid...")
            time.sleep(self.time_interval)
            runid = self.get_last_runid()

            if runid != runid_old:
                break
    
            n += 1
            if n == 10:
                raise SubmitError

        if debug:
            print("Get new runid:", runid)
        while True:
            # 获取结果
            if debug:
                print("getting result...", end="")
            time.sleep(self.time_interval)
            result, timeused, memoryused = self.get_result(runid)
            if debug:
                print(result)

            # 若判题结果为 Waiting / Judging / Compiling / ...
            # 继续获取
            if "ing" in result:
                continue

            return runid, result, timeused, memoryused
    def login(self):
        """登录
        使用self.ssession登录维持登录状态
        失败抛出LoginError
        """
        raise NotImplementedError

    def submit(self, pid, language, code):
        """提交代码
        使用self.session提交代码等数据
        失败抛出SubmitError
        """
        raise NotImplementedError

    def get_last_runid(self):
        """获取本账号最近一次提交记录的runid
        成功返回runid
        失败抛出NoMatchError
        """
        raise NotImplementedError

    def get_result(self, runid):
        """判题结果
        使用runid获取并匹配判题结果
        返回 result timeused memoryused
        匹配不到结果时抛出NoMatchError
        """
        raise NotImplementedError

    def get_compile_error_info(self, runid):
        """编译错误信息
        发生编译错误时 调用该方法使用runid获取并返回远程编译错误信息
        匹配不到信息时抛出NoMatchError
        """
        raise NotImplementedError

class NoMatchError(Exception):
    """没有匹配到数据"""
    pass

class LoginError(Exception):
    """登录失败"""
    pass

class SubmitError(Exception):
    """提交失败"""
    pass