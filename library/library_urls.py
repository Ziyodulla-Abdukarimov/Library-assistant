from django.urls import path
from library.settings import *
from library.services import *
from library.staff import staff
from library.students import *
from library.menu_view import *
from library.staff import *

urlpatterns = [
### Staff
	path('', staff, name='staff'),
### Settings
	path('add_group', add_group, name='add_group'),
	path('del_group', del_group, name='del_group'),
	path('del_group/<id>', del_g, name='del_g'),
	path('add_student/', add_student, name='add_student'),
	path('del_student', del_student, name='del_student'),
	path('del_student/<id>', del_s, name='del_s'),
	path('add_book', add_book, name='add_book'),
	path('del_book', del_book, name='del_book'),
	path('del_book/<id>', del_book_id, name='del_book_id'),
#### Servise
	path('book_in', book_in, name='book_in'),
	path('book_in/<id>', bookIn, name='bookIn'),
	path('return_book', return_book, name='return_book'),
	path('return_book/<id>', return_user, name='return_user'),
	path('notime', notime, name='notime'),
	path('allreading', allreading, name='allreading'),
	path('check', checkbook, name='check'),
	path('check/<id>', checkdate, name='checkdate'),
	path('check/del/<id>', delcheck, name='delcheck'),
### Menyu
	path('all_books', all_books, name='all_books'),
	path('bookers', bookers, name='bookers'),
	path('contact', contact, name='contact'),
	path('sendM',sendM, name='sendM'),
	path('profile', talaba_tanla, name='profile'),
	path('profile/<id>',talaba, name='talaba'),
]