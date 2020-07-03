from django.db import models
from djongo.models.fields import ObjectIdField
from django.contrib.auth.models import User
from django.urls import reverse

class Profile(models.Model):

    _id = ObjectIdField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ips = models.Field(default=[])
    subprofiles = models.Field(default={})
    wallet = models.Field(choices=[(x, x) for x in range(1, 11)], default=0)
    profit = models.FloatField(default=0)

    def __str__(self):
        return f"{self.user}({self._id})"

class Order(models.Model):
    DROPDOWN = (
        ('BUY', 'BUY'),
        ('SELL', 'SELL'),
    )
    DROPDOWN2 = (
        ('NOT COMPLETED', 'NOT COMPLETED'),
        ('COMPLETED', 'COMPLETED'),
    )
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    position = models.Field(max_length=50, choices=DROPDOWN, default='')
    price = models.FloatField(default=0)
    quantity = models.FloatField(default=0)
    done = models.Field(max_length=50, choices=DROPDOWN2, default='NOT COMPLETED')

    def __str__(self):
        return f"Order {self.pk} : {self.quantity} BTC - {self.price}$ - {self.done} by {self.profile.user}({self.profile._id})"

    def get_absolute_url(self):
        return reverse('app-home')

