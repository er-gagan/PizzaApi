from django.db import models

# Create your models here.
class Pizza(models.Model):
    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Image = models.CharField(max_length=200)
    Desciption = models.TextField()
    Size = models.CharField(max_length=10)
    Category = models.CharField(max_length=10)
    def __str__(self):
        return self.Name+" "+self.Size+" "+self.Category
  
# user pizza@123
# pass  pizza@123