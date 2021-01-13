from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User

class UserStatus(models.Model):
    user=models.ForeignKey(User, blank=True, on_delete=models.PROTECT)
    categories_status=models.BooleanField("categories status",default=True)
    product_status=models.BooleanField("product status",default=True)
    client_status=models.BooleanField("Clients status",default=True)
    order_status=models.BooleanField("order status",default=True)


class All_categories(models.Model):
    name = models.CharField(("Categories name"), max_length=120)
    status = models.BooleanField("status",default=False)

    def __str__(self):
        return self.name


class Categories(models.Model):
    all_categories=models.ForeignKey(All_categories,blank=True, on_delete=models.CASCADE)
    name = models.CharField(("Categories name"), max_length=120)
    status = models.BooleanField("status",default=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(("Product name"), max_length=120)
    price =models.FloatField('price',null=True, blank=True, default=None)
    debt = models.FloatField('debt',null=True, blank=True, default=None)
    categoriya_id = models.ForeignKey(Categories, blank=True, on_delete=models.CASCADE)
    count = models.IntegerField('count')
    def __str__(self):
        return self.name


class Cilent(models.Model):
    FIO = models.CharField(("FIO"), max_length=120)
    phone = PhoneNumberField("phone_number")
    tg_number = models.CharField("tg username or phone number",max_length=20)

    def __str__(self):
        return self.FIO

class Order(models.Model):
    product_id=models.ForeignKey(Product,blank=True,on_delete=models.PROTECT)
    cilent_id=models.ForeignKey(Cilent,blank=True,on_delete=models.CASCADE)
    count=models.CharField('Count',max_length=10)
    sum=models.FloatField('summa',null=True, blank=True, default=None)
    order_date=models.DateTimeField('qarz olgan vaqti',auto_now_add=True)
