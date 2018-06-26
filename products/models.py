from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    title = models.CharField(max_length=255)
    url = models.TextField()
    body = models.TextField()
    pub_date =  models.DateTimeField()
    votes_total = models.IntegerField(default=1)
    image = models.ImageField(upload_to="images/", blank=True)
    icon = models.ImageField(upload_to="images/", blank=True)

    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    def pub_date_pretty(self):
        return self.pub_date.strftime('%d-%b-%Y')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]
