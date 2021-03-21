from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=5)
    last_name = models.CharField(max_length=5)
    first_name_kana = models.CharField(max_length=10, null=True)
    last_name_kana = models.CharField(max_length=10, null=True)
    birth_day = models.DateTimeField(null=True)
    # joining_date = models.DateTimeField('date published')
    # leave_date = models.DateTimeField('date published')
    # country_of_citizenship = models.IntegerField()

    def __str__(self):
        return id + ":" + self.first_name + " " + self.last_name

    def getFullName(self):
        return self.first_name + self.last_name