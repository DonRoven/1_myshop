from django.db import models
from shop.models import Product


class Order(models.Model):
    first_name = models.CharField(verbose_name="Ім'я", max_length=50)
    last_name = models.CharField(verbose_name='Прізвище', max_length=50)
    email = models.EmailField(verbose_name='Email')
    address =  models.CharField(verbose_name='Адреса', max_length=250)
    postal_code = models.CharField(verbose_name='Почтовий індекс', max_length=20)
    city = models.CharField(verbose_name='Місто', max_length=100)
    created = models.DateTimeField(verbose_name='Створений', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Оновлений', auto_now=True)
    paid = models.BooleanField(verbose_name='Оплачений', default=False)

    class Meta:
        ordering = ('-created', )
        verbose_name = 'Заказ'
        verbose_name_plural = 'Закази'

    def __str__(self):
        return 'Заказ: {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items')
    product = models.ForeignKey(Product, related_name='order_items')
    price = models.DecimalField(verbose_name='Ціна', max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(verbose_name='Кількість', default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity