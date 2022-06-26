from django.db import models
# Create your models here.
class bankname(models.Model):
    bankname=models.CharField(max_length=20)
    #id=models.IntegerField(primary_key=True)
    def __str__(self):
        return '{0.bankname}'.format(self)
class Atm(models.Model):
    #bankname=models.CharField(max_length=20)
    available=models.DecimalField(decimal_places=2,max_digits=9)
    relate=models.ForeignKey(bankname,on_delete=models.CASCADE)
    location=models.CharField(max_length=15)
    def __str__(self):
        return '{0.available}{0.relate}'.format(self)
class users(models.Model):
    userid=models.CharField(max_length=12)
    account=models.CharField(max_length=30)
    cash=models.DecimalField(decimal_places=2,max_digits=9)
    ifsc=models.CharField(max_length=15)
    username=models.CharField(max_length=20)
    relate=models.OneToOneField(bankname,on_delete=models.CASCADE)
    def __str__(self):
        return '{0.userid}{0.account}{0.cash}{0.ifsc}{0.username}{0.relate}'.format(self)