from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Notes(models.Model):                                          #once if the user is deeated, all the relate data of the users will 
    user=models.ForeignKey(User, on_delete=models.CASCADE)          #also be deleated due to foreignkey.
    title=models.CharField(max_length=200)
    description=models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "notes"                
        verbose_name_plural = "notes"       #verbose command is used to avoid the repetition of the 's' letter in the words....

class Homework(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    description=models.TextField()
    due = models.DateTimeField()
    is_finished=models.BooleanField(default=False)


    def __str__(self):
        return self.title

class Todo(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    is_finished = models.BooleanField(default=False)
    def __str__(self):
        return self.title


