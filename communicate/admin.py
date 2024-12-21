from django.contrib import admin
from .models import ConversationU,ConversationMessage
# Register your models here.

admin.site.register(ConversationU)
admin.site.register(ConversationMessage)