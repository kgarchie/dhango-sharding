from django.db import models
from django_multitenant.models import TenantModel
from django_multitenant.fields import TenantForeignKey

# Create your models here.
class Store(TenantModel):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    email = models.EmailField()

    class TenantMeta:
        tenant_field_name = "id"

class Product(TenantModel):
    store = models.ForeignKey(Store)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    stock = models.SmallIntegerField()
    description = models.TextField()

    class Meta:
        unique_together = ['id', 'store']

    class TenantMeta:
        tenant_field_name = "store_id"

class Orders(TenantModel):
    store = models.ForeignKey(Store)
    product = TenantForeignKey(Product)

    class TenantMeta:
        tenant_field_name = "store_id"