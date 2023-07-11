from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Restaurant
from .forms import RestaurantForm

def rest_list(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'restaurants/restaurant_list.html', {'restaurants': restaurants})

def rest_detail(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    return render(request, 'restaurants/restaurant_detail.html', {'restaurant': restaurant})

def rest_new(request):
    if request.method == "POST":
        form = RestaurantForm(request.POST)
        if form.is_valid():
            restaurant = form.save(commit=False)
            restaurant.save()
            return redirect('user_detail', pk=restaurant.pk)
    else:
        form = RestaurantForm()
    return render(request, 'restaurants/restaurant_edit.html', {'form': form})

def rest_edit(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    if request.method == "POST":
        form = RestaurantForm(request.POST, instance=restaurant)
        if form.is_valid():
            restaurant = form.save(commit=False)
            restaurant.save()
            return redirect('user_detail', pk=restaurant.pk)
    else:
        form = RestaurantForm(instance=restaurant)
    return render(request, 'restaurants/restaurant_edit.html', {'form': form})

def rest_delete(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    if request.method == "POST":
        restaurant.delete()
        return redirect('rest_list')
    return render(request, 'restaurants/restaurant_confirm_delete.html', {'restaurant': restaurant})


