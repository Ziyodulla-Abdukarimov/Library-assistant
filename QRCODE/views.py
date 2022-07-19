from django.utils import timezone
import datetime
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from accounts.models import Group, Return_Book, Staffs, Students, Book, Accept_Book, Check
from library.staff import staff
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
# Create your views here.
def main(request, id):
    if request.user.user_type == "3":
        if request.method == 'POST':
            Check(
                student=Students.objects.get(admin=request.user.id),
                book_name=Book.objects.get(key=id).book_name,
                author=Book.objects.get(key=id).author,
                date=timezone.now(),
                key=Book.objects.get(key=id).key,
            ).save()
            return render(request, 'student/profile.html')
        return render(request, 'student/qr.html')
    else:
        context = {
            'id': id,
        }
        return render(request, 'qrcode/main.html', context)


@login_required(login_url='login')
def qrCode(request, id):
    if request.method == 'POST':
        group = request.POST['group']
        member = Students.objects.filter(groups=group)
        context = {
            'member': member,
            'group': Group.objects.all(),
            'id': id,
        }
        return render(request, 'qrcode/qrcode.html', context)
    context = {
        'group': Group.objects.all(),
        'id': id,
    }
    return render(request, 'qrcode/qrcode.html', context)


@login_required(login_url='login')
def addUser(request, id, pk):
    if request.method == 'POST':
        respite = request.POST['respite']
        if Book.objects.filter(key=id).exists():
            if Accept_Book.objects.filter(key=id).exists():
                messages.success(request, 'Bu kitob olingan')
            else:
                Accept_Book(student=Students.objects.get(id=pk),
                            staff = Staffs.objects.get(admin=request.user.id).admin.username,
                            book_name=Book.objects.get(key=id).book_name,
                            author=Book.objects.get(key=id).author,
                            key=Book.objects.get(key=id).key,
                            respite=timezone.now() + datetime.timedelta(days=int(respite))
                            ).save()
                obj = get_object_or_404(Book, id=Book.objects.get(key=id).id)
                obj.delete()
                messages.success(request, "Kitob Qo'shildi")
        else:
            messages.success(request, "Bu Raqamli kitob bazada yo'q?")
        return render(request, 'qrcode/accept.html')
    return render(request, 'qrcode/respite.html')


@login_required(login_url='login')
def remove(request, id):

    if Accept_Book.objects.filter(key = id).exists():
            a = Accept_Book.objects.get(key=id).student
            Return_Book(student=Students.objects.get(id=a.id),
                staff = Staffs.objects.get(admin=request.user.id).admin.username,
                book_name=Accept_Book.objects.get(key=id).book_name,
                author=Accept_Book.objects.get(key=id).author,
                respite=Accept_Book.objects.get(key=id).respite,
                date=timezone.now(),
                key=Accept_Book.objects.get(key=id).key,
                ).save()
            Book(
                book_name=Accept_Book.objects.get(key=id).book_name,
                author=Accept_Book.objects.get(key=id).author,
                key=Accept_Book.objects.get(key=id).key,
                ).save()
            obj = get_object_or_404(Accept_Book, key=id)
            obj.delete()
            redirect('staff/services/return_user.html')
    else:
        messages.success(request, 'not response')
    return render(request, 'qrcode/remove.html')
