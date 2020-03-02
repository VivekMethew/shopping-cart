from django.db import models

# Create your models here.

class ProductDetail(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    img = models.ImageField(upload_to="shop/pics")
    category = models.CharField(max_length=50)
    subcategory = models.CharField(max_length=50)
    desc = models.CharField(max_length=300)
    ProductPrice = models.IntegerField()
    pub_data = models.DateField()

    def __str__(self):
        return self.product_name


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")
    
    def __str__(self):
        return self.name

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    item_json = models.CharField(max_length=5000, default="")
    name = models.CharField(max_length=90, default="")
    amount = models.IntegerField(default=0)
    email = models.CharField(max_length=100, default="")
    address = models.CharField(max_length=100, default="")
    city = models.CharField(max_length=100, default="")
    state = models.CharField(max_length=100, default="")
    zip_code = models.CharField(max_length=50, default="")
    phone = models.CharField(max_length=20, default="")

class orderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default=0)
    update_desc = models.TextField()
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:10] + "..."




