from django.db import models
# Create your models here.
""" 
python manage.py makemigrations    在migrations目录下生成一个迁移文件，此时数据库中还没有生成数据表
python manage.py migrate           执行MySQL语句创建数据表
"""

#user表

#problem表
class Problem(models.Model):
    #自增id作主键
    p_oj = models.CharField(max_length=128)
    p_id = models.IntegerField()
    p_title = models.CharField(max_length=128)
    p_description = models.TextField()
    p_input = models.TextField()
    p_output = models.TextField()
    p_sampleinput = models.CharField(max_length=512)
    p_sampleoutput = models.CharField(max_length=512)
    p_url = models.CharField(max_length=128,null=True)
    
    def __str__(self):
        return self.p_title

class Status(models.Model):
    #自增id作主键
    p_oj = models.CharField(max_length=128)
    p_id = models.IntegerField()
    p_result = models.CharField(max_length=128)
    p_code = models.TextField()
    p_runid = models.IntegerField(null=True)
    p_timeused = models.IntegerField(null=True)
    p_memoryused  =models.IntegerField(null=True)
    Language = models.CharField(max_length=128)
    username = models.CharField(max_length=128)
    contest_id = models.IntegerField(null=True)
    submitTime = models.DateTimeField(auto_now_add=True)
    #problemInfo = models.ForeignKey(Problem)
    def __datetime__(self):
        return self.submitTime

    class Meta:
        ordering = ['-submitTime']
#每场contest信息
class Contest(models.Model):
    c_title = models.CharField(max_length=128)
    time_start = models.DateTimeField()
    time_end = models.DateTimeField()
    c_manager = models.CharField(max_length=128)
    def __str__(self):
        return self.c_title

class Contest_Problem(models.Model):
    p_oj = models.CharField(max_length=128)
    p_id = models.IntegerField()
    p_title = models.CharField(max_length=128, null=True)
    c_id = models.IntegerField()
    #probleiInfo = models.ForeignKey(Problem)
    def __str__(self):
        return self.p_oj

    
