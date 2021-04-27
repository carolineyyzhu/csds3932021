from django.shortcuts import render
from .models import Course

# Create your views here.
def index(request):
    context = {}
    return render(request, 'index.html', context)


def posb(request):
    cid = []
    name = []
    numberDept = []
    classes = Course.objects.all()
    for courses in classes:
        cid.append(courses.cid)
        name.append(courses.name)
        temp = courses.department + str(courses.number)
        numberDept.append(temp)
    toHTML1 = [cid, name, numberDept]
    toHTML = zip(toHTML1[0],toHTML1[1],toHTML1[2])
    context = {"classes": toHTML}
    return render(request, 'ProgramBuilder.html', context)

def rchecker(request):
    context = {}
    return render(request, 'RequirementChecker.html', context)
