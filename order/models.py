from django.db import models


class Order(models.Model):
    user = models.ForeignKey('users.Users', verbose_name="user", on_delete=models.CASCADE)
    product = models.ForeignKey('product.Product', verbose_name="product", on_delete=models.CASCADE)
    ordered_date = models.DateTimeField(auto_now_add=True, verbose_name="order_date")
    quantity = models.IntegerField(verbose_name="quantity")
    amount = models.PositiveIntegerField(verbose_name="product_amount", default=0)
    STATUS_CHOICED = (('Proc','Processing'),('Ship','Shipped'),('On','On the way'),('Deli','Delivered'))
    status = models.CharField(max_length=4,verbose_name="status", choices=STATUS_CHOICED, default='Proc')

    def __str__(self):
        return str(self.user) + ' ' + str(self.product)

    class Meta:
        db_table = "Shoppingmall_Order"
        verbose_name = "order"
        verbose_name_plural = "order"

class Cart(models.Model):
    user = models.ForeignKey('users.Users', verbose_name="user", on_delete=models.CASCADE)
    product = models.ForeignKey('product.Product', verbose_name="product", on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name="quantity", default=1)
    amount = models.PositiveIntegerField(verbose_name="product_amount", default=0)
    def __str__(self):
        return str(self.user) + ' ' + str(self.product)