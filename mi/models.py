from django.db import models
from django.utils import timezone


# Create your models here.
class Client(models.Model):
    client_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=50)



    def __str__(self):
        return str(self.client_name)


class Project(models.Model):
    client_name = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='projects')
    project_title = models.CharField(max_length=50)
    description = models.CharField(max_length=100, blank=True)
    start_date = models.CharField(max_length=100)
    end_date = models.CharField(max_length=100)
    cost_estimation = models.IntegerField(blank=False, null=False)
    status_choice=[('Approved','Approved'),
            ('Pending','Pending'),
            ('Rejected','Rejected'),
            ]
    status = models.CharField(max_length=10, choices=status_choice)


    def __str__(self):
        return str(self.client_name)

