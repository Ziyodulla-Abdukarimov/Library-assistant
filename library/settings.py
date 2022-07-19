import base64
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from accounts.models import CustomUser, Students, Book, Group
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def add_group(request):
    if request.method == 'POST':
        group = request.POST['group']
        if Group.objects.filter(number=group):
            messages.success(request, 'Bu raqamdagi guruh bor')
        else:
            Group(number=group).save()
            return redirect('add_group')
    context = {
        'group_name': Group.objects.all(),
    }
    return render(request, 'staff/settings/add_group.html', context)


@login_required(login_url='login')
def del_group(request):
    context = {
        'groups': Group.objects.all(),
    }
    return render(request, 'staff/settings/del_group.html', context)


@login_required(login_url='login')
def del_g(request, id):
    try:
        object = get_object_or_404(Group, id=id)
        object.delete()
    except:
        print(request, 'Bu raqamli guruh id topilmadi')
    return redirect('del_group')

@login_required(login_url='login')
def add_student(request):
    if request.method == 'POST':
        group = request.POST['group']
        username = request.POST['username']
        password = request.POST['password']
        fio = request.POST['FIO']
        password_id = request.POST['password_ID']
        phone_number = request.POST['phone_number']
        id = Group.objects.get(id=group)
        try:
            user = CustomUser.objects.create_user(username=username,
                                              password=password,
                                              user_type=3)
            user.student.phone_number=phone_number
            user.student.passport_id=password_id
            user.student.FIO=fio
            user.student.groups=id
            user.save()
            return redirect('add_student')
        except:
            print('Username Band')
    context = {
        'group_id': Group.objects.all(),
        'student': CustomUser.objects.filter(user_type=3),
    }
    return render(request, 'staff/settings/add_students.html', context)


@login_required(login_url='login')
def del_student(request):
    if request.method == 'POST':
        group = request.POST['group']
        context = {
            'group': Group.objects.all(),
            'student': Students.objects.filter(groups=group),
        }
        return render(request, 'staff/settings/del_students.html', context)
    context = {
        'group': Group.objects.all(),
        'student': Students.objects.all(),
        }
    return render(request, 'staff/settings/del_students.html', context)

@login_required(login_url='login')
def del_s(request, id):
    user = CustomUser.objects.get(student=id)
    user.delete()
    return redirect('del_student')
# Qr code Start

import cv2
import qrcode
import os
def func(i):
    name='https://ubtuit-library.uz/qr/'+str(i)
    img = qrcode.make(name)
    name='qrs/'+str(i)+'.png'
    try:
        os.mkdir('qrs')
    except:pass
    img.save(name)
    im = cv2.imread(name, 1)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(im, str('id: '+str(i)), (130,360), font, 0.8, (6, 6, 6), 2, cv2.LINE_AA)
    cv2.imwrite(name, im)
    return name

# QR code end


@login_required(login_url='login')
def add_book(request):
    if request.method == 'POST':
        book_name = request.POST['book_name']
        author = request.POST['author']
        key = request.POST['key']
        book_type = request.POST['book_type']
        lang = request.POST['lang']
        if Book.objects.filter(key=key).exists():
            messages.success(request, 'Bu kitob bazada bor')
        else:
            Book(book_name=book_name, author=author,
                key=key,
                book_type=book_type,
                language=lang).save()
            name = func(key)
            with open(name, "rb") as image_file:
                image_data = base64.b64encode(image_file.read()).decode('utf-8')

            context = {
                'image': image_data, 
            }

            return render(request, 'staff/settings/add_book.html', context)
    context = {
        'book': Book.objects.all(),
    }
    return render(request, 'staff/settings/add_book.html', context)


@login_required(login_url='login')
def del_book(request):
    if request.method == 'POST':
        search = request.POST['search']
        book = Book.objects.filter(book_name__contains=search)
        context = {
            'object': book,
        }
        return render(request, 'staff/settings/search_result.html', context)

    context = {
        'book': Book.objects.all(),
    }
    return render(request, 'staff/settings/del_book.html', context)

@login_required(login_url='login')
def del_book_id(request, id):
    obj = get_object_or_404(Book, id=id)
    obj.delete()
    return redirect('del_book')