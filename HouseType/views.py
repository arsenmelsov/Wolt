from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import houseType
from .forms import HouseTypeForm

def houseType_list(request):
    houseTypes = houseType.objects.all()
    return render(request, 'houseTypes/houseType_list.html', {'houseTypes': houseTypes})

def houseType_detail(request, pk):
    houseType = get_object_or_404(houseType, pk=pk)
    return render(request, 'houseTypes/houseType_detail.html', {'houseType': houseType})

def houseType_new(request):
    if request.method == "POST":
        form = HouseTypeForm(request.POST)
        if form.is_valid():
            houseType = form.save(commit=False)
            houseType.save()
            return redirect('houseType_detail', pk=houseType.pk)
    else:
        form = HouseTypeForm()
    return render(request, 'houseTypes/houseType_edit.html', {'form': form})

def houseType_edit(request, pk):
    houseType = get_object_or_404(houseType, pk=pk)
    if request.method == "POST":
        form = HouseTypeForm(request.POST, instance=houseType)
        if form.is_valid():
            houseType = form.save(commit=False)
            houseType.save()
            return redirect('houseType_detail', pk=houseType.pk)
    else:
        form = HouseTypeForm(instance=houseType)
    return render(request, 'houseTypes/houseType_edit.html', {'form': form})

def houseType_delete(request, pk):
    houseType = get_object_or_404(houseType, pk=pk)
    if request.method == "POST":
        houseType.delete()
        return redirect('houseType_list')
    return render(request, 'houseTypes/houseType_confirm_delete.html', {'houseType': houseType})
