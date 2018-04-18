from django.db import models


# Create your models here.
class comment(models.Model):
    airticle_id = models.ForeignKey('blogs.airticle')
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone_num = models.CharField(max_length=11)
    created_time = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()

    def __str__(self):
        return comment


