from django.shortcuts import redirect, render
from django.db.models import Count
from django.utils import timezone
from accounts.models import *

def superadmin(request):
    context = {
        'accept': Accept_Book.objects.all().count(),
        'all': Book.objects.all().count(),
        'sms' : EmplayeeMessages.objects.all(),
        'data': timezone.now(),
        'null': Students.objects.filter(return_book__isnull=True).count(),
        'good': Students.objects.all().count()- Students.objects.filter(return_book__isnull=True).count(),
        'bookers': Students.objects.annotate(num=Count('return_book')).order_by('-num')[:10],
    }
    return render(request, 'admin/admin.html', context)


def all_book(request):
    if request.method == 'POST':
        search = request.POST['search']
        book = Book.objects.filter(book_name__contains=search)
        context = {
        'book': book,
        }
        return render(request, 'admin/all_book.html', context)
    context = {
        'book': Book.objects.all(),
    }
    return render(request, 'admin/all_book.html', context)


def bookers(request):
    stat = Students.objects.annotate(num=Count('return_book')).order_by('-num')
    return render(request, 'admin/bookers.html', {'statistics': stat, 'student': Students.objects.all()})


def about(request):
    return render(request, 'admin/about.html')


def employeesend(request):
    if request.method == 'POST':
        name = request.POST['name']
        title = request.POST['title']
        body = request.POST['body']
        try:
            EmplayeeMessages(name=name, title=title, body=body).save()
        except:
            print('yuborishda xatolik')
    return render(request, 'admin/employeesend.html')


def studentsend(request):
    if request.method == 'POST':
        name = request.POST['name']
        title = request.POST['title']
        body = request.POST['body']
        try:
            SendMessages(name=name, title=title, body=body).save()
        except:
            print('yuborishda xatolik')
    return render(request, 'admin/studentsend.html')


def addemployee(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        adress = request.POST['phone_number']
        try:
            user = CustomUser.objects.create_user(first_name=first_name,
                                            last_name=last_name,
                                            username=username,
                                            password=password,
                                            user_type=2)
            user.staff.address = adress
            user.save()
            return redirect('addemployee')
        except:
            print('xatolik yuz berdi')
    context = {
        'staff': Staffs.objects.all(),
    }
    return render(request, 'admin/addemployee.html', context)


def delemployee(request):
    context = {
        'staff': Staffs.objects.all(),
    }
    return render(request, 'admin/delemployee.html', context)


def del_e(request, id):
    user = CustomUser.objects.get(staff=id)
    user.delete()
    return redirect('delemployee')


def employee(request):
    context = {
        'employee': Staffs.objects.all(),
    }
    return render(request, 'admin/employee.html', context)


def talaba_tanla_admin(request):
    if request.method == 'POST':
        group = request.POST['group']
        member = Students.objects.filter(groups=group)
        context = {
            'member': member,
            'g':Group.objects.get(id=group).number,
            'group': Group.objects.all(),
        }
        return render(request, 'admin/talaba_select.html', context)
    return render(request, 'admin/talaba_select.html', {'group': Group.objects.all()})


def talaba_admin(request, id):
    student = Students.objects.get(id=id)
    context = {
        'student': student,
        'acceptbook': Accept_Book.objects.filter(student=id),
        'return_book': Return_Book.objects.filter(student=id),
    }
    return render(request, 'admin/talaba.html', context)
