from django.db import models

class Project(models.Model):
    message = models.TextField()

    def __str__(self):
        return self.message



class Achievement(models.Model):
    message = models.TextField()

    def __str__(self):
        return self.message


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    number = models.CharField(max_length=100)
    message = models.CharField(blank=True, max_length=500)

    def __str__(self):
        return self.email