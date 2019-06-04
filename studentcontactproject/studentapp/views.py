from django.shortcuts import render
from .models import StudentData
from .forms import StudentForm
from django.http import HttpResponse

def Student_Views(request):
    if request.method=='POST':
        sform = StudentForm(request.POST)
        if sform.is_valid():
            sno1 = request.POST.get('sno')
            sname1 = request.POST.get('sname')
            sloc1 = request.POST.get('sloc')
            sfee1 = request.POST.get('sfee')

            a = StudentData(
                sno = sno1,
                sname = sname1,
                sloc=sloc1,
                sfee=sfee1
            )
            a.save()
            sform = StudentForm()
            return render(request,'studentdata.html',{'abcd':sform})
        else:
            return HttpResponse('User invalid data')
    else:
        sform = StudentForm()
        return render(request,'studentdata.html',{'abcd':sform})



