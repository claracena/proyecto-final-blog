from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
    comments = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

class Comments(models.Model):
    # user = 
    comment = models.CharField(max_length=255)
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.comment