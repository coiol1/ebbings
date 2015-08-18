from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Deck)
admin.site.register(Group)
admin.site.register(UserGroup)
admin.site.register(GroupDeck)
admin.site.register(Card)
admin.site.register(StudentCard)