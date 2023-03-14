from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50, default="未命名")
    category = models.CharField(max_length=50, default="产品大厅")
    introduction = models.CharField(max_length=200, default="请至淘宝查看详细介绍")
    isCollection = models.BooleanField(default=False)
    image_url = models.CharField(max_length=100, default=
    "https://img.dpm.org.cn/Uploads/Picture/2016/12/29/s5864b06921de3.png"
                                 )
    product_url = models.CharField(max_length=100, default=
    "https://space.bilibili.com/594844283?spm_id_from=333.337.0.0"
                                   )

