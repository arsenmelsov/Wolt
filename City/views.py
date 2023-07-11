from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import City
from .forms import CityForm

def city_list(request):
    citys = City.objects.all()
    return render(request, 'cities/city_list.html', {'citys': citys})

def city_detail(request, pk):
    city = get_object_or_404(city, pk=pk)
    return render(request, 'cities/city_detail.html', {'city': city})

def city_new(request):
    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.save(commit=False)
            city.save()
            return redirect('city_detail', pk=city.pk)
    else:
        form = CityForm()
    return render(request, 'cities/city_edit.html', {'form': form})

def city_edit(request, pk):
    city = get_object_or_404(city, pk=pk)
    if request.method == "POST":
        form = CityForm(request.POST, instance=city)
        if form.is_valid():
            city = form.save(commit=False)
            city.save()
            return redirect('city_detail', pk=city.pk)
    else:
        form = CityForm(instance=city)
    return render(request, 'cities/city_edit.html', {'form': form})

def city_delete(request, pk):
    city = get_object_or_404(city, pk=pk)
    if request.method == "POST":
        city.delete()
        return redirect('city_list')
    return render(request, 'cities/city_confirm_delete.html', {'city': city})
