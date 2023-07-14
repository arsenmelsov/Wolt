from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import BranchAddress
from .forms import BranchAddressForm

def branchAddress_list(request):
    branchAddresses = BranchAddress.objects.all()
    return render(request, 'branchAddresses/branchAddress_list.html', {'branchAddresses': branchAddresses})

def branchAddress_detail(request, pk):
    branchAddress = get_object_or_404(branchAddress, pk=pk)
    return render(request, 'branchAddress/branchAddress_detail.html', {'branchAddress': branchAddress})

def branchAddress_new(request):
    if request.method == "POST":
        form = BranchAddressForm(request.POST)
        if form.is_valid():
            branchAddress = form.save(commit=False)
            branchAddress.save()
            return redirect('branchAddress_detail', pk=branchAddress.pk)
    else:
        form = BranchAddressForm()
    return render(request, 'branchAddresses/branchAddress_edit.html', {'form': form})

def branchAddress_edit(request, pk):
    branchAddress = get_object_or_404(branchAddress, pk=pk)
    if request.method == "POST":
        form = BranchAddressForm(request.POST, instance=branchAddress)
        if form.is_valid():
            branchAddress = form.save(commit=False)
            branchAddress.save()
            return redirect('branchAddress_detail', pk=branchAddress.pk)
    else:
        form = BranchAddressForm(instance=branchAddress)
    return render(request, 'branchAddresses/branchAddress_edit.html', {'form': form})

def branchAddress_delete(request, pk):
    branchAddress = get_object_or_404(branchAddress, pk=pk)
    if request.method == "POST":
        branchAddress.delete()
        return redirect('branchAddress_list')
    return render(request, 'branchAddresses/branchAddress_confirm_delete.html', {'branchAddress': branchAddress})