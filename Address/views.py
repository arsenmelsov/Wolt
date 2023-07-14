from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Address
from .forms import AddressForm

def address_list(request):
    addresss = Address.objects.all()
    return render(request, 'addresss/address_list.html', {'addresss': addresss})

def address_detail(request, pk):
    address = get_object_or_404(address, pk=pk)
    return render(request, 'addresses/address_detail.html', {'address': address})

def address_new(request):
    if request.method == "POST":
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.save()
            return redirect('address_detail', pk=address.pk)
    else:
        form = AddressForm()
    return render(request, 'addresses/address_edit.html', {'form': form})

def address_edit(request, pk):
    address = get_object_or_404(address, pk=pk)
    if request.method == "POST":
        form = AddressForm(request.POST, instance=address)
        if form.is_valid():
            address = form.save(commit=False)
            address.save()
            return redirect('address_detail', pk=address.pk)
    else:
        form = AddressForm(instance=address)
    return render(request, 'addresses/address_edit.html', {'form': form})

def address_delete(request, pk):
    address = get_object_or_404(address, pk=pk)
    if request.method == "POST":
        address.delete()
        return redirect('address_list')
    return render(request, 'addresses/address_confirm_delete.html', {'address': address})
