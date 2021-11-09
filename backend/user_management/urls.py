from django.urls import path

from . import views

urlpatterns = [
    path('signup/viewer', views.SignUPViewer.as_view(), name='signup_viewer'),
    path('signup/contentcreator', views.SignUPContentCreator.as_view(), name='signup_cc'),
]