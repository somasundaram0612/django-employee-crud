from django.db import models

# Create your models here.

class Employee(models.Model):
    e_id = models.IntegerField()
    e_name = models.CharField(max_length=20)
    e_age = models.IntegerField()
    e_email = models.EmailField(unique=True)
    e_contact = models.CharField(max_length=10, unique=True)
    e_description = models.TextField()
    e_img = models.ImageField(upload_to='employees/', null=True, blank=True)

    def __str__(self):
        return "%s" %(self.e_name)
    
    class Meta:
        db_table = "employee"