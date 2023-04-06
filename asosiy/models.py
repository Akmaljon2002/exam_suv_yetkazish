from django.db import models
from rest_framework.authtoken.admin import User


class Suv(models.Model):
    brend = models.CharField(max_length=50)
    narx = models.PositiveIntegerField()
    litr = models.SmallIntegerField()
    batafsil = models.CharField(max_length=100)
    def __str__(self):
        return self.brend

class Mijoz(models.Model):
    ism = models.CharField(max_length=30)
    tel = models.CharField(max_length=15)
    manzil = models.CharField(max_length=30)
    qarz = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.ism

class Admin(models.Model):
    ism = models.CharField(max_length=30)
    yosh = models.SmallIntegerField()
    ish_vaqti = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.ism

class Haydovchi(models.Model):
    ism = models.CharField(max_length=30)
    tel = models.CharField(max_length=15)
    kiritilgan_sana = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.ism

class Buyurtma(models.Model):
    suv = models.ForeignKey(Suv, on_delete=models.CASCADE)
    vaqti = models.DateField(auto_now_add=True)
    mijoz = models.ForeignKey(Mijoz, on_delete=models.CASCADE)
    miqdor = models.PositiveIntegerField()
    umumiy_narxi = models.PositiveIntegerField()
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    haydovchi = models.ForeignKey(Haydovchi, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.suv}({self.admin})[{self.vaqti}]"