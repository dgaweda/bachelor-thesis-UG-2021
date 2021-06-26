"""form_to_python URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', csrf_exempt(views.main), name = "Main"),
    path('Start/', csrf_exempt(views.botSettings)),
    path('Exit/', views.exit, name = "Exit"),
    path('Comments/', views.comments, name = "Comments"),
    path('CommentsAdd/', views.add_comment_record, name = "Comments_Setting"),
    path('AddSingleComment/', views.add_single_comment, name = "Single_Comment"),
    path('ClearComments/', views.clear_comments, name = "Clear"),
    path('Delete/<slug:_id>/', views.delete_record, name = "Delete")
]
