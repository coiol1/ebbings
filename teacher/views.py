from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from index.models import Card, Deck

# Create your views here.
@login_required
def index(request):
    return render(request, 'teacher/index.html', {})

@login_required
def decks(request):
    return render(request, 'teacher/decks.html', {})

@login_required
def decks_review(request, deck_pk):
    cards = Card.objects.filter(deck = Deck.objects.get(pk = deck_pk))
    return render(request, 'teacher/decks_review.html', {'cards': cards})

@login_required
def classes(request):
    return render(request, 'teacher/classes.html', {})

@login_required
def classes_new(request):
    decks = Deck.objects.all()
    return render(request, 'teacher/classes_new.html', {'decks': decks})

@login_required
def classes_new_create(request):
    print request.POST
    return render(request, 'teacher/classes_new_create.html', {})