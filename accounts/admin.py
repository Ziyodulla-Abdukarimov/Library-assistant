from django.contrib import admin
from .models import CustomUser
from .models import Return_Book, Accept_Book, Students, Group, Book, SendMessages, Check

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Return_Book)
admin.site.register(Accept_Book)
admin.site.register(Students)
admin.site.register(Group)
admin.site.register(Book)
admin.site.register(SendMessages)
admin.site.register(Check)