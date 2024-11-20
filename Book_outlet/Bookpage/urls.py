from django.urls import path
from. import views

urlpatterns=[
    path("", views.index),
    path("<slug:slug>/",views.Book_detail, name="book-detail")
]