from django.urls import path
from .views import qrCode, addUser, main, remove

urlpatterns = [
    path('<int:id>', main, name='main'),
    path('<int:id>/add', qrCode, name='qrCode'),
    path('<int:id>/add/<int:pk>', addUser, name='addUser'),
    path('<int:id>/remove', remove, name='remove'),
]
