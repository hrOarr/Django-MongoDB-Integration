from django.conf.urls import url 
from django.urls import path
from tutorials import views 
 
urlpatterns = [ 
    path('',views.home, name="home"),
    path('tutorials/', views.tutorial_list, name="tutorials"),
    path('tutorials/<slug:slug>', views.tutorial_detail, name="tutorial_detail"),
]