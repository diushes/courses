from django.db import models

CONTACT_CHOICES = (('FACEBOOK', 'Facebook'),
                   ('PHONE', 'Phone'),
                   ('EMAIL', 'Email'),)
class Contact(models.Model):
    choice = models.CharField(max_length=50, choices=CONTACT_CHOICES, default="PHONE", unique=True, )
    def __str__(self):
        return self.choice

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    imgpath = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    logo = models.CharField(max_length=100)
    contact = models.ForeignKey(Contact, related_name="contact", on_delete=models.CASCADE, null=False, to_field="choice",)
    category = models.ForeignKey(Category, related_name="category", on_delete=models.CASCADE, null=False, to_field="name",)


    def __str__(self):
        return self.name

class Branch(models.Model):
    latitude = models.CharField(max_length=100)
    longtitude = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    course = models.ForeignKey(Course, related_name="branches", on_delete=models.CASCADE, null=False)
    def __str__(self):
        return self.address



