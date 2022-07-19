from django.shortcuts import render
from accounts.models import Accept_Book, Students, Return_Book, Book, SendMessages
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def students(request):
    return render(request, 'student/student.html')


@login_required(login_url='login')
def student_profile(request):
    student = Students.objects.get(admin=request.user.id)
    context = {
        'student':student,
    }
    return render(request, 'student/profile.html', context)


@login_required(login_url='login')
def read_book(request):
    id = Students.objects.get(admin=request.user.id).id
    print(id)
    accept_book = Return_Book.objects.filter(student=id)
    context = {
        'accept_book':accept_book,
    }
    return render(request, 'student/read_book.html', context)


@login_required(login_url='login')
def all_book(request):
    if request.method == 'POST':
        search = request.POST['search']
        book = Book.objects.filter(book_name__contains=search)
        context = {
        'book': book,
        }
        return render(request, 'student/all_book.html', context)
    context = {
        'book': Book.objects.all(),
    }
    return render(request, 'student/all_book.html', context)


@login_required(login_url='login')
def contact(request):
    return render(request, 'student/contact.html')


@login_required(login_url='login')
def news(request):
    context = {
        'news': SendMessages.objects.all(),
    }
    return render(request, 'student/news.html', context)


@login_required(login_url='login')
def reading_book(request):
    id = Students.objects.get(admin=request.user.id).id
    print(id)
    accept_book = Accept_Book.objects.filter(student=id)
    context = {
        'accept_book':accept_book,
    }
    return render(request, 'student/reading_book.html', context)