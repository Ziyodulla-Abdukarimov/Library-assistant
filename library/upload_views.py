from django.shortcuts import render
from .upload_excel import BookResources, StudentResources
from accounts.models import Book, CustomUser, Group
from tablib import Dataset


def student_upload(request):
    if request.method == 'POST':
        group = request.POST['group']
        book_resourse = StudentResources()
        dataset = Dataset()
        new_book = request.FILES['file']
        group_id = Group.objects.get(id=group)

        if not new_book.name.endswith('xlsx'):
            return render(request, 'staff/file_upload/upload.html')
        imported_data = dataset.load(new_book.read(), format='xlsx')
        for data in imported_data:
            user = CustomUser.objects.create_user(
                    username=data[1],
                    password=data[5],
                    user_type = 3
                )
            user.student.FIO=data[6]
            user.student.passport_id=data[5]
            user.student.JSHSHIR=data[4]
            user.student.fuqarolik=data[2]
            user.student.country=data[13]
            user.student.region=data[14]
            user.student.tuman=data[15]
            user.student.gender=data[3]
            user.student.brithday=data[7]
            user.student.faculty=data[11]
            user.student.groups=group_id
            user.student.typeofEducation=data[9]
            user.student.formofEducation=data[11]
            user.student.phone_number=data[8]
            user.save()
    context = {
        'group': Group.objects.all(),
    }
    return render(request, 'staff/file_upload/upload.html', context)


def book_upload(request):
    if request.method == 'POST':
        book_resourse = BookResources()
        dataset = Dataset()
        new_book = request.FILES['file']

        if not new_book.name.endswith('xlsx'):
            return render(request, 'staff/file_upload/book_upload.html')
        imported_data = dataset.load(new_book.read(), format='xlsx')
        for data in imported_data:
            value = Book(
                book_name=data[1],
                author=data[2],
                organization=data[3],
                publishing=data[4],
                book_type=data[5],
                language=data[6],
                year=data[7],
                beti=data[8],
                isbn=data[9],
                money=data[10],
                key=data[13], 
            )
            value.save()
    return render(request, 'staff/file_upload/book_upload.html')