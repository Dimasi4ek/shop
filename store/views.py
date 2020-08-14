from django.shortcuts import render


def store(request):
    context = {}
    return render(request, 'store/index.html', context)


def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)


def about(request):
    context = {}
    return render(request, 'store/about.html', context)


def blog(request):
    context = {}
    return render(request, 'store/blog.html', context)


def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)


def confirmation(request):
    context = {}
    return render(request, 'store/confirmation.html', context)


def contact(request):
    context = {}
    return render(request, 'store/contact.html', context)


def product_details(request):
    context = {}
    return render(request, 'store/product_details.html', context)


def login(request):
    context = {}
    return render(request, 'store/login.html', context)


def shop(request):
    context = {}
    return render(request, 'store/shop.html', context)


def contact(request):
    context = {}
    return render(request, 'store/contact.html', context)