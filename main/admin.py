from django.contrib import admin

# Register your models here.
from main.models import Tweet
from main.models import Following
from main.models import MyUser
from main.models import Messages
admin.site.register(Tweet)
admin.site.register(Following)
admin.site.register(MyUser)
admin.site.register(Messages)
