from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from index.models import *
import random

def is_student(user):
    if UserProfile.objects.get(user = user).student_id:
        return True
    return False

def answer_card(card, selection):
    if selection == '1':
        card.interval = random.randint(8, 12)
        if card.learning_state == '3':
            card.learning_state = '2'
    else:
        card.interval = card.interval * card.ease_factor * random.uniform(0.95, 1.05)
        if card.interval < 1440:
            card.interval = 1440 * random.uniform(0.95, 1.05)
    card.due = datetime.now() + timedelta(minutes = card.interval)
    card.ease_factor = card.ease_factor + (0.1 - (5 - selection) * (0.08 + (5 - selection) * 0.02))
    if card.ease_factor < 1.3:
        card.ease_factor = 1.3
    if card.interval > 43829.1:
        card.learning_state = '3'
    card.save()

# Create your views here.
@login_required
@user_passes_test(is_student, login_url = '/users/login/?student=false',redirect_field_name = None)
def index(request):
    return render(request, 'student/index.html', {})

@login_required
@user_passes_test(is_student, login_url = '/users/login/?student=false',redirect_field_name = None)
def classes(request):
    student_groups = []
    for usergroup in UserGroup.objects.filter(user = request.user, role = '2'):
        student_groups.append(usergroup.group) #gets the classes (groups) with the user as teacher (role 1)
    return render(request, 'student/classes.html', {'student_groups': student_groups})

@login_required
@user_passes_test(is_student, login_url = '/users/login/?student=false',redirect_field_name = None)
def study_intro(request, deck_pk):
    deck = Deck.objects.get(pk = deck_pk)
    all_cards = Card.objects.filter(deck = deck)
    first_card = all_cards[0]
    if not StudentCard.objects.filter(user = request.user, card = first_card, deck = deck): #if the user doesn't already have the first studentcard (and therefore doesn't have any studentcards)
        for card in all_cards:
            StudentCard.objects.create(user = request.user, card = card, deck = deck) ###extension### change this to a single transaction that then commits manually after all the studentcards are added - django "atomic"???
    num_due_cards = StudentCard.objects.filter(user = request.user, deck = deck, due__lt = datetime.now).count()
    num_acquired_cards = StudentCard.objects.filter(user = request.user, deck = deck, learning_state = '3').count()
    num_total_cards = StudentCard.objects.filter(user = request.user, deck = deck).count()
    percent_acquired = "%.1f" % (num_acquired_cards / float(num_total_cards))
    return render(request, 'student/study_intro.html', {'num_due_cards': num_due_cards, 'num_acquired_cards': num_acquired_cards, 'num_total_cards': num_total_cards, 'percent_acquired': percent_acquired, 'deck': deck, 'now': datetime.now})

@login_required
@user_passes_test(is_student, login_url = '/users/login/?student=false',redirect_field_name = None)
def study_start(request, deck_pk):
    deck = Deck.objects.get(pk = deck_pk)
    card_pk = request.POST.get('card_pk')
    show_answer = request.POST.get('show_answer')
    if show_answer == 'y':
        due_card = StudentCard.objects.get(pk = card_pk)
        return render(request, 'student/study_answer.html', {'deck': deck, 'now': datetime.now, 'due_card': due_card})
    answered = request.POST.get('answered')
    if answered:
        answer_card(StudentCard.objects.get(pk = card_pk), int(answered))
    due_card = StudentCard.objects.filter(user = request.user, deck = deck, due__lt = datetime.now).first()
    return render(request, 'student/study_question.html', {'deck': deck, 'now': datetime.now, 'due_card': due_card})