from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import ReccomendedFood
from .forms import ReccomendedFoodForm

def reccomendedFood_list(request):
    reccomendedFoods = ReccomendedFood.objects.all()
    return render(request, 'reccomendedFoods/reccomendedFood_list.html', {'reccomendedFoods': reccomendedFoods})

def reccomendedFood_detail(request, pk):
    reccomendedFood = get_object_or_404(reccomendedFood, pk=pk)
    return render(request, 'reccomendedFoods/reccomendedFood_detail.html', {'reccomendedFood': reccomendedFood})

def reccomendedFood_new(request):
    if request.method == "POST":
        form = ReccomendedFoodForm(request.POST)
        if form.is_valid():
            reccomendedFood = form.save(commit=False)
            reccomendedFood.save()
            return redirect('reccomendedFood_detail', pk=reccomendedFood.pk)
    else:
        form = ReccomendedFoodForm()
    return render(request, 'reccomendedFoods/reccomendedFood_edit.html', {'form': form})

def reccomendedFood_edit(request, pk):
    reccomendedFood = get_object_or_404(reccomendedFood, pk=pk)
    if request.method == "POST":
        form = ReccomendedFoodForm(request.POST, instance=reccomendedFood)
        if form.is_valid():
            reccomendedFood = form.save(commit=False)
            reccomendedFood.save()
            return redirect('reccomendedFood_detail', pk=reccomendedFood.pk)
    else:
        form = ReccomendedFoodForm(instance=reccomendedFood)
    return render(request, 'reccomendedFoods/reccomendedFood_edit.html', {'form': form})

def reccomendedFood_delete(request, pk):
    reccomendedFood = get_object_or_404(reccomendedFood, pk=pk)
    if request.method == "POST":
        reccomendedFood.delete()
        return redirect('reccomendedFood_list')
    return render(request, 'reccomendedFoods/reccomendedFood_confirm_delete.html', {'reccomendedFood': reccomendedFood})
