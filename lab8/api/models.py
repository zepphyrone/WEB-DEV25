from django.db import models

class Category(models.Model):

    name = models.CharField(max_length=500)

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}"

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    descripion = models.TextField()
    count = models.IntegerField()
    is_active = models.BooleanField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"name:{self.name},price:{self.price},description:{self.descripion},count:{self.count},is_active:{self.is_active},category:{self.category.name}"
    
    def to_json(self):
        return {
            'name':self.name,
            'price':self.price,
            'description':self.descripion,
            'count':self.count,
            'is_active':self.is_active,
            'category':self.category.to_json()
        }
    
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"