from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Animal)
admin.site.register(Lot)
admin.site.register(Bet)