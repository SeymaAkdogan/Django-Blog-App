from django.utils.timezone import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Nutrition_Record(models.Model):
    user_id = models.ForeignKey(User,blank=True,on_delete=models.CASCADE)
    day = models.IntegerField()
    repast = models.JSONField()
    created_at = models.DateTimeField(default=datetime.now(),blank=True)
    updated_at = models.DateTimeField(default=datetime.now(),blank=True)
    deleted_at = models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        super().save(*args,**kwargs)