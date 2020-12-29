from django.db import models

# Create your models here.
class Testimonials(models.Model):
    name = models.CharField(max_length=100, default='', blank=True, null=True)
    client_image = models.ImageField(
        upload_to='testimonials/', default='', blank=True, null=True)
    client_testimonials = models.TextField(
        default='', blank=True, null=True)
    home_status = models.BooleanField(default=True)
    college_name =  models.CharField(max_length=100, default='', blank=True, null=True)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = 'testimonials'

    def __str__(self):
        return str(self.name)
