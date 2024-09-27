from django.shortcuts import render, get_object_or_404, redirect
from .models import Cart, CartItem
from main.models import Book


def cart_detail(request):
    cart = Cart.objects.get(user=request.user)
    return render(request, 'cart/cart.html', {'cart': cart})


def add_to_cart(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, book=book)

    if not created:
        cart_item.quantity += 1
    cart_item.save()

    return redirect('cart:cart')


def remove_from_cart(request, book_id):
    cart = Cart.objects.get(user=request.user)
    cart_item = get_object_or_404(CartItem, cart=cart, book_id=book_id)
    cart_item.delete()
    return redirect('cart:cart')