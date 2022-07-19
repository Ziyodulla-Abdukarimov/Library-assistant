from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from accounts.models import Group, Return_Book, Students, EmplayeeMessages, Accept_Book, Book
from django.db.models import Count

@login_required(login_url='login')
def staff(request):
    context = {
        'group': Group.objects.all().count,
        'accept': Accept_Book.objects.all().count(),
        'all': Book.objects.all().count(),
        'sms' : EmplayeeMessages.objects.all(),
        'data': timezone.now(),
        'null': Students.objects.filter(return_book__isnull=True).count(),
        'good': Students.objects.all().count()- Students.objects.filter(return_book__isnull=True).count(),
        'student': Students.objects.all().count(),
        'bookers': Students.objects.annotate(num=Count('return_book')).order_by('-num')[:5],
    }
    return render(request, 'staff/staff.html', context)