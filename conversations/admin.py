# registering the 2 models in admin(convo and msg)-(to django)
from django.contrib import admin
from .models import Conversation, Message


admin.site.register(Conversation)
admin.site.register(Message)

