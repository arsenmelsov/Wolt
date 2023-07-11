from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Basket
from .forms import BasketForm

def basket_list(request):
    baskets = Basket.objects.all()
    return render(request, 'baskets/basket_list.html', {'baskets': baskets})

def basket_detail(request, pk):
    basket = get_object_or_404(basket, pk=pk)
    return render(request, 'basket/basket_detail.html', {'basket': basket})

def basket_new(request):
    if request.method == "POST":
        form = BasketForm(request.POST)
        if form.is_valid():
            basket = form.save(commit=False)
            basket.save()
            return redirect('basket_detail', pk=basket.pk)
    else:
        form = BasketForm()
    return render(request, 'baskets/basket_edit.html', {'form': form})

def basket_edit(request, pk):
    basket = get_object_or_404(basket, pk=pk)
    if request.method == "POST":
        form = BasketForm(request.POST, instance=basket)
        if form.is_valid():
            basket = form.save(commit=False)
            basket.save()
            return redirect('basket_detail', pk=basket.pk)
    else:
        form = BasketForm(instance=basket)
    return render(request, 'baskets/basket_edit.html', {'form': form})

def basket_delete(request, pk):
    basket = get_object_or_404(basket, pk=pk)
    if request.method == "POST":
        basket.delete()
        return redirect('basket_list')
    return render(request, 'baskets/basket_confirm_delete.html', {'basket': basket})
