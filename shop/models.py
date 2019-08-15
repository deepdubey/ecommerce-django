from django.db import models

class Product(models.Model):
    pr_id=models.IntegerField(primary_key=True)
    pr_logo=models.CharField(max_length= 400)
    pr_title= models.CharField(max_length= 200)
    pr_price= models.IntegerField()
    pr_offer= models.CharField(max_length=30)

    def __str__(self):
        return '{0} : {1}'.format(self.pr_id,self.pr_title)
