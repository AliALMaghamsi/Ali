from django.db import models

# Create your models here.

class Project(models.Model):
    class CategoryChoices(models.TextChoices):
        web_development="web_dev","Web Development"
        machince_learning="data","Data Science/Machine Learning"
        script="script","Scripts/Automation"
        personal_project="personal","Personal Project"


    title=models.CharField(max_length=64)
    description=models.TextField()
    technologies=models.CharField(max_length=512)
    completed_date=models.DateField()
    link=models.URLField()
    image=models.ImageField(upload_to="images/",blank=True,null=True)
    video=models.FileField(upload_to="videos/",blank=True,null=True)
    category=models.CharField(max_length=128,choices=CategoryChoices.choices,default="personal")
