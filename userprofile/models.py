from django.db import models

class Users(models.Model):
    user_id = models.IntegerField(default=0, verbose_name="管理员ID")
    name = models.CharField(max_length=80, verbose_name='员工姓名')
    vip = models.BigIntegerField(default=1, verbose_name='VIP等级')
    openid = models.CharField(max_length=100, verbose_name='OPENID')
    appid = models.CharField(max_length=100, verbose_name='APPID')
    is_delete = models.BooleanField(default=False, verbose_name='删除标签')
    developer = models.BooleanField(default=True, verbose_name='开发者标签')
    t_code = models.CharField(max_length=100, verbose_name='交易代码')
    ip = models.CharField(max_length=100, verbose_name='注册IP')
    vip_time = models.DateTimeField(auto_now_add=True, verbose_name='VIP时间')
    link_to = models.BooleanField(default=False, verbose_name='链接到')
    link_to_id = models.BigIntegerField(default=0, verbose_name='链接到ID')
    avatar = models.CharField(max_length=100, default='/static/img/user.jpg', verbose_name='员工头像')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        db_table = 'user_profile'
        verbose_name = '用户档案'
        verbose_name_plural = "用户档案"
        ordering = ['-id']
