from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Country
from .forms import CountryForm

def country_list(request):
    countries = Country.objects.all()
    return render(request, 'countries/country_list.html', {'countries': countries})

def country_detail(request, pk):
    country = get_object_or_404(country, pk=pk)
    return render(request, 'country/country_detail.html', {'country': country})

def country_new(request):
    if request.method == "POST":
        form = CountryForm(request.POST)
        if form.is_valid():
            country = form.save(commit=False)
            country.save()
            return redirect('country_detail', pk=country.pk)
    else:
        form = CountryForm()
    return render(request, 'countries/country_edit.html', {'form': form})

def country_edit(request, pk):
    country = get_object_or_404(country, pk=pk)
    if request.method == "POST":
        form = CountryForm(request.POST, instance=country)
        if form.is_valid():
            country = form.save(commit=False)
            country.save()
            return redirect('country_detail', pk=country.pk)
    else:
        form = CountryForm(instance=country)
    return render(request, 'countries/country_edit.html', {'form': form})

def country_delete(request, pk):
    country = get_object_or_404(country, pk=pk)
    if request.method == "POST":
        country.delete()
        return redirect('country_list')
    return render(request, 'countries/country_confirm_delete.html', {'country': country})
