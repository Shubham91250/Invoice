from django.db import models

# Create your models here.

class Client_detail(models.Model):
    company_name = models.CharField(max_length=100)
    gst_number=models.CharField(max_length=50)
    country=models.CharField(max_length=23)
    state=models.CharField(max_length=23)
    address=models.CharField(max_length=34)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self)->str:
        return self.company_name

class Add_Service(models.Model):
    client= models.ForeignKey(Client_detail, on_delete=models.CASCADE)
    description=models.CharField(max_length=45)
    quantity=models.IntegerField()
    amount=models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self)->str:
        return f"{self.description},'client:'{self.client}"
    
class AddService(models.Model):
    client= models.ForeignKey(Client_detail, on_delete=models.CASCADE,related_name='AddService',blank=True,null=True)
    company_name=models.CharField(max_length=200)
    handle_by=models.CharField(max_length=200)
    email=models.CharField(max_length=80)
    phone=models.IntegerField()
    account_number=models.IntegerField()
    ifsc_code=models.CharField(max_length=20)
    bank=models.CharField(max_length=20)
    gst_number=models.CharField(max_length=20)
    


    def __str__(self):
        return f"{self.client} -- {self.handle_by}"
            