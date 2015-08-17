from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required, user_passes_test
from index.models import *

NON_TEACHER_LOGIN = settings.LOGIN_URL + '?teacher=false'

def is_teacher(user):
    if UserProfile.objects.get(user = user).teacher_id:
        return True
    return False

# Create your views here.
@login_required
@user_passes_test(is_teacher, login_url = NON_TEACHER_LOGIN,redirect_field_name = None)
def index(request):
    return render(request, 'teacher/index.html', {})

@login_required
@user_passes_test(is_teacher, login_url = NON_TEACHER_LOGIN,redirect_field_name = None)
def decks(request):
    return render(request, 'teacher/decks.html', {})

@login_required
@user_passes_test(is_teacher, login_url = NON_TEACHER_LOGIN,redirect_field_name = None)
def decks_review(request):
    decks = Deck.objects.all()
    return render(request, 'teacher/decks_review.html', {'decks': decks})

@login_required
@user_passes_test(is_teacher, login_url = NON_TEACHER_LOGIN,redirect_field_name = None)
def decks_review_one(request, deck_pk):
    cards = Card.objects.filter(deck = Deck.objects.get(pk = deck_pk))
    deck_name = Deck.objects.get(pk = deck_pk).name
    return render(request, 'teacher/decks_review_one.html', {'cards': cards, 'deck_name': deck_name})

@login_required
@user_passes_test(is_teacher, login_url = NON_TEACHER_LOGIN,redirect_field_name = None)
def classes(request):
    teacher_groups = []
    for usergroup in UserGroup.objects.filter(user = request.user, role = '1'):
        teacher_groups.append(usergroup.group) #gets the classes (groups) with the user as teacher (role 1)
    return render(request, 'teacher/classes.html', {'teacher_groups': teacher_groups})

@login_required
@user_passes_test(is_teacher, login_url = NON_TEACHER_LOGIN,redirect_field_name = None)
def classes_one(request, group_pk):
    group = Group.objects.get(pk = group_pk)
    groupdecks = GroupDeck.objects.filter(group_id = group_pk)
    decks = []
    for groupdeck in groupdecks:
        decks.append(groupdeck.deck)
    students = []
    for usergroup in UserGroup.objects.filter(group_id = group_pk, role = '2'):
        one_student = [usergroup.user]
        one_student.append(UserProfile.objects.get(user = usergroup.user).student_id)
        total_score = 0.0
        for deck in decks:
            num_acquired_cards = StudentCard.objects.filter(user = one_student[0], deck = deck, learning_state = '3').count()
            num_total_cards = StudentCard.objects.filter(user = one_student[0], deck = deck).count()
            try:
                percent_acquired = "%.1f" % (num_acquired_cards / float(num_total_cards) * 100)
            except:
                percent_acquired = "0.0"
            one_student.append(percent_acquired)
            total_score += float(percent_acquired) * GroupDeck.objects.get(group = group, deck = deck).weight / 100
        one_student.append(total_score)
        students.append(one_student) #students is an array of one_students, one_student format: [user object, student # string, deck1 percent acquired string, deck2 percent acquired string, ..., total score float]
    try:
        students.sort(key = lambda x: int(x[1])) #if student_ids are integer only
    except:
        students.sort(key = lambda x: x[1]) #else sort as strings
    return render(request, 'teacher/classes_one.html', {'group': group, 'students': students, 'groupdecks': groupdecks})

@login_required
@user_passes_test(is_teacher, login_url = NON_TEACHER_LOGIN,redirect_field_name = None)
def classes_new(request):
    decks = Deck.objects.all()
    return render(request, 'teacher/classes_new.html', {'decks': decks})

@login_required
@user_passes_test(is_teacher, login_url = NON_TEACHER_LOGIN,redirect_field_name = None)
def classes_new_create(request):
    decks = request.POST.getlist('deck')
    new_class = Group.objects.create(name = request.POST.get('title'))
    UserGroup.objects.create(user = request.user, group = new_class, role = '1')
    for deck in decks:
        deadline_string = 'deadline' + str(deck)
        weight_string = 'weight' + str(deck)
        GroupDeck.objects.create(group = new_class, deck = Deck.objects.get(pk = deck), deadline = request.POST.get(deadline_string).replace("T", " "), weight = request.POST.get(weight_string))
    return render(request, 'teacher/classes_new_create.html', {})