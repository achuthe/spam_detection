from django.urls import path
from .views import UserCreateView, ContactListCreateView, ContactDetailView

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='register'),
    path('contacts/', ContactListCreateView.as_view(), name='contact-list'),
    path('contacts/<int:pk>/', ContactDetailView.as_view(), name='contact-detail'),
]
