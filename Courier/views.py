from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Courier
from .forms import CourierForm

def courier_list(request):
    couriers = Courier.objects.all()
    return render(request, 'couriers/courier_list.html', {'couriers': couriers})

def courier_detail(request, pk):
    courier = get_object_or_404(courier, pk=pk)
    return render(request, 'courier/courier_detail.html', {'courier': courier})

def courier_new(request):
    if request.method == "POST":
        form = CourierForm(request.POST)
        if form.is_valid():
            courier = form.save(commit=False)
            courier.save()
            return redirect('courier_detail', pk=courier.pk)
    else:
        form = CourierForm()
    return render(request, 'couriers/courier_edit.html', {'form': form})

def courier_edit(request, pk):
    courier = get_object_or_404(courier, pk=pk)
    if request.method == "POST":
        form = CourierForm(request.POST, instance=courier)
        if form.is_valid():
            courier = form.save(commit=False)
            courier.save()
            return redirect('courier_detail', pk=courier.pk)
    else:
        form = CourierForm(instance=courier)
    return render(request, 'couriers/courier_edit.html', {'form': form})

def courier_delete(request, pk):
    courier = get_object_or_404(courier, pk=pk)
    if request.method == "POST":
        courier.delete()
        return redirect('courier_list')
    return render(request, 'couriers/courier_confirm_delete.html', {'courier': courier})
