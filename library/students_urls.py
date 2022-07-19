from django.urls import path
from library.students import *

urlpatterns = [
    path('', student_profile, name='student_profile'),
    path('read_book', read_book, name='read_book'),
    path('all_book', all_book, name='all_book'),
    path('contact', contact, name='contacta'),
    path('news', news, name='news'),
    path('reading_book', reading_book, name='reading_book'),
]