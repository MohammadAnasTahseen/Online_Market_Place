
from django.urls import path,include
from . import views

app_name='communicate'
urlpatterns = [
    path('',views.inbox,name='inbox'),
    path('new/<int:item_pk>/',views.new_conversation,name='new'),


] 