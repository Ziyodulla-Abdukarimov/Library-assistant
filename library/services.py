from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.utils import timezone
import datetime
from accounts.models import *
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def book_in(request):
    if request.method == 'POST':
        group = request.POST['group']
        member = Students.objects.filter(groups=group)
        context = {
            'member': member,
            'g':Group.objects.get(id=group).number,
            'group': Group.objects.all(),
        }
        return render(request, 'staff/services/add_group.html', context)
    return render(request, 'staff/services/add_group.html', {'group': Group.objects.all()})


@login_required(login_url='login')
def bookIn(request, id):
    student = Students.objects.get(id=id)
    if request.method == 'POST':
        book_key = request.POST['book_name']
        respite = request.POST['respite']
        id = Students.objects.get(id=id)
        staff_id = request.user.id
        if Book.objects.filter(key=book_key).exists():
            if Accept_Book.objects.filter(book_name=Book.objects.get(key=book_key).book_name).exists():
                messages.success(request, 'Bu kitob berilgan!')
            else:
                Accept_Book(
                    student=id,
                    staff = Staffs.objects.get(admin=staff_id).admin.username,
                    book_name=Book.objects.get(key=book_key).book_name,
                    author=Book.objects.get(key=book_key).author,
                    key=Book.objects.get(key=book_key).key,
                    respite=timezone.now() + datetime.timedelta(days=int(respite))
                    ).save()
                obj = get_object_or_404(Book, id=Book.objects.get(key=book_key).id)
                obj.delete()
                messages.success(request, 'Kitob berildi')
        else:
            messages.success(request, "Bu Raqamli kitob bazada yo'q?")

    context = {
        'student': student,
        'acceptbook': Accept_Book.objects.filter(student=id),
    }
    return render(request, 'staff/services/user.html', context)


@login_required(login_url='login')
def return_book(request):
    if request.method == 'POST':
        group = request.POST['group']
        member = Students.objects.filter(groups=group)
        context = {
            'member': member,
            'g':Group.objects.get(id=group).number,
            'group': Group.objects.all(),
        }
        return render(request, 'staff/services/return_book.html', context)
    return render(request, 'staff/services/return_book.html', {'group': Group.objects.all()})


@login_required(login_url='login')
def return_user(request, id):
    if request.method == 'POST':
        if Accept_Book.objects.filter(id=request.POST['idi']).exists():
                Return_Book(
                    student=Students.objects.get(id=id),
                    staff = Staffs.objects.get(admin=request.user.id).admin.username,
                    book_name=Accept_Book.objects.get(id=request.POST['idi']).book_name,
                    author=Accept_Book.objects.get(id=request.POST['idi']).author,
                    date=Accept_Book.objects.get(id=request.POST['idi']).created,
                    respite=Accept_Book.objects.get(id=request.POST['idi']).respite,
                    key=Accept_Book.objects.get(id=request.POST['idi']).key,
                    ).save()
                Book(
                    book_name=Accept_Book.objects.get(id=request.POST['idi']).book_name,
                    author=Accept_Book.objects.get(id=request.POST['idi']).author,
                    key=Accept_Book.objects.get(id=request.POST['idi']).key,
                    ).save()
                obj = get_object_or_404(Accept_Book, id=request.POST['idi'])
                obj.delete()
                redirect('staff/services/return_user.html')
        else:
            messages.success(request, 'not response')
    context = {
        'student': Students.objects.get(id=id),
        'accept_book': Accept_Book.objects.filter(student=id),
        'returnBook': Return_Book.objects.filter(student=id),
    }
    return render(request, 'staff/services/return_user.html', context)


@login_required(login_url='login')
def notime(request):
    date = timezone.now()

    context = {
        'accept': Accept_Book.objects.filter(respite__lte=date)
    }
    return render(request, 'staff/services/notime.html', context)


@login_required(login_url='login')
def checkbook(request):
    context = {
        'check': Check.objects.all(),
    }
    return render(request, 'staff/services/check.html', context)


@login_required(login_url='login')
def checkdate(request, id):
    if request.method == 'POST':
        respite_date = request.POST['date']
        Accept_Book(
            student= Check.objects.get(id=id).student,
            staff= Staffs.objects.get(admin=request.user.id).admin.username,
            book_name=Check.objects.get(id=id).book_name,
            author=Check.objects.get(id=id).author,
            key=Check.objects.get(id=id).key,
            respite=timezone.now() + datetime.timedelta(days=int(respite_date)),
        ).save()
        obj = get_object_or_404(Book, id=Book.objects.get(key=Check.objects.get(id=id).key).id)
        obj.delete()
        obj = get_object_or_404(Check, id=id)
        obj.delete()
        return redirect('check')
    return render(request, 'staff/services/checkdate.html')


@login_required(login_url='login')
def delcheck(request,id):
    obj = get_object_or_404(Check, id=id)
    obj.delete()
    return redirect('check')


@login_required(login_url='login')
def allreading(request):
    context = {
        'reading': Accept_Book.objects.all(),
    }
    return render(request, 'staff/services/allreading.html', context)