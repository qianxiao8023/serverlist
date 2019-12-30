from django.db import models
from django.utils import timezone


# Create your models here.
class servertest(models.Model):
    ip_adress = models.CharField(max_length=20, primary_key=True)
    server_location = models.CharField(max_length=30)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

class login(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    # 服务器IP
    # 服务器所在地
    # 创建时间
    # 更新时间


