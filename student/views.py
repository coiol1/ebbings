from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from index.models import *

# Create your views here.
@login_required
def index(request):
    return render(request, 'student/index.html', {})

@login_required
def classes(request):
    student_groups = []
    for usergroup in UserGroup.objects.filter(user = request.user, role = '2'):
        student_groups.append(usergroup.group) #gets the classes (groups) with the user as teacher (role 1)
    return render(request, 'student/classes.html', {'student_groups': student_groups})

@login_required
def study_intro(request, deck_pk):
    deck = Deck.objects.get(pk = deck_pk)
    all_cards = Card.objects.filter(deck = deck)
    first_card = all_cards[0]
    if not StudentCard.objects.filter(user = request.user, card = first_card, deck = deck): #if the user doesn't already have the first studentcard (and therefore doesn't have any studentcards)
        for card in all_cards:
            StudentCard.objects.create(user = request.user, card = card, deck = deck) ###extension### change this to a single transaction that then commits manually after all the studentcards are added - django "atomic"???
    num_due_cards = StudentCard.objects.filter(user = request.user, deck = deck, due__lt = datetime.now).count()
    return render(request, 'student/study_intro.html', {'num_due_cards': num_due_cards, 'deck': deck, 'now': datetime.now})

@login_required
def study_start(request, deck_pk):
    deck = Deck.objects.get(pk = deck_pk)
    due_card = StudentCard.objects.filter(user = request.user, deck = deck, due__lt = datetime.now).first()
    print request.GET.get('hidden')
    # if get == 'get_answer':
    #     return render(request, 'student/study_answer.html', 'deck': deck, 'now': datetime.now, 'due_card': due_card})
    return render(request, 'student/study_question.html', {'deck': deck, 'now': datetime.now, 'due_card': due_card})