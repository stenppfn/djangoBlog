from django.db import models

# Create your models here.
class ListModel(models.Model):
    company_name = models.CharField(max_length=255, verbose_name="公司名称")
    company_city = models.CharField(max_length=255, verbose_name="公司城市")
    company_address = models.CharField(max_length=255, verbose_name="公司地址")
    company_contact = models.CharField(max_length=255, verbose_name="公司联系人")
    company_manager = models.CharField(max_length=255, verbose_name="公司经理")
    creater = models.CharField(max_length=255, verbose_name="创建人")
    openid = models.CharField(max_length=255, verbose_name="Openid")
    is_delete = models.BooleanField(default=False, verbose_name='删除标签')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name="更新时间")

    class Meta:
        db_table = 'company'
        verbose_name = '公司'
        verbose_name_plural = "公司"
        ordering = ['company_name']