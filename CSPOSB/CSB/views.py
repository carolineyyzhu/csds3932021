from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import Course, Fulfills, Requirement, Requires, Degree


# Create your views here.
def index(request):
    context = {}
    return render(request, 'index.html', context)

@csrf_exempt
def posb(request):
    cid = []
    name = []
    numberDept = []

    # Breadth
    breadthClasses = Course.objects.all().select_related().filter(fulfills__rid=2)
    for courses in breadthClasses:
        cid.append(courses.cid)
        name.append(courses.name)
        temp = courses.department + str(courses.number)
        numberDept.append(temp)
    breadthToHTML1 = [cid, name, numberDept]
    cid =[]
    name = []
    numberDept = []
    breadthToHTML = zip(breadthToHTML1[0], breadthToHTML1[1], breadthToHTML1[2])

    # Depth
    depthClasses = Course.objects.all().select_related().filter(fulfills__rid=1)
    for courses in depthClasses:
        cid.append(courses.cid)
        name.append(courses.name)
        temp = courses.department + " " + str(courses.number)
        numberDept.append(temp)
    depthToHTML1 = [cid, name, numberDept]
    cid =[]
    name = []
    numberDept = []
    depthToHTML = zip(depthToHTML1[0], depthToHTML1[1], depthToHTML1[2])

    # Core
    coreClasses = Course.objects.all().select_related().filter(fulfills__rid=9)
    for courses in coreClasses:
        cid.append(courses.cid)
        name.append(courses.name)
        temp = courses.department + str(courses.number)
        numberDept.append(temp)
    coreToHTML1 = [cid, name, numberDept]
    cid =[]
    name = []
    numberDept = []
    coreToHTML = zip(coreToHTML1[0], coreToHTML1[1], coreToHTML1[2])

    # General Breadth
    generalBreadthClasses = Course.objects.all().select_related().filter(fulfills__rid=8)
    for courses in generalBreadthClasses:
        cid.append(courses.cid)
        name.append(courses.name)
        temp = courses.department + str(courses.number)
        numberDept.append(temp)
    generalBreadthToHTML1 = [cid, name, numberDept]
    cid =[]
    name = []
    numberDept = []
    generalBreadthToHTML = zip(generalBreadthToHTML1[0], generalBreadthToHTML1[1], generalBreadthToHTML1[2])

    # Technical Elective
    techElectiveClasses = Course.objects.all().select_related().filter(fulfills__rid=4)
    for courses in techElectiveClasses:
        cid.append(courses.cid)
        name.append(courses.name)
        temp = courses.department + str(courses.number)
        numberDept.append(temp)
    techElectiveToHTML1 = [cid, name, numberDept]
    cid =[]
    name = []
    numberDept = []
    techElectiveToHTML = zip(techElectiveToHTML1[0], techElectiveToHTML1[1], techElectiveToHTML1[2])

    # Sages
    sagesClasses = Course.objects.all().select_related().filter(fulfills__rid=3)
    for courses in sagesClasses:
        cid.append(courses.cid)
        name.append(courses.name)
        temp = courses.department + str(courses.number)
        numberDept.append(temp)
    sagesToHTML1 = [cid, name, numberDept]
    sagesToHTML = zip(sagesToHTML1[0], sagesToHTML1[1], sagesToHTML1[2])

    context = {"generalBreadthClasses": generalBreadthToHTML, "coreClasses": coreToHTML,
               "breadthClasses": breadthToHTML, "depthClasses": depthToHTML, "sagesClasses": sagesToHTML,
               "techElectiveClasses": techElectiveToHTML}

    return render(request, 'ProgramBuilder.html', context)


def rchecker(request):
    context = {}
    return render(request, 'RequirementChecker.html', context)
