from django.db import models

# Create your models here.

class Business(models.Model):
    caption = models.CharField(max_length=32)
    code = models.CharField(max_length=16, default='SA')


class Host(models.Model):
    # 自动生成id主键列 不写的话
    nid = models.AutoField(primary_key=True) # 自增
    hostname = models.CharField(max_length=32, db_index=True)
    ip = models.GenericIPAddressField(protocol='ipv4', db_index=True)  # ip类型实际是Char,默认支持ipv4,ipv6，可以指定protocol='ipv4'
    port = models.IntegerField()
    # 主机分配业务线
    b = models.ForeignKey(to='Business', to_field='id', on_delete=True)


class Application(models.Model):
    name = models.CharField(max_length=32)
    r = models.ManyToManyField("Host")

# class HostToApp(models.Model):
#     hobj = models.ForeignKey(to='Host', to_field='nid', on_delete=True)
#     aobj = models.ForeignKey(to='Application', to_field='id', on_delete=True)
#
