from django.shortcuts import render, get_object_or_404, redirect
from .models import Cart, CartItem, Order, OrderItem
from main.models import Book
from django.contrib.auth.decorators import login_required

@login_required
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)  # Создаем корзину, если ее нет
    return render(request, 'cart/cart.html', {'cart': cart})

@login_required
def add_to_cart(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    cart, created = Cart.objects.get_or_create(user=request.user)  # Создаем корзину, если ее нет
    cart_item, created = CartItem.objects.get_or_create(cart=cart, book=book)

    if not created:
        cart_item.quantity += 1
    cart_item.save()

    return redirect('cart:cart')

@login_required
def remove_from_cart(request, book_id):
    cart = Cart.objects.get(user=request.user)
    cart_item = get_object_or_404(CartItem, cart=cart, book_id=book_id)
    cart_item.delete()
    return redirect('cart:cart')


@login_required
def pay(request):
    cart = get_object_or_404(Cart, user=request.user)
    if not cart.items.exists():  # есть ли товары в корзине
        return redirect('cart:cart')

    if request.method == 'POST':
        order = Order.objects.create(  # создаем новый заказ
            user=request.user,
            total_price=cart.get_total_price(),
        )

        for item in cart.items.all():  # проходим по всем товарам в корзине и делаем записи в OrderItem для каждого
            OrderItem.objects.create(
                order=order,
                book=item.book,
                quantity=item.quantity,
                price=item.book.price,
            )
        cart.items.all().delete()  # удаляем все товары из корзины после оформления заказа
        return redirect('cart:profile')
    return redirect('cart:cart')

@login_required
def profile(request):
    orders = request.user.orders.all().order_by('-created_at')
    return render(request, 'cart/profile.html', {'orders': orders})
