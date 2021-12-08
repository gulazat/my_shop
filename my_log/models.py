from django.db import models

# Create your models here.


class Customer(models.Model):
    customer_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    email = models.EmailField()
    time_created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.customer_name


class Product(models.Model):
    CATEGORY = (
        ('Indoor','Indoor'),
        ('Outdoor','Outdoor')
    )

    product_name = models.CharField(max_length=30)
    price = models.CharField(max_length=30)
    category = models.CharField(max_length=30, choices=CATEGORY)
    description = models.TextField(blank=True,null=True)
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name

class Order(models.Model):
    STATUS = (
        ('pending','pending'),
        ('out for dilivert','out for delivery'),
        ('Deivered','Delivered')
    )
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='c_order')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='p_order')
    time_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=30,choices=STATUS)


class Add(models.Model):
    title = models.CharField(max_length=128, verbose_name='广告标题')
    description = models.TextField(max_length=256, blank=True, null=True, verbose_name='广告描述')
    img = models.ImageField(upload_to='blog_images', null=True, blank=True, verbose_name='广告图')
    callback_url = models.URLField(null=True,blank=True,verbose_name='网络URL')
    time_created = models.DateTimeField(auto_now_add=True,verbose_name='发布时间')
    index = models.IntegerField(default=999,verbose_name='排序')
    location = models.CharField(max_length=50,verbose_name='位置')
    is_display = models.BooleanField(default=False,verbose_name='是否显示')


    class Meta:

        verbose_name = "广告"
        verbose_name_plural = '广告'


    def __str__(self):
        return self.title