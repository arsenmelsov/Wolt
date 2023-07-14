from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Card
from .forms import CardForm

def card_list(request):
    cards = Card.objects.all()
    return render(request, 'cards/card_list.html', {'cards': cards})

def card_detail(request, pk):
    card = get_object_or_404(card, pk=pk)
    return render(request, 'cards/card_detail.html', {'card': card})

def card_new(request):
    if request.method == "POST":
        form = CardForm(request.POST)
        if form.is_valid():
            card = form.save(commit=False)
            card.save()
            return redirect('card_detail', pk=card.pk)
    else:
        form = CardForm()
    return render(request, 'cards/card_edit.html', {'form': form})

def card_edit(request, pk):
    card = get_object_or_404(card, pk=pk)
    if request.method == "POST":
        form = CardForm(request.POST, instance=card)
        if form.is_valid():
            card = form.save(commit=False)
            card.save()
            return redirect('card_detail', pk=card.pk)
    else:
        form = CardForm(instance=card)
    return render(request, 'cards/card_edit.html', {'form': form})

def card_delete(request, pk):
    card = get_object_or_404(card, pk=pk)
    if request.method == "POST":
        card.delete()
        return redirect('card_list')
    return render(request, 'cards/card_confirm_delete.html', {'card': card})
