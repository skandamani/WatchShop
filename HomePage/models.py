from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Watches(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class WatchesUploads(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    count = models.IntegerField(default=1)
    image = models.ImageField(upload_to="watch_images/")

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name} _ {self.price}" 


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(WatchesUploads)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class CartItem(models.Model):
    user = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True, blank=True )
    product= models.ForeignKey(WatchesUploads, on_delete=models.CASCADE)
    cart_count = models.IntegerField(default=1)


class WatchReview(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    product = models.ForeignKey(WatchesUploads, on_delete=models.CASCADE)
    review_text = models.TextField()
    rating = models.PositiveSmallIntegerField(choices= [(i,str(i)) for i in range(1,6)])

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

