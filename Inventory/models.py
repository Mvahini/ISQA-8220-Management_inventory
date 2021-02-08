from django.utils import timezone
from django.db import models


# Create your models here.
class ClientDetail(models.Model):
    client_first_name = models.CharField(max_length=50)
    client_last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=50)


    def __str__(self):
        return str(self.client_first_name)



# Create your models here.
class ProjectDetail(models.Model):
    project_title = models.CharField(max_length=50)
    description = models.CharField(max_length=100, blank=True)
    start_date = models.CharField(max_length=100)
    end_date = models.CharField(max_length=100)
    cost_estimation = models.IntegerField(blank=False, null=False)
    status = models.CharField(max_length=50)

    def __str__(self):
        return str(self.project_title)
