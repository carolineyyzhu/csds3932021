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

    # Gets all classes by requirement for display on schedule builder form
    # Breadth
    breadthClasses = Course.objects.all().select_related().filter(fulfills__rid=2)
    for courses in breadthClasses:
        cid.append(courses.cid)
        name.append(courses.name)
        temp = courses.department + " " + str(courses.number)
        numberDept.append(temp)
    breadthToHTML1 = [cid, name, numberDept]
    cid = []
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
    cid = []
    name = []
    numberDept = []
    depthToHTML = zip(depthToHTML1[0], depthToHTML1[1], depthToHTML1[2])

    # Core
    coreClasses = Course.objects.all().select_related().filter(fulfills__rid=9)
    for courses in coreClasses:
        cid.append(courses.cid)
        name.append(courses.name)
        temp = courses.department + " " + str(courses.number)
        numberDept.append(temp)
    coreToHTML1 = [cid, name, numberDept]
    cid = []
    name = []
    numberDept = []
    coreToHTML = zip(coreToHTML1[0], coreToHTML1[1], coreToHTML1[2])

    # General Breadth
    generalBreadthClasses = Course.objects.all().select_related().filter(fulfills__rid=8)
    for courses in generalBreadthClasses:
        cid.append(courses.cid)
        name.append(courses.name)
        temp = courses.department + " " + str(courses.number)
        numberDept.append(temp)
    generalBreadthToHTML1 = [cid, name, numberDept]
    cid = []
    name = []
    numberDept = []
    generalBreadthToHTML = zip(generalBreadthToHTML1[0], generalBreadthToHTML1[1], generalBreadthToHTML1[2])

    # Technical Elective
    techElectiveClasses = Course.objects.all().select_related().filter(fulfills__rid=4)
    for courses in techElectiveClasses:
        cid.append(courses.cid)
        name.append(courses.name)
        temp = courses.department + " " + str(courses.number)
        numberDept.append(temp)
    techElectiveToHTML1 = [cid, name, numberDept]
    cid = []
    name = []
    numberDept = []
    techElectiveToHTML = zip(techElectiveToHTML1[0], techElectiveToHTML1[1], techElectiveToHTML1[2])

    # Sages
    sagesClasses = Course.objects.all().select_related().filter(fulfills__rid=3)
    for courses in sagesClasses:
        cid.append(courses.cid)
        name.append(courses.name)
        temp = courses.department + " " + str(courses.number)
        numberDept.append(temp)
    sagesToHTML1 = [cid, name, numberDept]
    sagesToHTML = zip(sagesToHTML1[0], sagesToHTML1[1], sagesToHTML1[2])

    # Schedule has been submitted
    f1, s1, f2, s2, f3, s3, f4, s4 = ([],) * 8
    if request.method == "POST":
        form = request.POST.get("builder")
        data = request.POST.copy()
        semester = data.getlist("Semester")
        year = data.getlist("Year")
        classes = data.getlist('Classes')

        toDelete = []
        removeEmpty=[]
        for i in range(0,len(classes)):
            if classes[i] != "empty":
                removeEmpty.append(i-1)
        removeEmpty.reverse()
        for index in removeEmpty:
            classes.pop(index)
        for i in range(0, len(classes)):
            if classes[i] == "empty":
                toDelete.append(i)
        toDelete.reverse()
        for index in range(0, len(toDelete)):
            semester.pop(toDelete[index])
            year.pop(toDelete[index])
            classes.pop(toDelete[index])

        for i in range(0, len(classes)):
            if semester == "spring":
                if year == 1:
                    s1.append(classes[i])
                if year == 4:
                    s2.append(classes[i])
                if year == 3:
                    s3.append(classes[i])
                else:
                    s4.append(classes[i])
            else:
                if year == 1:
                    f1.append(classes[i])
                if year == 4:
                    f2.append(classes[i])
                if year == 3:
                    f3.append(classes[i])
                else:
                    f4.append(classes[i])

        areReqFulfilled, missingReq = checkRequirements(classes)

        context = {'classes': classes, 'areReqFulfilled': areReqFulfilled, 'missingReq': missingReq}
        return render(request, 'RequirementChecker.html', context)
    else:
        context = {"generalBreadthClasses": generalBreadthToHTML, "coreClasses": coreToHTML,
                   "breadthClasses": breadthToHTML, "depthClasses": depthToHTML, "sagesClasses": sagesToHTML,
                   "techElectiveClasses": techElectiveToHTML}
        return render(request, 'ProgramBuilder.html', context)


def rchecker(request):
    context = {"fulfillsRequirements":False, "classesNeeded":None}
    return render(request, 'RequirementChecker.html', context)


def checkRequirements(classes):
    while('empty' in classes):
        classes.remove('empty')

    #TODO: Get the actual value of the depth area
    #TODO: Add group 1 and group 2 to database
    depth_area = "Software Engineering"
    are_reqs_fulfilled = True
    missing_reqs = []

    cs_requirement_nums = {"total_cs_credits":0, "total_cs_courses":0, "core_courses":0, "breadth_courses":0, "depth_courses":0, "tech_group_1": 0, "tech_group_2":0}
    can_be_counted = {"depth":False, "breadth":False, "tech-elective":False}

    for course in classes:
        dept_id = course[0:4]
        course_id = course[5:8]

        if Course.objects.filter(department=dept_id,number=course_id).exists():
            cs_requirement_nums["tech_group_1"] += 1

        if dept_id == "CSDS" and Course.objects.filter(department=dept_id,number=course_id).exists():
            cs_requirement_nums["total_cs_credits"] += Course.objects.get(department=dept_id,number=course_id).credits
            cs_requirement_nums["total_cs_courses"] += 1

        course_name = Course.objects.get(department=dept_id, number=course_id).cid
        #TODO: make sure that this is the same as the depth from above
        can_be_counted["depth"] = Fulfills.objects.get(cid=course_name).rid == "Depth"
        can_be_counted["breadth"] = Fulfills.objects.get(cid=course_name).rid == "Breadth"


        if can_be_counted["depth"]:
            cs_requirement_nums["depth_courses"] += 1
        if can_be_counted["breadth"]:
            cs_requirement_nums["breadth_courses"] += 1
        #TODO: Fulfills needs classes that can be counted toward the tech electives
        #elif not can_be_counted["depth"]:

    is_fulfilled = {"is_cs_credits_fulfilled":cs_requirement_nums["total_cs_credits"] > 63,
                    "is_cs_courses_fulfilled":cs_requirement_nums["total_cs_courses"] > 20,
                    "is_core_fulfilled":cs_requirement_nums["core_courses"] > 6,
                    "is_breadth_fulfilled":cs_requirement_nums["breadth_courses"] > 5,
                    "is_depth_fulfilled":cs_requirement_nums["depth_courses"] > 4,
                    "is_tech_fulfilled":cs_requirement_nums["tech_group_1"] + cs_requirement_nums["tech_group_2"] <= 6 and cs_requirement_nums["tech_group_2"] <= 2}

    if not is_fulfilled["is_cs_credits_fulfilled"]:
        missing_reqs.append("Total CS Credits")
    if not is_fulfilled["is_cs_courses_fulfilled"]:
        missing_reqs.append("Total CS Courses")
        #TODO: display all technical electives to fulfill this requirement
    if not is_fulfilled["is_core_fulfilled"]:
        missing_reqs.append("Core Courses")
    if not is_fulfilled["is_breadth_fulfilled"]:
        missing_reqs.append("Breadth Courses")
    if not is_fulfilled["is_depth_fulfilled"]:
        missing_reqs.append("Depth Courses")

    print("missing_reqs" + str(missing_reqs))

    if not all(not value for value in is_fulfilled.values()):
        are_reqs_fulfilled = False

    return are_reqs_fulfilled, missing_reqs