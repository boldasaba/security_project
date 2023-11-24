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
    
    def __str__(self):
        return f"{self.name}-{self.address}-{self.gender}-{self.birth_date}-{self.contact}-{self.grade}"

class Client(models.Model):
    name = models.CharField(max_length=40,verbose_name="Client Name")
    contact = models.CharField(max_length=15)
    address = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.name}-{self.contact}-{self.address}"
class Deployment(models.Model):
    Shift_Options = [
        ("M","Morning"),
         ("E","Evening"),
    ]
    deployment_date = models.DateField(auto_now=False)
    client= models.ForeignKey(Client,on_delete=models.CASCADE)  
    Shift = models.CharField(max_length=10,choices=Shift_Options)
    Officer = models.ForeignKey(Officer,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.deployment_date}-{self.client}-{self.Shift}-{self.Officer}"

class ClientPayment(models.Model):
    payment_date = models.DateField(auto_now=False)
    client = models.ForeignKey(Client,on_delete=models.CASCADE)
    payment_for = models.CharField(max_length=15)
    amount_paid = models.CharField(max_length=20) 
    def __str__(self):
        return f"{self.payment_date }-{self.client}-{self.payment_for}-{self.amount_paid}"             

    
 
