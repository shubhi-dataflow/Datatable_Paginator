from django.db import models

# Create your models here.


class Employees(models.Model):
    name = models.CharField(max_length=400,default=None, null=True, blank=True)
    position = models.CharField(max_length=400, null=True, blank=True)
    photo = models.FileField(upload_to='', null=False, blank=False)
    age = models.CharField(max_length=400, null=True, blank=True)
    salary = models.CharField(max_length=400, null=True, blank=True)
    office = models.CharField(max_length=250, null=False, blank=False)


                      # 'id': row['id'],
                        # 'name': row['Name of Hospital'],
                        # 'position': row['Address'],
                        # 'age': row['City'],
                        # 'salary': row['State'],
                        # 'office': row['Country'],
                        # 'Contact no.': row['Contact no.'],
                        # 'Email': row['Email'],
                        # 'Number of Doctors': row['Number of Doctors'],
                        # 'Number of Nurses': row['Number of Nurses'],
                        # 'Number of Beds': row['Number of Beds'],
                        # 'Number of ICU Beds': row['Number of ICU Beds'],
                        # 'Available Departments': row['Available Departments'],
                        # 'Source': row['Source'],