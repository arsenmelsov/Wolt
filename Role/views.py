from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Role
from .forms import RoleForm

def role_list(request):
    roles = Role.objects.all()
    return render(request, 'roles/role_list.html', {'roles': roles})

def role_detail(request, pk):
    role = get_object_or_404(role, pk=pk)
    return render(request, 'roles/role_detail.html', {'role': role})

def role_new(request):
    if request.method == "POST":
        form = RoleForm(request.POST)
        if form.is_valid():
            role = form.save(commit=False)
            role.save()
            return redirect('role_detail', pk=role.pk)
    else:
        form = RoleForm()
    return render(request, 'roles/role_edit.html', {'form': form})

def role_edit(request, pk):
    role = get_object_or_404(role, pk=pk)
    if request.method == "POST":
        form = RoleForm(request.POST, instance=role)
        if form.is_valid():
            role = form.save(commit=False)
            role.save()
            return redirect('role_detail', pk=role.pk)
    else:
        form = RoleForm(instance=role)
    return render(request, 'roles/role_edit.html', {'form': form})

def role_delete(request, pk):
    role = get_object_or_404(role, pk=pk)
    if request.method == "POST":
        role.delete()
        return redirect('role_list')
    return render(request, 'roles/role_confirm_delete.html', {'role': role})
