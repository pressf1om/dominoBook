from django.db import models
from django.contrib.auth.models import User
from main.models import Book

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart')
    created_at = models.DateTimeField(auto_now_add=True)

    def get_total_price(self):
        return sum(item.book.price * item.quantity for item in self.items.all())

    def __str__(self):
        return f"Корзина пользователя: {self.user.username}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.book.title} (x{self.quantity})"


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')  # связывает заказ с пользователем
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)  # общая стоимость заказа

    def __str__(self):
        return f'Заказ {self.id} пользователя {self.user.username}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')  # связывает товар с заказом
    book = models.ForeignKey(Book, on_delete=models.CASCADE)  # связывает товар с моделью книги
    quantity = models.PositiveIntegerField()  # кол-во заказанных единиц товара
    price = models.DecimalField(max_digits=10, decimal_places=2)  # цена на момент заказа

    def __str__(self):
        return f"{self.book.title} x {self.quantity}"

    def get_total_price(self):
        return self.price * self.quantity  # общая стоимость для товара в заказе
