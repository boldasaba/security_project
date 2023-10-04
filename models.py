from django.db import models



class Officer (models.Model):
    
    Gender_options=[
            ("M","Male"),
            ("F","Female"),

    ]
    
    name = models.CharField(max_length=40, verbose_name="Officer_Name")
    address = models.CharField(max_length=40,null=True,blank=True,default="N/P")
    gender = models.CharField(max_length=2,choices=Gender_options)
    birth_date = models.DateField(auto_now=False)
    contact = models.CharField(max_length=15)
    grade = models.CharField(max_length=30)

class Client(models.Model):
    name = models.CharField(max_length=40,verbose_name="Client Name")
    contact = models.CharField(max_length=15)
    address = models.CharField(max_length=40)
class Deployment(models.Model):
    Shift_Options = [
        ("M","Morning"),
         ("E","Evening"),
    ]
    deployment_date = models.DateField(auto_now=False)
    client = models.ForeignKey(Client,on_delete=models.CASCADE)  
    Shift = models.CharField(max_length=10,choices=Shift_Options)
    Officer = models.ForeignKey(Officer,on_delete=models.CASCADE)

class ClientPayment(models.Model):
    payment_date = models.DateField(auto_now=False)
    client = models.ForeignKey(Client,on_delete=models.CASCADE)
    payment_for = models.CharField(max_length=15)
    amount_paid = models.CharField(max_length=20)              

    
 
