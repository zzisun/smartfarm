from django.db import models

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey('users.Users', verbose_name="user", on_delete=models.CASCADE)
    product = models.ForeignKey('product.Product', verbose_name="product", on_delete=models.CASCADE)
    ordered_date = models.DateTimeField(auto_now_add=True, verbose_name="order_date")
    quantity = models.IntegerField(verbose_name="quantity")

    def __str__(self):
        return str(self.user) + ' ' + str(self.product)

    class Meta:
        db_table = "Shoppingmall_Order"
        verbose_name = "order"
        verbose_name_plural = "order"