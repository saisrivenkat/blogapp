
from django.urls import path
from .views import postview , detailview , createview
from . import views


urlpatterns = [
    path('',postview.as_view(), name='blog-home'),
    path('post/<int:pk>/',detailview.as_view(), name='post-detail'),
    path('create/',createview.as_view(), name='post-create'),
    path('about/',views.about),
]


