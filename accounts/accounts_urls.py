from django.urls import path, include
from .views import login, log_out
from library import library_urls, students_urls, admin_url
from library.upload_views import student_upload, book_upload
from QRCODE import qr_urls

urlpatterns = [
    path('', login, name='login'),
    path('logout', log_out, name='logout'),
    path('staff/', include(library_urls), name='staff'),
    path('student/', include(students_urls)),
    path('super_admin/', include(admin_url), name='superadmin'),
    path('qr/', include(qr_urls)),
    path('upload_student', student_upload),
    path('upload_book', book_upload),
]
