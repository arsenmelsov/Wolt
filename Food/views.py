from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Food
from .forms import FoodForm

def food_list(request):
    foods = Food.objects.all()
    return render(request, 'foods/food_list.html', {'foods': foods})

def food_detail(request, pk):
    food = get_object_or_404(food, pk=pk)
    return render(request, 'food/food_detail.html', {'food': food})

def food_new(request):
    if request.method == "POST":
        form = FoodForm(request.POST)
        if form.is_valid():
            food = form.save(commit=False)
            food.save()
            return redirect('food_detail', pk=food.pk)
    else:
        form = FoodForm()
    return render(request, 'foods/food_edit.html', {'form': form})

def food_edit(request, pk):
    food = get_object_or_404(food, pk=pk)
    if request.method == "POST":
        form = FoodForm(request.POST, instance=food)
        if form.is_valid():
            food = form.save(commit=False)
            food.save()
            return redirect('food_detail', pk=food.pk)
    else:
        form = FoodForm(instance=food)
    return render(request, 'foods/food_edit.html', {'form': form})

def food_delete(request, pk):
    food = get_object_or_404(food, pk=pk)
    if request.method == "POST":
        food.delete()
        return redirect('food_list')
    return render(request, 'foods/food_confirm_delete.html', {'food': food})
