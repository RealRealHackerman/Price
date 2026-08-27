from django.shortcuts import render, get_object_or_404
from . import services
from . import models
def price(request):
    currencies = models.Currency.objects.filter(is_active=True)
    nobitex_data = services.get_nobitex_stats()
    tgju_keys = [
        currency.symbol
        for currency in currencies
        if currency.source == "tgju"
    ]
    tgju_data = {}
    if tgju_keys:
        tgju_data = services.get_tgju_stats(tgju_keys)

    prices = []
    for currency in currencies:
        price = services.get_price(currency , nobitex_data , tgju_data)
        if price:
            prices.append(price)
    return render(request, "Price/price.html", {"prices": prices})

def price_detail(request,symbol):
    currency = get_object_or_404(
        models.Currency,
        is_active=True,
        symbol=symbol
    )

    price = services.get_price_detail(currency)

    return render(request, "Price/price_detail.html", {"price": price,"currency": currency,})