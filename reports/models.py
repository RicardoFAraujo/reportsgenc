# reports/models.py


from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Company(models.Model):
    name = models.CharField(max_length=100)




    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Report(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    embed_url = models.URLField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

