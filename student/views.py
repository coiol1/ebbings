from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib.auth.decorators import login_required, user_passes_test
from index.models import *
import random

NON_STUDENT_LOGIN = settings.LOGIN_URL + '?student=false'

def is_student(user):
    try:
        if UserProfile.objects.get(user = user).student_id:
            return True
        else:
            return False
    except:
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
@user_passes_test(is_student, login_url = NON_STUDENT_LOGIN, redirect_field_name = None)
def index(request):
    return render(request, 'student/index.html', {})

@login_required
@user_passes_test(is_student, login_url = NON_STUDENT_LOGIN, redirect_field_name = None)
def learnmore(request):
    return render(request, 'student/learnmore.html', {})

@login_required
@user_passes_test(is_student, login_url = NON_STUDENT_LOGIN, redirect_field_name = None)
def classes(request):
    student_groups = []
    for usergroup in UserGroup.objects.filter(user = request.user, role = '2'):
        student_groups.append(usergroup.group) #gets the classes (groups) with the user as student (role 2)
    return render(request, 'student/classes.html', {'student_groups': student_groups})

@login_required
@user_passes_test(is_student, login_url = NON_STUDENT_LOGIN, redirect_field_name = None)
def classes_teachers(request):
    teachers = sorted(UserProfile.objects.exclude(teacher_id = ''), key = lambda x: x.user.last_name)
    return render(request, 'student/classes_teachers.html', {'teachers': teachers})

@login_required
@user_passes_test(is_student, login_url = NON_STUDENT_LOGIN, redirect_field_name = None)
def classes_teachers_list(request, teacher_pk):
    teacher_user = User.objects.get(pk = teacher_pk)
    teacher_userprofile = UserProfile.objects.get(user = teacher_user)
    teacher_groups = []
    for usergroup in UserGroup.objects.filter(user = teacher_user, role = '1'):
        teacher_groups.append(usergroup.group)
    return render(request, 'student/classes_teachers_list.html', {'teacher_user': teacher_user, 'teacher_userprofile': teacher_userprofile, 'teacher_groups': teacher_groups})

@login_required
@user_passes_test(is_student, login_url = NON_STUDENT_LOGIN, redirect_field_name = None)
def classes_join(request, group_pk):
    group = Group.objects.get(pk = group_pk)
    teacher = UserGroup.objects.get(group_id = group_pk, role = '1').user
    try:
        UserGroup.objects.get(user = request.user, group = group, role = '2')
        return render(request, 'student/classes_join.html', {'group': group, 'teacher': teacher, 'already_joined': True})
    except:
        return render(request, 'student/classes_join.html', {'group': group, 'teacher': teacher, 'already_joined': False})

@login_required
@user_passes_test(is_student, login_url = NON_STUDENT_LOGIN, redirect_field_name = None)
def classes_join_success(request, group_pk):
    if request.method == 'POST':
        group = Group.objects.get(pk = group_pk)
        UserGroup.objects.create(user = request.user, group = group, role = '2')
        return render(request, 'student/classes_join_success.html', {'group': group})
    else:
        return redirect(reverse('student:classes_join', args = (group_pk)))

@login_required
@user_passes_test(is_student, login_url = NON_STUDENT_LOGIN, redirect_field_name = None)
def study_intro(request, group_pk, deck_pk):
    group = Group.objects.get(pk = group_pk)
    deck = Deck.objects.get(pk = deck_pk)
    groupdeck = GroupDeck.objects.filter(group = group, deck = deck, deadline__gt = datetime.now)
    if groupdeck:
        deadline_passed = False
    else:
        deadline_passed = True
    all_cards = Card.objects.filter(deck = deck)
    first_card = all_cards[0]
    if not StudentCard.objects.filter(user = request.user, card = first_card, deck = deck): #if the user doesn't already have the first studentcard (and therefore doesn't have any studentcards)
        for card in all_cards:
            StudentCard.objects.create(user = request.user, card = card, deck = deck) ###extension### change this to a single transaction that then commits manually after all the studentcards are added - django "atomic"???
    num_due_cards = StudentCard.objects.filter(user = request.user, deck = deck, due__lt = datetime.now).count()
    num_acquired_cards = StudentCard.objects.filter(user = request.user, deck = deck, learning_state = '3').count()
    num_total_cards = StudentCard.objects.filter(user = request.user, deck = deck).count()
    percent_acquired = "%.1f" % (num_acquired_cards / float(num_total_cards) * 100)
    return render(request, 'student/study_intro.html', {'num_due_cards': num_due_cards, 'num_acquired_cards': num_acquired_cards, 'num_total_cards': num_total_cards, 'percent_acquired': percent_acquired, 'deck': deck, 'group': group, 'now': datetime.now, 'deadline_passed': deadline_passed})

@login_required
@user_passes_test(is_student, login_url = NON_STUDENT_LOGIN, redirect_field_name = None)
def study_start(request, group_pk, deck_pk):
    group = Group.objects.get(pk = group_pk)
    deck = Deck.objects.get(pk = deck_pk)
    deadline_passed = GroupDeck.objects.filter(group = group, deck = deck, deadline__lt = datetime.now)
    if deadline_passed:
        return redirect(reverse('student:study_intro', args = (group.pk, deck.pk)))
    card_pk = request.POST.get('card_pk')
    show_answer = request.POST.get('show_answer')
    if show_answer == 'y':
        due_card = StudentCard.objects.get(pk = card_pk)
        return render(request, 'student/study_answer.html', {'deck': deck, 'group': group, 'now': datetime.now, 'due_card': due_card})
    answered = request.POST.get('answered')
    if answered:
        answer_card(StudentCard.objects.get(pk = card_pk), int(answered))
    try:
        due_card = random.choice(StudentCard.objects.filter(user = request.user, deck = deck, due__lt = datetime.now))
    except:
        due_card = None
    return render(request, 'student/study_question.html', {'deck': deck, 'group': group, 'now': datetime.now, 'due_card': due_card})