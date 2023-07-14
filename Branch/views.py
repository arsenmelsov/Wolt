from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Branch
from .forms import BranchForm

def branch_list(request):
    branches = Branch.objects.all()
    return render(request, 'branches/branch_list.html', {'branches': branches})

def branch_detail(request, pk):
    branch = get_object_or_404(branch, pk=pk)
    return render(request, 'branches/branch_detail.html', {'branch': branch})

def branch_new(request):
    if request.method == "POST":
        form = BranchForm(request.POST)
        if form.is_valid():
            branch = form.save(commit=False)
            branch.save()
            return redirect('branch_detail', pk=branch.pk)
    else:
        form = BranchForm()
    return render(request, 'branches/branch_edit.html', {'form': form})

def branch_edit(request, pk):
    branch = get_object_or_404(branch, pk=pk)
    if request.method == "POST":
        form = BranchForm(request.POST, instance=branch)
        if form.is_valid():
            branch = form.save(commit=False)
            branch.save()
            return redirect('branch_detail', pk=branch.pk)
    else:
        form = BranchForm(instance=branch)
    return render(request, 'branches/branch_edit.html', {'form': form})

def branch_delete(request, pk):
    branch = get_object_or_404(branch, pk=pk)
    if request.method == "POST":
        branch.delete()
        return redirect('branch_list')
    return render(request, 'branches/branch_confirm_delete.html', {'branch': branch})