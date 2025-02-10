from django.db import models

# Create your models here.

class destination(models.Model):
    name = models.CharField(max_length= 225)
    location = models.TextField()
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models. BooleanField(default=False)

    def __str__(self):
        return self.name

class Booking(models.Model):
    Name = models.CharField(max_length= 225)
    destination = models.ForeignKey(destination, on_delete=models.CASCADE)
    From = models.DateField()
    To = models.DateField()
    Price = models.IntegerField()

    def __str__(self) -> str:
        return super().__str__()