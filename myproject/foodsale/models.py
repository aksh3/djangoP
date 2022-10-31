from django.db import models                              
class foodsale(models.Model):
    OrderDate = models.DateField(auto_now_add=True)
    Region = models.CharField(max_length=120)
    City = models.CharField(max_length=120)
    Category = models.CharField(max_length=120)
    Product = models.CharField(max_length=120)
    Quantity = models.IntegerField()
    UnitPrice = models.FloatField()
    class Meta:  
        db_table = "foods" 