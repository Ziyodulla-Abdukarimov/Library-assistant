from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomUser(AbstractUser):
    HOD = '1'
    STAFF = '2'
    STUDENT = '3'

    EMAIL_TO_USER_TYPE_MAP = {
        'hod': HOD,
        'staff': STAFF,
        'student': STUDENT
    }

    user_type_data = ((HOD, "HOD"), (STAFF, "Staff"), (STUDENT, "Student"))
    user_type = models.CharField(default=1, choices=user_type_data, max_length=10)

class Group(models.Model):
    number = models.CharField(max_length=10, verbose_name="Gruh nomeri")
    objects = models.Manager()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.number

class AdminHOD(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)


class Staffs(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='staff')
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

class Students(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE,related_name='student')
    id = models.AutoField(primary_key=True)
    FIO = models.CharField(max_length=500, verbose_name='FIO')
    passport_id = models.CharField(max_length=15, verbose_name="Pasport ID")
    JSHSHIR = models.CharField(max_length=50)
    fuqarolik = models.CharField(max_length=300)
    country = models.CharField(max_length=100)
    nationaly = models.CharField(max_length=100, verbose_name='Millat')
    region = models.CharField(max_length=100, verbose_name='viloyat', blank=True, null=True)
    tuman = models.CharField(max_length=100, verbose_name='tuman', blank=True, null=True)
    gender = models.CharField(max_length=50, verbose_name='jins')
    brithday = models.CharField(max_length=100, verbose_name="Tugulgan sana")
    faculty = models.CharField(max_length=300, verbose_name="Fakultet")
    groups = models.ForeignKey(Group, on_delete=models.CASCADE, blank=True, null=True)
    typeofEducation = models.CharField(max_length=100, name="Talim turi")
    formofEducation = models.CharField(max_length=100, verbose_name="Talim shakli")
    phone_number = models.CharField(max_length=20, verbose_name="Telefon raqami")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.FIO

class Accept_Book(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE, related_name='accept_book')
    staff = models.CharField(max_length=100, verbose_name='Bergan odam nomi')
    created = models.DateTimeField(editable=False, auto_now_add=True)
    book_name = models.CharField(max_length=50, verbose_name="Kitob nomi")
    author = models.CharField(max_length=100, verbose_name='Муаллифи')
    key = models.CharField(max_length=25)
    respite = models.DateTimeField(blank=True, null=True)
    date = models.DateField(editable=False, auto_now_add=True)
    objects = models.Manager()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.book_name

class Return_Book(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE, blank=True, null=True)
    staff = models.CharField(max_length=100, verbose_name='Bergan odam nomi')
    created = models.DateTimeField(editable=False, auto_now_add=True)
    book_name = models.CharField(max_length=50, verbose_name="Kitob nomi")
    author = models.CharField(max_length=100, verbose_name='Муаллифи')
    date = models.DateTimeField(verbose_name="olingan vaqti", blank=True, null=True)
    key = models.CharField(max_length=25)
    respite = models.DateTimeField(blank=True, null=True)
    objects = models.Manager()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.book_name


class SendMessages(models.Model):
    name = models.CharField(max_length=100, verbose_name='Ism', blank=True)
    title = models.CharField(max_length=100, verbose_name='Mavzu')
    body = models.CharField(max_length=1000, verbose_name='Xabar matni')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.name


class Check(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE, blank=True, null=True)
    created = models.DateTimeField(editable=False, auto_now_add=True)
    book_name = models.CharField(max_length=50, verbose_name="Kitob nomi")
    author = models.CharField(max_length=100, verbose_name='Муаллифи')
    date = models.DateField(verbose_name="olingan vaqti", blank=True, null=True)
    key = models.CharField(max_length=25)
    objects = models.Manager()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.book_name


class EmplayeeMessages(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.name



class Book(models.Model):
    book_name = models.CharField(max_length=100, verbose_name='Китоб номи',blank=True, null=True)
    key = models.CharField(max_length=25, verbose_name='Инвентар рақами')
    author = models.CharField(max_length=100, verbose_name='Муаллифи',blank=True, null=True)
    organization= models.CharField(max_length=200, verbose_name="Тавсия қилган ташкилот",blank=True, null=True)
    publishing = models.CharField(max_length=100, verbose_name="Нашриёт",blank=True, null=True)
    book_type = models.CharField(max_length=25,blank=True, null=True)
    language = models.CharField(max_length=25,blank=True, null=True)
    year =models.CharField(max_length=50, verbose_name="Йили",blank=True, null=True)
    beti = models.CharField(max_length=50, verbose_name="Бети",blank=True, null=True)
    isbn = models.CharField(max_length=50, verbose_name="ISBN")
    money = models.CharField(max_length=25, verbose_name="Сумма",blank=True, null=True)
    objects = models.Manager()
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ('-created_at',)
    
    def __str__(self):
        return self.book_name

@receiver(post_save, sender=CustomUser)
# Now Creating a Function which will
# automatically insert data in HOD, Staff or Student
def create_user_profile(sender, instance, created, **kwargs):
    # if Created is true (Means Data Inserted)
    if created:

        # Check the user_type and insert the data in respective tables
        if instance.user_type == 1:
            AdminHOD.objects.create(admin=instance)
        if instance.user_type == 2:
            Staffs.objects.create(admin=instance)
        if instance.user_type == 3:
            Students.objects.create(admin=instance)


@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == 1:
        instance.adminhod.save()
    if instance.user_type == 2:
        instance.staff.save()
    if instance.user_type == 3:
        instance.student.save()
