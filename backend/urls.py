from django.contrib import admin
from django.urls import path
from api.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ApiOverview.as_view()),
    path('signup', Signup.as_view()),
    path('login', Login.as_view()),
    path('tasklist', All_Task.as_view()),
    path('create', Create_task.as_view()),
    path('logout', Logout.as_view()),
    path('update/<str:pk>', Update_task.as_view()),
    path('delete/<str:pk>', Delete_task.as_view()),
]
